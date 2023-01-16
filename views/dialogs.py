import wx
from .panels import ErrorPanel, FormPanel, InfoPanel


class EmployeeForm(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Add new employee", pos=wx.DefaultPosition,
                           size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.st_status = wx.StaticText(self, wx.ID_ANY, u"Status:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_status.Wrap(-1)

        self.st_name_value = wx.StaticText(self, wx.ID_ANY, u"<value>", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_name_value.Wrap(-1)

        self.st_name = wx.StaticText(self, wx.ID_ANY, u"Full name:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_name.Wrap(-1)

        self.tc_name = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(260, -1), 0)
        self.tc_name.SetMaxLength(30)

        self.st_position = wx.StaticText(self, wx.ID_ANY, u"Position:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_position.Wrap(-1)

        ch_position_choices = [u"<null>"]
        self.ch_position = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ch_position_choices,
                                     wx.CB_SORT)
        self.ch_position.SetSelection(0)

        self.st_payment = wx.StaticText(self, wx.ID_ANY, u"Payment:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_payment.Wrap(-1)

        ch_payment_choices = [u"Piece work", u"Hourly work"]
        self.ch_payment = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ch_payment_choices, 0)
        self.ch_payment.SetSelection(0)

        self.st_rate = wx.StaticText(self, wx.ID_ANY, u"Rate:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_rate.Wrap(-1)

        self.tc_rate = wx.TextCtrl(self, wx.ID_ANY, u"0.00", wx.DefaultPosition, wx.Size(75, -1), wx.TE_RIGHT)
        self.tc_rate.SetMaxLength(7)

        self.btn_save = wx.Button(self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0)

        second_sizer = wx.FlexGridSizer(0, 2, 0, 0)
        second_sizer.SetFlexibleDirection(wx.BOTH)
        second_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        second_sizer.Add(self.st_status, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        second_sizer.Add(self.st_name_value, 0, wx.ALL, 5)
        second_sizer.Add(self.st_name, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        second_sizer.Add(self.tc_name, 0, wx.ALL, 5)
        second_sizer.Add(self.st_position, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        second_sizer.Add(self.ch_position, 0, wx.ALL, 5)
        second_sizer.Add(self.st_payment, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        second_sizer.Add(self.ch_payment, 0, wx.ALL, 5)
        second_sizer.Add(self.st_rate, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        second_sizer.Add(self.tc_rate, 0, wx.ALL, 5)

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(second_sizer, 1, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(self.btn_save, 0, wx.ALIGN_RIGHT | wx.ALL, 10)
        main_sizer.Fit(self)

        self.SetSizer(main_sizer)
        self.Layout()
        self.Centre(wx.BOTH)

    def __del__(self):
        pass


class PositionForm(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Add new position", pos=wx.DefaultPosition,
                           size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.st_position = wx.StaticText(self, wx.ID_ANY, u"Position:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_position.Wrap(-1)

        self.tc_position = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(260, -1), 0)
        self.tc_position.SetMaxLength(30)

        self.btn_save = wx.Button(self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0)

        second_sizer = wx.FlexGridSizer(0, 2, 0, 0)
        second_sizer.SetFlexibleDirection(wx.BOTH)
        second_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        second_sizer.Add(self.st_position, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        second_sizer.Add(self.tc_position, 0, wx.ALL, 5)

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(second_sizer, 1, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(self.btn_save, 0, wx.ALIGN_RIGHT | wx.ALL, 10)
        main_sizer.Fit(self)

        self.SetSizer(main_sizer)
        self.Layout()
        self.Centre(wx.BOTH)

    def __del__(self):
        pass


class ProductForm(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Add new product", pos=wx.DefaultPosition,
                           size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.st_name = wx.StaticText(self, wx.ID_ANY, u"Title:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_name.Wrap(-1)

        self.tc_name = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(260, -1), 0)
        self.tc_name.SetMaxLength(30)

        self.st_description = wx.StaticText(self, wx.ID_ANY, u"Descrioption:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_description.Wrap(-1)

        self.tc_description = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(260, 100),
                                          wx.TE_MULTILINE)

        self.st_table = wx.StaticText(self, wx.ID_ANY, u"Table", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_table.Wrap(-1)

        self.lc_table = wx.ListCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 250),
                                    wx.LC_REPORT | wx.LC_SORT_ASCENDING)

        self.btn_info = wx.Button(self, wx.ID_ANY, u"Info", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btn_add = wx.Button(self, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btn_edit = wx.Button(self, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btn_delete = wx.Button(self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btn_save = wx.Button(self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0)

        second_sizer = wx.FlexGridSizer(0, 2, 0, 0)
        second_sizer.SetFlexibleDirection(wx.BOTH)
        second_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        second_sizer.Add(self.st_name, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        second_sizer.Add(self.tc_name, 0, wx.ALL, 5)
        second_sizer.Add(self.st_description, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        second_sizer.Add(self.tc_description, 0, wx.ALL, 5)

        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        btn_sizer.Add(self.btn_info, 0, wx.ALL, 5)
        btn_sizer.Add(self.btn_add, 0, wx.ALL, 5)
        btn_sizer.Add(self.btn_edit, 0, wx.ALL, 5)
        btn_sizer.Add(self.btn_delete, 0, wx.ALL, 5)

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(second_sizer, 1, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(self.st_table, 0, wx.ALIGN_CENTER | wx.BOTTOM | wx.TOP, 10)
        main_sizer.Add(self.lc_table, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        main_sizer.Add(btn_sizer, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        main_sizer.Add(self.btn_save, 0, wx.ALIGN_RIGHT | wx.ALL, 10)
        main_sizer.Fit(self)

        self.SetSizer(main_sizer)
        self.Layout()
        self.Centre(wx.BOTH)

    def __del__(self):
        pass


class DetailForm(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Add new detail", pos=wx.DefaultPosition,
                           size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.form_panel = FormPanel(self)

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(self.form_panel, 1, wx.EXPAND | wx.ALL, 5)
        main_sizer.Fit(self)

        self.SetSizer(main_sizer)
        self.Layout()
        self.Centre(wx.BOTH)

    def __del__(self):
        pass


class OperationForm(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Add new operation", pos=wx.DefaultPosition,
                           size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.form_panel = FormPanel(self)

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(self.form_panel, 1, wx.EXPAND | wx.ALL, 5)
        main_sizer.Fit(self)

        self.SetSizer(main_sizer)
        self.Layout()
        self.Centre(wx.BOTH)

    def __del__(self):
        pass


class ProductDetailsForm(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Add new product details", pos=wx.DefaultPosition,
                           size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.st_detail = wx.StaticText(self, wx.ID_ANY, u"Detail:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_detail.Wrap(-1)

        ch_detail_choices = [u"<null>"]
        self.ch_detail = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ch_detail_choices, wx.CB_SORT)
        self.ch_detail.SetSelection(0)

        self.st_operation = wx.StaticText(self, wx.ID_ANY, u"Operation:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_operation.Wrap(-1)

        ch_operation_choices = [u"<null>"]
        self.ch_operation = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ch_operation_choices,
                                      wx.CB_SORT)
        self.ch_operation.SetSelection(0)

        self.st_cost = wx.StaticText(self, wx.ID_ANY, u"Cost:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_cost.Wrap(-1)

        self.tc_cost = wx.TextCtrl(self, wx.ID_ANY, u"0.00", wx.DefaultPosition, wx.Size(75, -1), wx.TE_RIGHT)
        self.tc_cost.SetMaxLength(7)

        self.btn_save = wx.Button(self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0)

        second_size = wx.FlexGridSizer(0, 2, 0, 0)
        second_size.SetFlexibleDirection(wx.BOTH)
        second_size.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        second_size.Add(self.st_detail, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        second_size.Add(self.ch_detail, 0, wx.ALL, 5)
        second_size.Add(self.st_operation, 0, wx.ALL, 5)
        second_size.Add(self.ch_operation, 0, wx.ALL, 5)
        second_size.Add(self.st_cost, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        second_size.Add(self.tc_cost, 0, wx.ALL, 5)

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(second_size, 1, wx.EXPAND, 5)
        main_sizer.Add(self.btn_save, 0, wx.ALIGN_RIGHT | wx.ALL, 10)
        main_sizer.Fit(self)

        self.SetSizer(main_sizer)
        self.Layout()
        self.Centre(wx.BOTH)

    def __del__(self):
        pass


class EmployeeInfo(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Employee info", pos=wx.DefaultPosition,
                           size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.st_status = wx.StaticText(self, wx.ID_ANY, u"Status:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_status.Wrap(-1)

        self.st_status_value = wx.StaticText(self, wx.ID_ANY, u"<value>", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_status_value.Wrap(-1)

        self.st_name = wx.StaticText(self, wx.ID_ANY, u"Full name:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_name.Wrap(-1)

        self.st_name_value = wx.StaticText(self, wx.ID_ANY, u"<value>", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_name_value.Wrap(-1)

        self.st_position = wx.StaticText(self, wx.ID_ANY, u"Position:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_position.Wrap(-1)

        self.st_position_value = wx.StaticText(self, wx.ID_ANY, u"<value>", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_position_value.Wrap(-1)

        self.st_payment = wx.StaticText(self, wx.ID_ANY, u"Payment:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_payment.Wrap(-1)

        self.st_payment_value = wx.StaticText(self, wx.ID_ANY, u"<value>", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_payment_value.Wrap(-1)

        self.st_rate = wx.StaticText(self, wx.ID_ANY, u"Rate:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_rate.Wrap(-1)

        self.st_rate_value = wx.StaticText(self, wx.ID_ANY, u"<value>", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_rate_value.Wrap(-1)

        self.btn_ok = wx.Button(self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0)

        second_sizer = wx.FlexGridSizer(0, 2, 0, 0)
        second_sizer.SetFlexibleDirection(wx.BOTH)
        second_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        second_sizer.Add(self.st_status, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        second_sizer.Add(self.st_status_value, 0, wx.ALL, 5)
        second_sizer.Add(self.st_name, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        second_sizer.Add(self.st_name_value, 0, wx.ALL, 5)
        second_sizer.Add(self.st_position, 0, wx.ALL, 5)
        second_sizer.Add(self.st_position_value, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        second_sizer.Add(self.st_payment, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        second_sizer.Add(self.st_payment_value, 0, wx.ALL, 5)
        second_sizer.Add(self.st_rate, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        second_sizer.Add(self.st_rate_value, 0, wx.ALL, 5)

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(second_sizer, 1, wx.EXPAND, 5)
        main_sizer.Add(self.btn_ok, 0, wx.ALIGN_RIGHT | wx.ALL, 10)
        main_sizer.Fit(self)

        self.SetSizer(main_sizer)
        self.Layout()
        self.Centre(wx.BOTH)

    def __del__(self):
        pass


class ProductInfo(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Product info", pos=wx.DefaultPosition,
                           size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.st_name = wx.StaticText(self, wx.ID_ANY, u"Title:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_name.Wrap(-1)

        self.st_name_value = wx.StaticText(self, wx.ID_ANY, u"<value>", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_name_value.Wrap(-1)

        self.st_description = wx.StaticText(self, wx.ID_ANY, u"Description:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_description.Wrap(-1)

        self.tc_description = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(260, 100),
                                          wx.TE_MULTILINE | wx.TE_READONLY)

        self.st_table = wx.StaticText(self, wx.ID_ANY, u"Table", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_table.Wrap(-1)

        self.lc_table = wx.ListCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                    wx.LC_REPORT | wx.LC_SORT_ASCENDING)
        self.lc_table.SetMinSize(wx.Size(-1, 250))

        self.btn_info = wx.Button(self, wx.ID_ANY, u"Info", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btn_ok = wx.Button(self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0)

        second_sizer = wx.FlexGridSizer(0, 2, 0, 0)
        second_sizer.SetFlexibleDirection(wx.BOTH)
        second_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        second_sizer.Add(self.st_name, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        second_sizer.Add(self.st_name_value, 0, wx.ALL, 5)
        second_sizer.Add(self.st_description, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        second_sizer.Add(self.tc_description, 0, wx.ALL, 5)

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(second_sizer, 1, wx.EXPAND, 5)
        main_sizer.Add(self.st_table, 0, wx.ALIGN_CENTER | wx.BOTTOM | wx.TOP, 10)
        main_sizer.Add(self.lc_table, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        main_sizer.Add(self.btn_info, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        main_sizer.Add(self.btn_ok, 0, wx.ALIGN_RIGHT | wx.ALL, 10)
        main_sizer.Fit(self)

        self.SetSizer(main_sizer)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


class DetailInfo(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Detail info", pos=wx.DefaultPosition,
                           size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.info_panel = InfoPanel(self)

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(self.info_panel, 1, wx.EXPAND | wx.ALL, 5)
        main_sizer.Fit(self)

        self.SetSizer(main_sizer)
        self.Layout()
        self.Centre(wx.BOTH)

    def __del__(self):
        pass


class OperationInfo(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Operation info", pos=wx.DefaultPosition,
                           size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.info_panel = InfoPanel(self)

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(self.info_panel, 1, wx.EXPAND | wx.ALL, 5)
        main_sizer.Fit(self)

        self.SetSizer(main_sizer)
        self.Layout()
        self.Centre(wx.BOTH)

    def __del__(self):
        pass


class ExceptionDialog(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Exception message", pos=wx.DefaultPosition,
                           size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.error_panel = ErrorPanel(self)

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(self.error_panel, 1, wx.EXPAND | wx.ALL, 5)
        main_sizer.Fit(self)

        self.SetSizer(main_sizer)
        self.Layout()
        self.Centre(wx.BOTH)

    def __del__(self):
        pass


class ErrorDialog(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Error message", pos=wx.DefaultPosition,
                           size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.error_panel = ErrorPanel(self)

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(self.error_panel, 1, wx.EXPAND | wx.ALL, 5)
        main_sizer.Fit(self)

        self.SetSizer(main_sizer)
        self.Layout()
        self.Centre(wx.BOTH)

    def __del__(self):
        pass