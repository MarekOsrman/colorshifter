import wx

class MainWindow(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title, size=(400,200))
		
		self.CreateStatusBar()
		
		filemenu = wx.Menu()
		menuAbout = filemenu.Append(wx.ID_ABOUT, "&About", "Info")
		filemenu.AppendSeparator()
		menuExit = filemenu.Append(wx.ID_EXIT, "E&xit", "Terminate")
		
		menuBar = wx.MenuBar()
		menuBar.Append(filemenu, "&File")
		self.SetMenuBar(menuBar)
		
		self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
		self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
		
		self.Show(True)
	
	def OnAbout(self, event):
		dlg = wx.MessageDialog(self, "Hello App", "About Hello App", wx.OK)
		dlg.ShowModal()
		dlg.Destroy()
		
	def OnExit(self, event):
		self.Close(True)



print("Starting NOW!")

app = wx.App(False)
frame = MainWindow(None, "Hello World!")
app.MainLoop()
