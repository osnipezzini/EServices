# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.9.0 Jan 28 2020)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.dataview
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

		self.menu_product = wx.MenuItem( self.m_menu41, wx.ID_ANY, u"Produtos", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu41.Append( self.menu_product )

		self.m_menubar1.Append( self.m_menu41, u"Cadastros" )

		self.SetMenuBar( self.m_menubar1 )

        self.status_bar = self.CreateStatusBar(3, wx.STB_DEFAULT_STYLE | wx.STB_SIZEGRIP, wx.ID_ANY)

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.open_client, id = self.menu_client.GetId() )
		self.Bind( wx.EVT_MENU, self.open_product, id = self.menu_product.GetId() )

	def __del__( self ):
		# Disconnect Events
		self.Unbind( wx.EVT_MENU, id = self.menu_client.GetId() )
		self.Unbind( wx.EVT_MENU, id = self.menu_product.GetId() )


	# Virtual event handlers, overide them in your derived class
	def open_client( self, event ):
		event.Skip()

	def open_product( self, event ):
		event.Skip()


###########################################################################
## Class Search
###########################################################################

class Search ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Pesquisa", pos = wx.DefaultPosition, size = wx.Size( 500,350 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.Size( 500,350 ), wx.Size( 640,480 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.data_search = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.data_search, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		choice_search_typeChoices = [ u"Nome", u"CPF/CNPJ" ]
		self.choice_search_type = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_search_typeChoices, 0 )
		self.choice_search_type.SetSelection( 0 )
		bSizer2.Add( self.choice_search_type, 0, wx.ALL, 5 )

		self.text_search = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		bSizer2.Add( self.text_search, 1, wx.ALL, 5 )

		self.btn_options = wx.Button( self, wx.ID_ANY, u"Opções", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.btn_options, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.data_search.Bind( wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.load_client, id = wx.ID_ANY )
		self.text_search.Bind( wx.EVT_KEY_DOWN, self.process_keys )
		self.text_search.Bind( wx.EVT_TEXT_ENTER, self.search )
		self.btn_options.Bind( wx.EVT_BUTTON, self.open_options )

	def __del__( self ):
		# Disconnect Events
		self.data_search.Unbind( wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, None, id = wx.ID_ANY )
		self.text_search.Unbind( wx.EVT_KEY_DOWN, None )
		self.text_search.Unbind( wx.EVT_TEXT_ENTER, None )
		self.btn_options.Unbind( wx.EVT_BUTTON, None )


	# Virtual event handlers, overide them in your derived class
	def load_client( self, event ):
		event.Skip()

	def process_keys( self, event ):
		event.Skip()

	def search( self, event ):
		event.Skip()

	def open_options( self, event ):
		event.Skip()


