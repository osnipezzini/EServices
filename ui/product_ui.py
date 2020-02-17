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
## Class ProductForm
###########################################################################

class ProductForm ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Cadastro de produtos", pos = wx.DefaultPosition, size = wx.Size( 724,447 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		bSizer61 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Código", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		bSizer61.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.text_code = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer61.Add( self.text_code, 0, wx.ALL, 5 )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Codigo de barras", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer61.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.text_barcode = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer61.Add( self.text_barcode, 1, wx.ALL, 5 )

		self.check_active = wx.CheckBox( self, wx.ID_ANY, u"Ativo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.check_active.SetValue(True)
		bSizer61.Add( self.check_active, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer8.Add( bSizer61, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Nome", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer13.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.text_name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.text_name, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer8.Add( bSizer13, 0, wx.EXPAND, 5 )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer8.Add( bSizer9, 0, wx.EXPAND, 5 )

		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer8.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )

		fgSizer1 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer1.AddGrowableCol( 2 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Grupo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		fgSizer1.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.text_group_grid = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		fgSizer1.Add( self.text_group_grid, 0, wx.ALL, 5 )

		self.text_group_name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer1.Add( self.text_group_name, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"SubGrupo : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		fgSizer1.Add( self.m_staticText14, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.text_subgroup_code = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.text_subgroup_code, 0, wx.ALL, 5 )

		self.text_subgroup_name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer1.Add( self.text_subgroup_name, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Marca : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		fgSizer1.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.text_brand_code = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.text_brand_code, 0, wx.ALL, 5 )

		self.text_brand_name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer1.Add( self.text_brand_name, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Fornecedor : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		fgSizer1.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.text_provider_code = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.text_provider_code, 0, wx.ALL, 5 )

		self.text_provider_name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer1.Add( self.text_provider_name, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer8.Add( fgSizer1, 1, wx.EXPAND, 5 )


		bSizer7.Add( bSizer8, 1, wx.EXPAND, 5 )


		bSizer4.Add( bSizer7, 1, wx.EXPAND, 5 )

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
		self.text_group_grid.Bind( wx.EVT_TEXT_ENTER, self.search_group )
		self.btn_new.Bind( wx.EVT_BUTTON, self.new_product )
		self.btn_save.Bind( wx.EVT_BUTTON, self.save_product )
		self.btn_search.Bind( wx.EVT_BUTTON, self.search_product )
		self.btn_delete.Bind( wx.EVT_BUTTON, self.delete_product )
		self.btn_options.Bind( wx.EVT_BUTTON, self.open_options_menu )

	def __del__( self ):
		# Disconnect Events
		self.text_group_grid.Unbind( wx.EVT_TEXT_ENTER, None )
		self.btn_new.Unbind( wx.EVT_BUTTON, None )
		self.btn_save.Unbind( wx.EVT_BUTTON, None )
		self.btn_search.Unbind( wx.EVT_BUTTON, None )
		self.btn_delete.Unbind( wx.EVT_BUTTON, None )
		self.btn_options.Unbind( wx.EVT_BUTTON, None )


	# Virtual event handlers, overide them in your derived class
	def search_group( self, event ):
		event.Skip()

	def new_product( self, event ):
		event.Skip()

	def save_product( self, event ):
		event.Skip()

	def search_product( self, event ):
		event.Skip()

	def delete_product( self, event ):
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
		self.text_search.Bind( wx.EVT_TEXT_ENTER, self.search_client )
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

	def search_client( self, event ):
		event.Skip()

	def open_options( self, event ):
		event.Skip()


###########################################################################
## Class SearchOptions
###########################################################################

class SearchOptions ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Opções de pesquisa", pos = wx.DefaultPosition, size = wx.Size( 321,156 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		self.check_inactived = wx.CheckBox( self, wx.ID_ANY, u"Inativos", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.check_inactived.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer14.Add( self.check_inactived, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )

		self.check_deleted = wx.CheckBox( self, wx.ID_ANY, u"Deletados", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.check_deleted.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer14.Add( self.check_deleted, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		bSizer15.Add( bSizer14, 1, wx.EXPAND, 5 )

		self.btn_save = wx.Button( self, wx.ID_ANY, u"Salvar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_save.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer15.Add( self.btn_save, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer15 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_save.Bind( wx.EVT_BUTTON, self.save_options )

	def __del__( self ):
		# Disconnect Events
		self.btn_save.Unbind( wx.EVT_BUTTON, None )


	# Virtual event handlers, overide them in your derived class
	def save_options( self, event ):
		event.Skip()


###########################################################################
## Class PersonGroupForm
###########################################################################

class PersonGroupForm ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Cadastro de Tipos de pessoas", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		bSizer61 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Código", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		bSizer61.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.text_code = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer61.Add( self.text_code, 0, wx.ALL, 5 )

		self.check_active = wx.CheckBox( self, wx.ID_ANY, u"Ativo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.check_active.SetValue(True)
		bSizer61.Add( self.check_active, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer8.Add( bSizer61, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Nome", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer13.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.text_name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.text_name, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer8.Add( bSizer13, 0, wx.EXPAND, 5 )

		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer8.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )


		bSizer7.Add( bSizer8, 1, wx.EXPAND, 5 )


		bSizer4.Add( bSizer7, 1, wx.EXPAND, 5 )

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
		self.btn_new.Bind( wx.EVT_BUTTON, self.new_act )
		self.btn_save.Bind( wx.EVT_BUTTON, self.save_act )
		self.btn_search.Bind( wx.EVT_BUTTON, self.search_act )
		self.btn_delete.Bind( wx.EVT_BUTTON, self.delete_act )
		self.btn_options.Bind( wx.EVT_BUTTON, self.open_options_menu )

	def __del__( self ):
		# Disconnect Events
		self.btn_new.Unbind( wx.EVT_BUTTON, None )
		self.btn_save.Unbind( wx.EVT_BUTTON, None )
		self.btn_search.Unbind( wx.EVT_BUTTON, None )
		self.btn_delete.Unbind( wx.EVT_BUTTON, None )
		self.btn_options.Unbind( wx.EVT_BUTTON, None )


	# Virtual event handlers, overide them in your derived class
	def new_act( self, event ):
		event.Skip()

	def save_act( self, event ):
		event.Skip()

	def search_act( self, event ):
		event.Skip()

	def delete_act( self, event ):
		event.Skip()

	def open_options_menu( self, event ):
		event.Skip()


