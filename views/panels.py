import wx


class HomeTab(wx.Panel):

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(500, 300), style=wx.TAB_TRAVERSAL,
                 name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)

    def __del__(self):
        pass


class EmployeesTab(wx.Panel):

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(-1, -1), style=wx.TAB_TRAVERSAL,
                 name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)

        self.lc_employees = wx.ListCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 250),
                                        wx.LC_REPORT | wx.LC_SORT_ASCENDING)
        self.lc_position = wx.ListCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 250),
                                       wx.LC_REPORT | wx.LC_SORT_ASCENDING)

        self.btn_info = wx.Button(self, wx.ID_ANY, u"Info", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btn_add = wx.Button(self, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btn_edit = wx.Button(self, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btn_delete = wx.Button(self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0)

        table_sizer = wx.BoxSizer(wx.HORIZONTAL)
        table_sizer.Add(self.lc_employees, 0, wx.ALL, 5)
        table_sizer.Add(self.lc_position, 0, wx.ALL, 5)

        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        btn_sizer.Add(self.btn_info, 0, wx.ALL, 5)
        btn_sizer.Add(self.btn_add, 0, wx.ALL, 5)
        btn_sizer.Add(self.btn_edit, 0, wx.ALL, 5)
        btn_sizer.Add(self.btn_delete, 0, wx.ALL, 5)

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(table_sizer, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        main_sizer.Add(btn_sizer, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        main_sizer.Fit(self)

        self.SetSizer(main_sizer)
        self.Layout()

    def __del__(self):
        pass


class ProductsTab(wx.Panel):

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(-1, -1), style=wx.TAB_TRAVERSAL,
                 name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)

        self.lc_products = wx.ListCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 250),
                                       wx.LC_REPORT | wx.LC_SORT_ASCENDING)

        self.lc_details = wx.ListCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 250),
                                      wx.LC_REPORT | wx.LC_SORT_ASCENDING)

        self.lc_operations = wx.ListCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 250),
                                         wx.LC_REPORT | wx.LC_SORT_ASCENDING)

        self.btn_info = wx.Button(self, wx.ID_ANY, u"Info", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btn_add = wx.Button(self, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btn_edit = wx.Button(self, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btn_delete = wx.Button(self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0)
        table_sizer = wx.BoxSizer(wx.HORIZONTAL)
        table_sizer.Add(self.lc_products, 0, wx.ALL, 5)
        table_sizer.Add(self.lc_details, 0, wx.ALL, 5)
        table_sizer.Add(self.lc_operations, 0, wx.ALL, 5)

        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        btn_sizer.Add(self.btn_info, 0, wx.ALL, 5)
        btn_sizer.Add(self.btn_add, 0, wx.ALL, 5)
        btn_sizer.Add(self.btn_edit, 0, wx.ALL, 5)
        btn_sizer.Add(self.btn_delete, 0, wx.ALL, 5)

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(table_sizer, 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(btn_sizer, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        main_sizer.Fit(self)

        self.SetSizer(main_sizer)
        self.Layout()

    def __del__(self):
        pass


class SalaryTab(wx.Panel):

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(500, 300), style=wx.TAB_TRAVERSAL,
                 name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)

    def __del__(self):
        pass


class OrdersTab(wx.Panel):

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(500, 300), style=wx.TAB_TRAVERSAL,
                 name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)

    def __del__(self):
        pass


class Form(wx.Panel):

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(-1, -1), style=wx.TAB_TRAVERSAL,
                 name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)

        self.st_name = wx.StaticText(self, wx.ID_ANY, u"Title:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_name.Wrap(-1)

        self.tc_name = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(260, -1), 0)
        self.tc_name.SetMaxLength(30)

        self.st_description = wx.StaticText(self, wx.ID_ANY, u"Description:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_description.Wrap(-1)

        self.tc_description = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(260, 100),
                                          wx.TE_MULTILINE)

        self.btn_save = wx.Button(self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0)

        second_sizer = wx.FlexGridSizer(0, 2, 0, 0)
        second_sizer.SetFlexibleDirection(wx.BOTH)
        second_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        second_sizer.Add(self.st_name, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        second_sizer.Add(self.tc_name, 0, wx.ALL, 5)
        second_sizer.Add(self.st_description, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        second_sizer.Add(self.tc_description, 0, wx.ALL, 5)

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(second_sizer, 1, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(self.btn_save, 0, wx.ALIGN_RIGHT | wx.ALL, 10)
        main_sizer.Fit(self)

        self.SetSizer(main_sizer)
        self.Layout()

    def __del__(self):
        pass


class Info(wx.Panel):

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(-1, -1), style=wx.TAB_TRAVERSAL,
                 name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)

        self.st_name = wx.StaticText(self, wx.ID_ANY, u"Title:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_name.Wrap(-1)

        self.st_name_value = wx.StaticText(self, wx.ID_ANY, u"<value>", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_name_value.Wrap(-1)

        self.st_description = wx.StaticText(self, wx.ID_ANY, u"Description:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_description.Wrap(-1)

        self.tc_description = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(260, 100),
                                          wx.TE_MULTILINE | wx.TE_READONLY)

        self.btn_ok = wx.Button(self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0)

        second_sizer = wx.FlexGridSizer(0, 2, 0, 0)
        second_sizer.SetFlexibleDirection(wx.BOTH)
        second_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        second_sizer.Add(self.st_name, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        second_sizer.Add(self.st_name_value, 0, wx.ALL, 5)
        second_sizer.Add(self.st_description, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        second_sizer.Add(self.tc_description, 0, wx.ALL, 5)

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(second_sizer, 1, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(self.btn_ok, 0, wx.ALIGN_RIGHT | wx.ALL, 10)
        main_sizer.Fit(self)

        self.SetSizer(main_sizer)
        self.Layout()

    def __del__(self):
        pass


class Error(wx.Panel):

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(-1, -1), style=wx.TAB_TRAVERSAL,
                 name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)

        self.tc_exception = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(260, 100),
                                        wx.TE_MULTILINE | wx.TE_READONLY)

        self.btn_ok = wx.Button(self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0)

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(self.tc_exception, 0, wx.ALL, 5)
        main_sizer.Add(self.btn_ok, 0, wx.ALIGN_RIGHT | wx.ALL, 10)
        main_sizer.Fit(self)

        self.SetSizer(main_sizer)
        self.Layout()

    def __del__(self):
        pass
