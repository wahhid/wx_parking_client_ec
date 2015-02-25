import xmlrpclib
from openerp import *
from parkingclient import *
import xmlrpclib
import datetime
import time

class Parking_PricingDialog(PricingDialog):
	
	def __init__(self,parent):
		PricingDialog.__init__(self,parent)
		self.parent = parent	
		
		#Init OpenERP Class
		self.openerp = Openerp(self)
		self.sock_object = self.openerp.sock_object()
		self.sock_common = self.openerp.sock_common()
		self.dbname = self.openerp.dbname	
		self.uid = self.parent.uid
		self.password = self.parent.password
		
		#filepath = 'images/1.jpg'
		#img = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
		#SizeX, SizeY = self.bitmap_pricing.GetSize()
		#img = img.Scale(SizeX, SizeY ,wx.IMAGE_QUALITY_HIGH)
		#self.bitmap_pricing.SetBitmap(wx.BitmapFromImage(img))		
		#self.bitmap_pricing.SetFocus()		
		self.listbox_pricing.Append("Car")
		self.listbox_pricing.Append("Motor Cycle")
		self.listbox_pricing.Append("Truck")
		self.listbox_pricing.Select(0)
						
	def commit_pricing(self,event):
		x = event.GetKeyCode()
		count = self.listbox_pricing.GetCount()
		if x == wx.WXK_DOWN:
			current_index = self.listbox_pricing.GetSelection()
			if current_index + 1 <= count:
				self.listbox_pricing.SetSelection(current_index + 1)
			print self.listbox_pricing.GetStringSelection()
		elif x == wx.WXK_UP:			
			current_index = self.listbox_pricing.GetSelection()
			if current_index - 1 >= 0 :
				self.listbox_pricing.SetSelection(current_index - 1)			
			print self.listbox_pricing.GetStringSelection()
		elif x == wx.WXK_ESCAPE:
			pricing = self.listbox_pricing.GetStringSelection()
			results = self.get_pricing(pricing)
			if results == None:
				dial = wx.MessageDialog(None, 'Error Get Pricing !', 'Error', wx.OK | wx.ICON_ERROR)
				dial.ShowModal()																	
			else:
				self.parent.pricing_id = results[0]['id']
				self.Destroy()
		
	def get_pricing(self,pricing):					
		args = [('name','=',pricing)]
		ids = self.sock_object.execute(self.dbname, self.uid, self.password, 'parking.pricing', 'search', args)			
		fields = ['name']
		return self.sock_object.execute(self.dbname, self.uid, self.password, 'parking.pricing', 'read', ids, fields)					
		
			
			
			
