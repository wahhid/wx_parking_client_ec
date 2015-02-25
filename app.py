import wx
from logindialog import *
from parkingclient import ManlessDialog
import ConfigParser, os

		
class Parking_ClientMain(wx.App):
	
	def OnInit(self):
		self.logindialog = Parking_LoginDialog(None)
		self.logindialog.Show()
		return True
	
	
class Parking_ManlessMain(wx.App):
	
	def OnInit(self):
		self.manlessframe = ManlessDialog(None)
		self.manlessframe.Show()
		return True

config = ConfigParser.ConfigParser()
config.read("parking.cfg")

def ConfigSectionMap(section):
    dict1 = {}
    options = config.options(section)
    for option in options:
        try:
            dict1[option] = config.get(section, option)
        except:
            dict1[option] = None
    return dict1
  
serverip = ConfigSectionMap("General")['ServerIp']
serverport = ConfigSectionMap("General")['ServerPort']
appusername = ConfigSectionMap("General")['AppUserName']
apppassword = ConfigSectionMap("General")['AppPassword'] 
boothtype = ConfigSectionMap("General")['BoothType']

if serverip and serverport and appusername and apppassword and boothtype:
	if boothtype == 'manless':	
		app = Parking_ClientMain(0)		
		app.MainLoop()
	
	if boothtype == 'normalin':
		pass
	