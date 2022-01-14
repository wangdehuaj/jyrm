#!/usr/bin/env python
# -*- coding: us-ascii -*-
# generated by wxGlade 0.6.3 on Fri Aug 14 15:59:40 2009

import wx
import os,sys
from tumblelog import TumbleLog
# begin wxGlade: extracode
# end wxGlade

ID_TEXT = wx.NewId()
ID_PHOTO = wx.NewId()
ID_QUOTE = wx.NewId()
ID_LINK = wx.NewId()
ID_CHAT = wx.NewId()
ID_AUDIO = wx.NewId()
ID_VIDEO = wx.NewId()


class Dashboard(wx.Frame):
    def __init__(self, parent, id, api):
        # begin wxGlade: Dashboard.__init__
        #kwds["style"] = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.MAXIMIZE_BOX|wx.SYSTEM_MENU|wx.RESIZE_BORDER|wx.FULL_REPAINT_ON_RESIZE|wx.CLIP_CHILDREN
        wx.Frame.__init__(self, parent, id)
        self.parent = parent
        self.api = api
        
        # Tool Bar
        self.toolbar_dashboard = ToolBarDashboard(self, -1)
        self.SetToolBar(self.toolbar_dashboard)
        # Tool Bar end
        self.panel = TumbleLog(self, -1)
        self.b_twitter = wx.Button(self, -1, "Twitter")
        self.b_filesocial = wx.Button(self, -1, "FileSocial")
        self.b_logout = wx.Button(self, -1, "Logout")
        
        self.Bind(wx.EVT_TOOL, self.SelectPanel, id = ID_TEXT)
        self.Bind(wx.EVT_TOOL, self.SelectPanel, id = ID_PHOTO)
        self.Bind(wx.EVT_TOOL, self.SelectPanel, id = ID_QUOTE)
        self.Bind(wx.EVT_TOOL, self.SelectPanel, id = ID_LINK)
        self.Bind(wx.EVT_TOOL, self.SelectPanel, id = ID_CHAT)
        self.Bind(wx.EVT_TOOL, self.SelectPanel, id = ID_AUDIO)
        self.Bind(wx.EVT_TOOL, self.SelectPanel, id = ID_VIDEO)
        self.Bind(wx.EVT_BUTTON, self.OnLogout, id = self.b_logout.GetId())

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Dashboard.__set_properties
        self.SetTitle("Opentumblr")
        self.SetSize((290, 570))
        #self.toolbar_dashboard.SetToolBitmapSize((26, 25))
        #self.toolbar_dashboard.SetToolPacking(1)
        #self.toolbar_dashboard.Realize()
        self.panel.SetMinSize((290, 570))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Dashboard.__do_layout
        s_dashboard = wx.BoxSizer(wx.VERTICAL)
        s_buttons = wx.BoxSizer(wx.VERTICAL)
        s_buttonsocials = wx.BoxSizer(wx.HORIZONTAL)
        s_dashboard.Add(self.panel, 1, wx.EXPAND, 0)
        s_buttonsocials.Add(self.b_twitter, 1, wx.ALL|wx.EXPAND, 5)
        s_buttonsocials.Add(self.b_filesocial, 1, wx.ALL|wx.EXPAND, 5)
        s_buttons.Add(s_buttonsocials, 1, wx.EXPAND, 0)
        s_buttons.Add(self.b_logout, 0, wx.EXPAND, 0)
        s_buttons.Add((20, 20), 0, 0, 0)
        s_dashboard.Add(s_buttons, 0, wx.EXPAND, 0)
        self.SetSizer(s_dashboard)
        self.Layout()
        # end wxGlade
        
    def SelectPanel(self, evt):
        evt_id = evt.GetId()
        if evt_id == ID_TEXT:
            self.panel.SetPanel("TEXT")
        elif evt_id == ID_PHOTO:
            self.panel.SetPanel("PHOTO")
        elif evt_id == ID_QUOTE:
            self.panel.SetPanel("QUOTE")
        elif evt_id == ID_LINK:
            self.panel.SetPanel("LINK")
        elif evt_id == ID_CHAT:
            self.panel.SetPanel("CHAT")
        elif evt_id == ID_AUDIO:
            self.panel.SetPanel("AUDIO")
        elif evt_id == ID_VIDEO:
            self.panel.SetPanel("VIDEO")
        else:
            evt.Skip()

# end of class Dashboard
    def OnLogout(self, evt):
    	self.Close()


class ToolBarDashboard(wx.ToolBar):
    def __init__(self, parent, id):
        # begin wxGlade: ToolBarDashboard.__init__
        #kwds["style"] = wx.TB_TEXT
        wx.ToolBar.__init__(self, parent, id, style=wx.TB_HORIZONTAL|wx.TB_TEXT)
        self.path_images = '/usr/share/pixmaps/opentumblr/dashboard/'
        
        if not os.path.isdir(self.path_images):
            if sys.platform == "win32":
                self.path_images = os.path.abspath(os.path.dirname(__file__)) + '\\..\\images\\'
            else:
                self.path_images = os.path.abspath('images') + '/'

        self.AddSeparator()
        self.AddLabelTool(ID_TEXT, "Text", wx.Bitmap(self.path_images + "text.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "", "")
        self.AddLabelTool(ID_PHOTO, "Photo", wx.Bitmap(self.path_images + "photo.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "", "")
        self.AddLabelTool(ID_QUOTE, "Quote", wx.Bitmap(self.path_images + "quote.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "", "")
        self.AddLabelTool(ID_LINK, "Link", wx.Bitmap(self.path_images + "link.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "", "")
        self.AddLabelTool(ID_CHAT, "Chat", wx.Bitmap(self.path_images + "chat.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "", "")
        self.AddLabelTool(ID_AUDIO, "Audio", wx.Bitmap(self.path_images + "audio.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "", "")
        self.AddLabelTool(ID_VIDEO, "Video", wx.Bitmap(self.path_images + "video.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "", "")
        self.AddSeparator()

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: ToolBarDashboard.__set_properties
        self.SetToolBitmapSize((16, 15))
        self.SetToolPacking(1)
        self.Realize()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: ToolBarDashboard.__do_layout
        pass
        # end wxGlade

# end of class ToolBarDashboard


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    f_dashboard = Dashboard(None, -1)
    app.SetTopWindow(f_dashboard)
    f_dashboard.Show()
    app.MainLoop()
