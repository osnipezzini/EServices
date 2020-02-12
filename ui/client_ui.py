# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.9.0 Jan 28 2020)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview

###########################################################################
## Class ClientForm
###########################################################################

class ClientForm ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Cadastro de clientes", pos = wx.DefaultPosition, size = wx.Size( 724,447 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.AddGrowableCol( 1 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Nome", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		fgSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.text_name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.text_name, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer4.Add( fgSizer1, 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.btn_new = wx.Button( self, wx.ID_ANY, u"Novo", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.btn_new, 1, wx.ALL|wx.EXPAND, 5 )

		self.btn_save = wx.Button( self, wx.ID_ANY, u"Salvar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.btn_save, 1, wx.ALL|wx.EXPAND, 5 )

		self.btn_search = wx.Button( self, wx.ID_ANY, u"Procurar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.btn_search, 1, wx.ALL|wx.EXPAND, 5 )

		self.btn_delete = wx.Button( self, wx.ID_ANY, u"Excluir", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.btn_delete, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer6.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		self.btn_options = wx.Button( self, wx.ID_ANY, u"Opções", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.btn_options, 1, wx.ALL, 5 )


		bSizer4.Add( bSizer6, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_new.Bind( wx.EVT_BUTTON, self.new_client )
		self.btn_save.Bind( wx.EVT_BUTTON, self.save_client )
		self.btn_search.Bind( wx.EVT_BUTTON, self.search_client )
		self.btn_delete.Bind( wx.EVT_BUTTON, self.delete_client )
		self.btn_options.Bind( wx.EVT_BUTTON, self.open_options_menu )

	def __del__( self ):
		# Disconnect Events
		self.btn_new.Unbind( wx.EVT_BUTTON, None )
		self.btn_save.Unbind( wx.EVT_BUTTON, None )
		self.btn_search.Unbind( wx.EVT_BUTTON, None )
		self.btn_delete.Unbind( wx.EVT_BUTTON, None )
		self.btn_options.Unbind( wx.EVT_BUTTON, None )


	# Virtual event handlers, overide them in your derived class
	def new_client( self, event ):
		event.Skip()

	def save_client( self, event ):
		event.Skip()

	def search_client( self, event ):
		event.Skip()

	def delete_client( self, event ):
		event.Skip()

	def open_options_menu( self, event ):
		event.Skip()


###########################################################################
## Class ClientSearch
###########################################################################

class ClientSearch ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Pesquisa de clientes", pos = wx.DefaultPosition, size = wx.Size( 500,350 ), style = wx.DEFAULT_DIALOG_STYLE )

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

		self.text_search = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.text_search, 1, wx.ALL, 5 )


		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.text_search.Bind( wx.EVT_KEY_UP, self.process_keys )
		self.text_search.Bind( wx.EVT_TEXT_ENTER, self.search_client )

	def __del__( self ):
		# Disconnect Events
		self.text_search.Unbind( wx.EVT_KEY_UP, None )
		self.text_search.Unbind( wx.EVT_TEXT_ENTER, None )


	# Virtual event handlers, overide them in your derived class
	def process_keys( self, event ):
		event.Skip()

	def search_client( self, event ):
		event.Skip()


