import wx

from views.frames import MainFrame

app = wx.App()

main_frame = MainFrame()
main_frame.Center()

app.MainLoop()
