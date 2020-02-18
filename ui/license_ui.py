# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.9.0 Jan 28 2020)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class LicenseUI
###########################################################################

class LicenseUI ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Licenciamento de software"), pos = wx.DefaultPosition, size = wx.Size( 485,386 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		self.img_bg = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../../../autosystem/share/images/visita_virtual.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.img_bg, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer14.Add( bSizer15, 0, wx.EXPAND, 5 )

		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, _(u"CNPJ :     "), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		self.m_staticText9.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer16.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.text_ident = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_ident.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer16.Add( self.text_ident, 1, wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, _(u"Senha : "), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		self.m_staticText10.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer16.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.text_password = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		self.text_password.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer16.Add( self.text_password, 1, wx.ALL, 5 )


		bSizer14.Add( bSizer16, 0, wx.EXPAND, 5 )

		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, _(u"Estação : "), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer17.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.text_machine = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_machine.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer17.Add( self.text_machine, 1, wx.ALL, 5 )


		bSizer14.Add( bSizer17, 0, wx.EXPAND, 5 )

		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, _(u"Serial :      "), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		self.m_staticText12.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer18.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.text_serial = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER|wx.TE_READONLY )
		self.text_serial.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer18.Add( self.text_serial, 1, wx.ALL, 5 )


		bSizer14.Add( bSizer18, 0, wx.EXPAND, 5 )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn_save = wx.Button( self, wx.ID_ANY, _(u"Registrar"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_save.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer6.Add( self.btn_save, 0, wx.ALL, 5 )


		bSizer14.Add( bSizer6, 1, wx.ALIGN_RIGHT, 5 )


		self.SetSizer( bSizer14 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_save.Bind( wx.EVT_BUTTON, self.get_license )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def get_license( self, event ):
		event.Skip()


