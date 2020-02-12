# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.9.0 Jan 28 2020)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainUi
###########################################################################

class MainUi ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"EServices", pos = wx.DefaultPosition, size = wx.Size( 752,379 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu2 = wx.Menu()
		self.menu_bill_control = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Manutenção de contas", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.menu_bill_control )

		self.menu_bill_receive = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Contas a receber", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.menu_bill_receive )

		self.menu_bill_pay = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Contas a pagar", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.menu_bill_pay )

		self.m_menubar1.Append( self.m_menu2, u"Financeiro" )

		self.m_menu3 = wx.Menu()
		self.m_menubar1.Append( self.m_menu3, u"Relatórios" )

		self.m_menu4 = wx.Menu()
		self.m_menubar1.Append( self.m_menu4, u"Consultas" )

		self.m_menu41 = wx.Menu()
		self.menu_client = wx.MenuItem( self.m_menu41, wx.ID_ANY, u"Clientes", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu41.Append( self.menu_client )

		self.m_menubar1.Append( self.m_menu41, u"Cadastros" )

		self.SetMenuBar( self.m_menubar1 )

		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.open_client, id = self.menu_client.GetId() )

	def __del__( self ):
		# Disconnect Events
		self.Unbind( wx.EVT_MENU, id = self.menu_client.GetId() )


	# Virtual event handlers, overide them in your derived class
	def open_client( self, event ):
		event.Skip()


