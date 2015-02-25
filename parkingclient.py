# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Nov 10 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class LoginDialog
###########################################################################

class LoginDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Login - Parking Client", pos = wx.DefaultPosition, size = wx.Size( 348,314 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer1 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer1.AddGrowableCol( 0 )
		fgSizer1.AddGrowableRow( 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.bitmap_logo = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.bitmap_logo, 0, wx.ALL|wx.EXPAND, 5 )
		
		fgSizer10 = wx.FlexGridSizer( 4, 2, 0, 0 )
		fgSizer10.AddGrowableCol( 1 )
		fgSizer10.SetFlexibleDirection( wx.BOTH )
		fgSizer10.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		fgSizer10.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.text_username = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.text_username, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		fgSizer10.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.text_password = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		fgSizer10.Add( self.text_password, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Booth", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		fgSizer10.Add( self.m_staticText16, 0, wx.ALL, 5 )
		
		self.text_booth = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.text_booth, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		fgSizer10.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		fgSizer2 = wx.FlexGridSizer( 1, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.button_login = wx.Button( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.button_login, 0, wx.ALL, 5 )
		
		self.button_quit = wx.Button( self, wx.ID_ANY, u"Quit", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.button_quit, 0, wx.ALL, 5 )
		
		
		fgSizer10.Add( fgSizer2, 1, wx.EXPAND, 5 )
		
		
		fgSizer1.Add( fgSizer10, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( fgSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.button_login.Bind( wx.EVT_BUTTON, self.OnClickLoginButton )
		self.button_quit.Bind( wx.EVT_BUTTON, self.OnClickQuitButton )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnClickLoginButton( self, event ):
		event.Skip()
	
	def OnClickQuitButton( self, event ):
		event.Skip()
	

###########################################################################
## Class ParkingFrame
###########################################################################

class ParkingFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Parking Client", pos = wx.DefaultPosition, size = wx.Size( 743,606 ), style = wx.MAXIMIZE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer3 = wx.FlexGridSizer( 3, 1, 0, 0 )
		fgSizer3.AddGrowableCol( 0 )
		fgSizer3.AddGrowableRow( 2 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer4 = wx.FlexGridSizer( 6, 4, 0, 0 )
		fgSizer4.AddGrowableCol( 1 )
		fgSizer4.AddGrowableCol( 3 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Company", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		self.m_staticText4.SetFont( wx.Font( 12, 74, 90, 90, False, "Arial" ) )
		
		fgSizer4.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.label_company = wx.StaticText( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_company.Wrap( -1 )
		self.label_company.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer4.Add( self.label_company, 0, wx.ALL, 5 )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Date & Time", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		self.m_staticText6.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer4.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.label_datetime = wx.StaticText( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_datetime.Wrap( -1 )
		self.label_datetime.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer4.Add( self.label_datetime, 0, wx.ALL, 5 )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Operator", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		self.m_staticText8.SetFont( wx.Font( 12, 74, 90, 90, False, "Arial" ) )
		
		fgSizer4.Add( self.m_staticText8, 0, wx.ALL, 5 )
		
		self.label_operator = wx.StaticText( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_operator.Wrap( -1 )
		self.label_operator.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer4.Add( self.label_operator, 0, wx.ALL, 5 )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		self.m_staticText10.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer4.Add( self.m_staticText10, 0, wx.ALL, 5 )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		self.m_staticText11.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer4.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Booth", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		self.m_staticText12.SetFont( wx.Font( 12, 74, 90, 90, False, "Arial" ) )
		
		fgSizer4.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		self.label_booth = wx.StaticText( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_booth.Wrap( -1 )
		self.label_booth.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer4.Add( self.label_booth, 0, wx.ALL, 5 )
		
		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Type", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		self.m_staticText14.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer4.Add( self.m_staticText14, 0, wx.ALL, 5 )
		
		self.label_type = wx.StaticText( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_type.Wrap( -1 )
		self.label_type.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer4.Add( self.label_type, 0, wx.ALL, 5 )
		
		
		fgSizer3.Add( fgSizer4, 1, wx.EXPAND, 5 )
		
		self.text_car_or_rfid = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,100 ), wx.TE_LEFT )
		self.text_car_or_rfid.SetFont( wx.Font( 60, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer3.Add( self.text_car_or_rfid, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		fgSizer9 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer9.AddGrowableCol( 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		fgSizer6 = wx.FlexGridSizer( 12, 2, 2, 2 )
		fgSizer6.AddGrowableCol( 1 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"Car Number", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		fgSizer6.Add( self.m_staticText17, 0, wx.ALL, 5 )
		
		self.label_carnumber = wx.StaticText( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_carnumber.Wrap( -1 )
		fgSizer6.Add( self.label_carnumber, 0, wx.ALL, 5 )
		
		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Type", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		fgSizer6.Add( self.m_staticText19, 0, wx.ALL, 5 )
		
		self.label_transtype = wx.StaticText( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_transtype.Wrap( -1 )
		fgSizer6.Add( self.label_transtype, 0, wx.ALL, 5 )
		
		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Booth In", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		fgSizer6.Add( self.m_staticText21, 0, wx.ALL, 5 )
		
		self.label_boothin = wx.StaticText( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_boothin.Wrap( -1 )
		fgSizer6.Add( self.label_boothin, 0, wx.ALL, 5 )
		
		self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"Date Time In", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )
		fgSizer6.Add( self.m_staticText30, 0, wx.ALL, 5 )
		
		self.label_datetimein = wx.StaticText( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_datetimein.Wrap( -1 )
		fgSizer6.Add( self.label_datetimein, 0, wx.ALL, 5 )
		
		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u"Operator In", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )
		fgSizer6.Add( self.m_staticText32, 0, wx.ALL, 5 )
		
		self.label_operatorin = wx.StaticText( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_operatorin.Wrap( -1 )
		fgSizer6.Add( self.label_operatorin, 0, wx.ALL, 5 )
		
		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u"Shift In", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )
		fgSizer6.Add( self.m_staticText34, 0, wx.ALL, 5 )
		
		self.label_shiftin = wx.StaticText( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_shiftin.Wrap( -1 )
		fgSizer6.Add( self.label_shiftin, 0, wx.ALL, 5 )
		
		self.m_staticText36 = wx.StaticText( self, wx.ID_ANY, u"Driver In", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )
		fgSizer6.Add( self.m_staticText36, 0, wx.ALL, 5 )
		
		self.label_driverin = wx.StaticText( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_driverin.Wrap( -1 )
		fgSizer6.Add( self.label_driverin, 0, wx.ALL, 5 )
		
		self.m_staticText38 = wx.StaticText( self, wx.ID_ANY, u"Booth Out", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText38.Wrap( -1 )
		fgSizer6.Add( self.m_staticText38, 0, wx.ALL, 5 )
		
		self.label_boothout = wx.StaticText( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_boothout.Wrap( -1 )
		fgSizer6.Add( self.label_boothout, 0, wx.ALL, 5 )
		
		self.m_staticText40 = wx.StaticText( self, wx.ID_ANY, u"Date Time Out", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40.Wrap( -1 )
		fgSizer6.Add( self.m_staticText40, 0, wx.ALL, 5 )
		
		self.label_datetimeout = wx.StaticText( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_datetimeout.Wrap( -1 )
		fgSizer6.Add( self.label_datetimeout, 0, wx.ALL, 5 )
		
		self.m_staticText42 = wx.StaticText( self, wx.ID_ANY, u"Operator Out", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )
		fgSizer6.Add( self.m_staticText42, 0, wx.ALL, 5 )
		
		self.label_operatorout = wx.StaticText( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_operatorout.Wrap( -1 )
		fgSizer6.Add( self.label_operatorout, 0, wx.ALL, 5 )
		
		self.m_staticText44 = wx.StaticText( self, wx.ID_ANY, u"Shift Out", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )
		fgSizer6.Add( self.m_staticText44, 0, wx.ALL, 5 )
		
		self.label_shiftout = wx.StaticText( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_shiftout.Wrap( -1 )
		fgSizer6.Add( self.label_shiftout, 0, wx.ALL, 5 )
		
		self.m_staticText46 = wx.StaticText( self, wx.ID_ANY, u"Driver Out", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText46.Wrap( -1 )
		fgSizer6.Add( self.m_staticText46, 0, wx.ALL, 5 )
		
		self.label_driverout = wx.StaticText( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_driverout.Wrap( -1 )
		fgSizer6.Add( self.label_driverout, 0, wx.ALL, 5 )
		
		
		bSizer3.Add( fgSizer6, 1, wx.EXPAND, 5 )
		
		fgSizer8 = wx.FlexGridSizer( 6, 2, 2, 2 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"Duration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		fgSizer8.Add( self.m_staticText23, 0, wx.ALL, 5 )
		
		self.label_duration = wx.StaticText( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_duration.Wrap( -1 )
		fgSizer8.Add( self.label_duration, 0, wx.ALL, 5 )
		
		self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, u"Parking Fee", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		fgSizer8.Add( self.m_staticText25, 0, wx.ALL, 5 )
		
		self.label_parkingfee = wx.StaticText( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_parkingfee.Wrap( -1 )
		fgSizer8.Add( self.label_parkingfee, 0, wx.ALL, 5 )
		
		self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, u"Services Fee", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )
		fgSizer8.Add( self.m_staticText27, 0, wx.ALL, 5 )
		
		self.label_servicefee = wx.StaticText( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_servicefee.Wrap( -1 )
		fgSizer8.Add( self.label_servicefee, 0, wx.ALL, 5 )
		
		self.m_staticText48 = wx.StaticText( self, wx.ID_ANY, u"Missing Fee", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText48.Wrap( -1 )
		fgSizer8.Add( self.m_staticText48, 0, wx.ALL, 5 )
		
		self.label_missingfee = wx.StaticText( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_missingfee.Wrap( -1 )
		fgSizer8.Add( self.label_missingfee, 0, wx.ALL, 5 )
		
		self.m_staticText50 = wx.StaticText( self, wx.ID_ANY, u"Limit Fee", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText50.Wrap( -1 )
		fgSizer8.Add( self.m_staticText50, 0, wx.ALL, 5 )
		
		self.label_limitfee = wx.StaticText( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_limitfee.Wrap( -1 )
		fgSizer8.Add( self.label_limitfee, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer3.Add( fgSizer8, 1, wx.EXPAND, 5 )
		
		
		fgSizer9.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		bSizer41 = wx.BoxSizer( wx.VERTICAL )
		
		self.label_totalfee = wx.StaticText( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.label_totalfee.Wrap( -1 )
		self.label_totalfee.SetFont( wx.Font( 48, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer41.Add( self.label_totalfee, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer9.Add( bSizer41, 1, wx.EXPAND, 5 )
		
		
		bSizer2.Add( fgSizer9, 1, wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_bitmap1, 0, wx.ALL, 5 )
		
		self.m_bitmap2 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_bitmap2, 0, wx.ALL, 5 )
		
		
		bSizer2.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		
		fgSizer3.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( fgSizer3 )
		self.Layout()
		self.refresh_date = wx.Timer()
		self.refresh_date.SetOwner( self, 1 )
		self.refresh_date.Start( 1000 )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.text_car_or_rfid.Bind( wx.EVT_KEY_DOWN, self.process_steps )
		self.Bind( wx.EVT_TIMER, self.refresh_datetime, id=1 )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def process_steps( self, event ):
		event.Skip()
	
	def refresh_datetime( self, event ):
		event.Skip()
	

###########################################################################
## Class PricingDialog
###########################################################################

class PricingDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Pricing - Parking Client", pos = wx.DefaultPosition, size = wx.Size( 360,216 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer10 = wx.FlexGridSizer( 1, 1, 0, 0 )
		fgSizer10.AddGrowableCol( 0 )
		fgSizer10.AddGrowableRow( 0 )
		fgSizer10.SetFlexibleDirection( wx.BOTH )
		fgSizer10.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		listbox_pricingChoices = []
		self.listbox_pricing = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listbox_pricingChoices, 0 )
		self.listbox_pricing.SetFont( wx.Font( 16, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer10.Add( self.listbox_pricing, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( fgSizer10 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.listbox_pricing.Bind( wx.EVT_KEY_DOWN, self.commit_pricing )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def commit_pricing( self, event ):
		event.Skip()
	

###########################################################################
## Class DriverDialog
###########################################################################

class DriverDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Driver", pos = wx.DefaultPosition, size = wx.Size( 400,272 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer11 = wx.FlexGridSizer( 1, 0, 0, 0 )
		fgSizer11.AddGrowableCol( 0 )
		fgSizer11.AddGrowableRow( 0 )
		fgSizer11.SetFlexibleDirection( wx.BOTH )
		fgSizer11.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		listbox_driverChoices = []
		self.listbox_driver = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listbox_driverChoices, 0 )
		fgSizer11.Add( self.listbox_driver, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( fgSizer11 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class ManlessDialog
###########################################################################

class ManlessDialog ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 683,454 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer15 = wx.FlexGridSizer( 1, 2, 0, 0 )
		fgSizer15.AddGrowableCol( 0 )
		fgSizer15.AddGrowableRow( 0 )
		fgSizer15.SetFlexibleDirection( wx.BOTH )
		fgSizer15.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer1 = wx.GridSizer( 2, 3, 0, 0 )
		
		self.imgcarfrontin = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.imgcarfrontin, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.imgcarrearin = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.imgcarrearin, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.imgdriverin = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.imgdriverin, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_bitmap10 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap10, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_bitmap11 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap11, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_bitmap12 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap12, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer7.Add( gSizer1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer15.Add( bSizer7, 1, wx.EXPAND, 5 )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer17 = wx.FlexGridSizer( 1, 1, 0, 0 )
		fgSizer17.AddGrowableCol( 0 )
		fgSizer17.AddGrowableRow( 0 )
		fgSizer17.SetFlexibleDirection( wx.BOTH )
		fgSizer17.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		lstcarChoices = []
		self.lstcar = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,-1 ), lstcarChoices, 0 )
		fgSizer17.Add( self.lstcar, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer8.Add( fgSizer17, 1, wx.EXPAND, 5 )
		
		
		fgSizer15.Add( bSizer8, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( fgSizer15 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

