#!/usr/bin/python

import wx

class MainWindow(wx.Frame):
	def __init__(self, parent, title):
		super(MainWindow, self).__init__(parent, title=title,
				size=(1600, 800))
		
		self.init_menu()
		
		self.Bind(wx.EVT_PAINT, self.OnPaint)
		
		self.Centre()
		self.Show()
	
	def init_menu(self):
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
	
	def OnAbout(self, event):
		dlg = wx.MessageDialog(self, "Hello App", "About Hello App", wx.OK)
		dlg.ShowModal()
		dlg.Destroy()
		
	def OnExit(self, event):
		self.Close(True)
	
	def OnPaint(self, event):
		dc = wx.PaintDC(self)
		
		dc.SetPen(wx.Pen(wx.Colour(0,0,0), 0, wx.TRANSPARENT))
		
		for gray in range(0,256):
			dc.SetBrush(wx.Brush(wx.Colour(gray,gray,gray)))
			dc.DrawRectangle(gray*6, 0, 6, 800)
		
		for red in range(0,256):
			dc.SetBrush(wx.Brush(wx.Colour(red,0,0)))
			dc.DrawRectangle(100 + red*3, 20, 3, 50)
		for green in range(0,256):
			dc.SetBrush(wx.Brush(wx.Colour(0,green,0)))
			dc.DrawRectangle(100 + green*3, 80, 3, 50)
		for blue in range(0,256):
			dc.SetBrush(wx.Brush(wx.Colour(0,0,blue)))
			dc.DrawRectangle(100 + blue*3, 140, 3, 50)
		
		offx = 400
		offy = 400
		
		for green in range(0,128):
			for blue in range(0,128):
				dc.SetPen(wx.Pen(wx.Colour(255, 255 - 2*green, 2*blue)))
				dc.DrawPoint(offx + blue, offy + green)
		
		for red in range(0,128):
			for blue in range(0,128):
				dc.SetPen(wx.Pen(wx.Colour(2*red, 255, 2*blue)))
				dc.DrawPoint(offx + blue + red/2, offy - red/2)
		
		
		#dc.DrawLine(0, 0, 190, 60)


if __name__ == '__main__':
	app = wx.App()
	MainWindow(None, "Hello World!")
	app.MainLoop()
