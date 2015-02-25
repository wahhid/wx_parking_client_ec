import xmlrpclib
from openerp import *
from parkingclient import *
from pricingdialog import *
import threading
import datetime
import time

class Parking_ClientFrame(ParkingFrame):

	def __init__(self,parent):
		ParkingFrame.__init__(self,parent)
		self.parent = parent
		self.transactiontype = 0 #0=in,1=out
		self.shift = 0
		
		#Init OpenERP Class
		self.openerp = Openerp(self)
		self.sock_object = self.openerp.sock_object()
		self.sock_common = self.openerp.sock_common()
		self.dbname = self.openerp.dbname
		self.uid = self.parent.uid
		self.password = self.parent.password
		
		self.status = 0
		self.exit_process_status = 0
		self.parent = parent			
		self.booth = parent.booth
		self.pricing_id = 0
		self.label_operator.SetLabel(str(self.parent.username))
		self.label_company.SetLabel(self.parent.company)
		self.label_booth.SetLabel(self.parent.booth['name'])
		if self.parent.booth['type'] == '01':
			self.label_type.SetLabel('In')	
		if self.parent.booth['type'] == '02':
			self.label_type.SetLabel('Out')
		if self.parent.booth['type'] == '03':
			self.label_type.SetLabel('In / Out')								
		self.label_datetime.SetLabel(datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
		
	def refresh_datetime(self,event):
		self.label_datetime.SetLabel(datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
		
	def ucase_text(self,event):
		selection = self.text_car_or_rfid.GetSelection()
		value = self.text_car_or_rfid.GetValue().upper()
		self.text_car_or_rfid.ChangeValue(value)
		self.text_car_or_rfid.SetSelection(*selection)		
		
	def process_steps(self,event):		
		x = event.GetKeyCode()		
		if x == wx.WXK_F4:
			self.parent.Show(True)
			self.Destroy()		
		elif x == wx.WXK_RETURN:
			if self.exit_process_status == 0:
				if len(self.text_car_or_rfid.GetValue()) > 0:
					tp = self.find_vehicle(self.text_car_or_rfid.GetValue())
					if len(tp) == 1:					
						if self.parent.booth['type'] == '01':
							print 'Car Exist and Stop transaction'
							dial = wx.MessageDialog(None, 'Car Exist !', 'Error', wx.OK | wx.ICON_ERROR)
							dial.ShowModal()						
						elif self.parent.booth['type'] == '02':
							print 'Car Exist and Continue for exit'		
							self.pricingdialog = Parking_PricingDialog(self)
							self.pricingdialog.ShowModal()							
							self.status = 1							
							self.exit_process(tp[0])														
						elif self.parent.booth['type'] == '03':
							print 'Car Exist and Continue for exit'
							self.pricingdialog = Parking_PricingDialog(self)
							self.pricingdialog.ShowModal()							
							self.status = 1
							self.exit_process(tp[0])					
					else:			
						if self.parent.booth['type'] == '01':
							print 'Car Not Exist and Continue transaction'
							print 'New Transacation'										
							self.status = 0
							self.entry_process(self.text_car_or_rfid.GetValue())												
							self.text_car_or_rfid.SetValue('')
						elif self.parent.booth['type'] == '02':
							print 'Car Not Exist and Stop Transaction'
							dial = wx.MessageDialog(None, 'Car Not Exist !', 'Error', wx.OK | wx.ICON_ERROR)
							dial.ShowModal()													
						elif self.parent.booth['type'] == '03':
							print 'Car Not Exist and Continue for entry'				
							print 'New Transacation'			
							self.entry_process(self.text_car_or_rfid.GetValue())																				
							self.text_car_or_rfid.SetValue('')
			else:
				self.text_car_or_rfid.SetValue('')
				self.status = 0
				self.exit_process_status = 0
				self.clear_view()
						
		elif x == wx.WXK_BACK:
			self.text_car_or_rfid.SetValue(self.text_car_or_rfid.GetValue()[:-1])
		elif x == wx.WXK_ESCAPE:
			if len(self.text_car_or_rfid.GetValue()) > 0:
				self.text_car_or_rfid.SetValue('')
			else:
				self.parent.Show(True)
				self.Destroy()
		else:			
			if x >= 97 & x <= 122:
				self.text_car_or_rfid.AppendText(str(unichr(x)))
	
	def selected_pricing(self,event):
		self.text_car_or_rfid.SetFocus()
	
	def entry_process(self,barcode):				
		#find shift
		shift_id = self.find_shift()
		print "Shift ID : " + str(shift_id)
		#define value	
		values = {}	
		values.update({'transid':datetime.datetime.now().strftime('%Y%m%d%H%M%S')})		
		values.update({'carnumber':barcode})
		values.update({'transtype':0})					
		values.update({'datetimein':datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
		#datetimein = datetime.datetime.now()
		#values.update({'datetimein': xmlrpclib.DateTime(datetimein)})
		values.update({'datein':datetime.datetime.now().strftime('%Y-%m-%d')})
		values.update({'oprin':self.parent.uid})				
		values.update({'boothin':self.parent.booth['id']})						
		values.update({'shiftin':1})
		print values
		#defind model
		model = 'parking.transparking'					
		#create process		
		return self.sock_object.execute(self.parent.dbname, self.parent.uid, self.parent.password,model,'create',values);				
	
	def exit_process(self,tp):
		id = tp['id']
		
		#find shift
		shift_id = self.find_shift()
		print "Shift ID : " + str(shift_id)	
		
		#define values
		values = {}				
		values.update({'pricing':self.pricing_id})
		values.update({'datetimeout':datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
		values.update({'dateout':datetime.datetime.now().strftime('%Y-%m-%d')})
		values.update({'oprout':self.parent.uid})				
		values.update({'boothout':self.parent.booth['id']})
		values.update({'shiftout':1})
		values.update({'status':True})
		#define model
		model = 'parking.transparking'
		#Write Transaction		
		tpwrite = self.sock_object.execute(self.parent.dbname, self.parent.uid, self.parent.password, model, 'write', [id], values)	
		if tpwrite:
			fields = []
			tps = self.sock_object.execute(self.parent.dbname, self.parent.uid, self.parent.password, 'parking.transparking', 'read', [id], fields)			
			print tps
			tp = tps[0]
			self.fill_view(tp)
			self.exit_process_status = 1
	
	def _shifts(self):
		args = []
		ids = self.sock_object.execute(self.parent.dbname, self.parent.uid, self.parent.password, 'parking.shift', 'search', args)			
		fields = []
		return self.sock_object.execute(self.parent.dbname, self.parent.uid, self.parent.password, 'parking.shift', 'read', ids, fields)							
		
	def find_shift(self):						
		current_date_time = datetime.datetime.now()		
		str_current_date = datetime.datetime.now().strftime("%Y-%m-%d")
		shifts = self._shifts()
		for shift in shifts:
			if shift['nextday'] == False:
				print "Same Day"
				arrstarttime = str(shift['startime']).split(".")
				arrendtime = str(shift['endtime']).split(".")								
				startdatetime = datetime.datetime.strptime(str_current_date + " " + arrstarttime[0] + ":" + arrstarttime[1] + ":" + "0","%Y-%m-%d %H:%M:%S")
				startendtime = datetime.datetime.strptime(str_current_date + " " + arrendtime[0] + ":" + arrendtime[1] + ":" + "0","%Y-%m-%d %H:%M:%S")
				if current_date_time >= startdatetime & current_date_time <= enddatettime:
					self.shift = shift['id']
			else:
				print "Next Day"
				arrstarttime = str(shift['startime']).split(".")			
				arrendtime = str(shift['endtime']).split(".")
				nextmiddledatetime = datetime.datetime.strptime(str_current_date + "0:0:0","%Y-%m-%d %H:%M:%S")
				nextenddatetime = datetime.datetime.strptime(str_current_date + " " + arrendtime[0] + ":" + arrendtime[1] + ":" + "0","%Y-%m-%d %H:%M:%S")
				if current_date_time >= nextmiddledatetime & current_date_time <= nextsenddatettime:
					self.shift = shift['id']
				else:
					beforemiddledatetime = datetime.datetime.strptime(str_current_date + "0:0:0","%Y-%m-%d %H:%M:%S")
					beforestartdatetime = datetime.datetime.strptime(str_current_date + " " + arrstarttime[0] + ":" + arrstarttime[1] + ":" + "0","%Y-%m-%d %H:%M:%S")
					if current_date_time >= beforestartdatetime & current_date_time <= beforemiddledatettime:
						self.shift = shift['id']
										
	def find_vehicle(self,carnumber):		
		args = [('carnumber','=',self.text_car_or_rfid.GetValue()),('status','=',False)]
		ids = self.sock_object.execute(self.parent.dbname, self.parent.uid, self.parent.password, 'parking.transparking', 'search', args)			
		fields = []
		return self.sock_object.execute(self.parent.dbname, self.parent.uid, self.parent.password, 'parking.transparking', 'read', ids, fields)					
				
	def fill_view(self,tp):	
		self.label_carnumber.SetLabel(tp['carnumber'])
		if tp['transtype'] == 0:
			self.label_transtype.SetLabel('Normal')
		else:
			self.label_transtype.SetLabel('Manual')			
		self.label_boothin.SetLabel(tp['boothin'][1])
		self.label_datetimein.SetLabel(tp['datetimein'])
		self.label_operatorin.SetLabel(tp['oprin'][1])
		self.label_shiftin.SetLabel(tp['shiftin'][1])
		if tp['driverin'] == False:
			self.label_driverin.SetLabel('-')
		else:
			self.label_driverin.SetLabel(tp['driverin'][1])
		self.label_boothout.SetLabel(tp['boothout'][1])
		self.label_datetimeout.SetLabel(tp['datetimeout'])
		self.label_operatorout.SetLabel(tp['oprout'][1])
		self.label_shiftout.SetLabel(tp['shiftout'][1])
		if tp['driverout'] == False:
			self.label_driverout.SetLabel('-')		
		else:
			self.label_driverout.SetLabel(tp['driverout'][1])		
			
		if self.status == 1:
			duration = '{0} Hours and {1} Minutes'.format(str(tp['hours']),str(tp['minutes']))
			self.label_duration.SetLabel(duration)
			self.label_parkingfee.SetLabel(str(tp['hourly_charges']))
			self.label_servicefee.SetLabel(str(tp['services_charges']))
			self.label_missingfee.SetLabel(str(tp['missing_charges']))
			self.label_limitfee.SetLabel(str(tp['limit_charges']))
			self.label_totalfee.SetLabel(str(tp['total_charges']))
			
	def clear_view(self):
		self.label_carnumber.SetLabel('-')		
		self.label_type.SetLabel('-')		
		self.label_boothin.SetLabel('-')
		self.label_datetimein.SetLabel('-')
		self.label_operatorin.SetLabel('-')
		self.label_shiftin.SetLabel('-')
		self.label_driverin.SetLabel('-')
		self.label_boothout.SetLabel('-')
		self.label_datetimeout.SetLabel('-')
		self.label_operatorout.SetLabel('-')
		self.label_shiftout.SetLabel('-')
		self.label_driverout.SetLabel('-')				
		self.label_duration.SetLabel('-')
		self.label_parkingfee.SetLabel('-')
		self.label_servicefee.SetLabel('-')
		self.label_missingfee.SetLabel('-')
		self.label_limitfee.SetLabel('-')
		self.label_totalfee.SetLabel('-')
		self.pricing_id = 0
		self.shift = 0
