import wx


class MainFrame(wx.Frame):

    def __init__(self, parent=None):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.tabs = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        self.home_tab = wx.Panel(self.tabs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.employees_tab = wx.Panel(self.tabs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.products_tab = wx.Panel(self.tabs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.salary_tab = wx.Panel(self.tabs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.orders_tab = wx.Panel(self.tabs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)

        self.tabs.AddPage(self.home_tab, u"Home", True)
        self.tabs.AddPage(self.employees_tab, u"Employees", False)
        self.tabs.AddPage(self.products_tab, u"Products", False)
        self.tabs.AddPage(self.salary_tab, u"Salary", False)
        self.tabs.AddPage(self.orders_tab, u"Orders", False)

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(self.tabs, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(main_sizer)
        self.Layout()
        self.Centre(wx.BOTH)

    def __del__(self):
        pass
