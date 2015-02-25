import xmlrpclib
from openerp import *
import serial
from parkingclient import *
from parkingframe import *

class Parking_LoginDialog(LoginDialog):
	
	def __init__(self,parent):
		LoginDialog.__init__(self,parent)			
		#defind OpenErp
		self.openerp = Openerp(self)
		self.sock_object = self.openerp.sock_object()
		self.sock_common  = self.openerp.sock_common()
		self.dbname = self.openerp.dbname
		
		self.company = 'Mulia Intipelangi'				
		filepath = 'images/mulia.jpg'
		img = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
		SizeX, SizeY = self.bitmap_logo.GetSize()
		img = img.Scale(SizeX, SizeY ,wx.IMAGE_QUALITY_HIGH)
		self.bitmap_logo.SetBitmap(wx.BitmapFromImage(img))		
		self.text_username.SetFocus()
			
	def OnClickLoginButton(self,event):
		self.check_authentication()
		self.check_booth()		
		if(self.uid != False ):					
			if(self.booth != False):
				self.parkingframe = Parking_ClientFrame(self)
				self.parkingframe.Show()
				self.text_username.SetValue('')
				self.text_password.SetValue('')
				self.text_booth.SetValue('')
				self.text_username.SetFocus()
				self.Show(False)
				return True
			else:
				dial = wx.MessageDialog(None, 'Username or password or booth was wrong !', 'Error', wx.OK | wx.ICON_ERROR)
				dial.ShowModal()
				return False		
		else:
			dial = wx.MessageDialog(None, 'Username or password or booth was wrong !', 'Error', wx.OK | wx.ICON_ERROR)
			dial.ShowModal()
			return False
				
	def OnClickQuitButton(self,event):
		self.Destroy()
		
	def check_authentication(self):
		self.username = self.text_username.GetValue()
		self.password = self.text_password.GetValue()		
		self.booth = self.text_booth.GetValue()				
		self.uid = self.openerp.auth(self.username,self.password)		
		
	def check_booth(self):						
		args = [('boothid','=',self.booth)]
		ids = self.sock_object.execute(self.dbname, self.uid, self.password, 'parking.booth', 'search', args)
		fields = []
		results = self.sock_object.execute(self.dbname, self.uid, self.password, 'parking.booth', 'read', ids, fields)	
		self.booth = results[0]
		