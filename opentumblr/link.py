#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Mon May  4 00:02:40 2009

import wx
import string
from message import Message

try:
    from opentumblr.tumblr import Api
except ImportError:
    from tumblr import Api
# begin wxGlade: extracode
# end wxGlade



class Link(wx.Dialog):
    def __init__(self, parent, id):
        # begin wxGlade: Link.__init__
        self.parent = parent
        self.api = self.parent.api
        wx.Dialog.__init__(self, parent, id, style = wx.DEFAULT_DIALOG_STYLE)
        self.panel = wx.Panel(self, -1)
        self.p_options = wx.Panel(self.panel, -1)
        self.p_link = wx.Panel(self.panel, -1)
        self.s_options_staticbox = wx.StaticBox(self.p_options, -1, "")
        self.s_link_staticbox = wx.StaticBox(self.p_link, -1, "")
        self.l_addlink = wx.StaticText(self.p_link, -1, "Add a Link")
        self.l_name = wx.StaticText(self.p_link, -1, "Name (optional)")
        self.tc_name = wx.TextCtrl(self.p_link, -1, "")
        self.l_urllink = wx.StaticText(self.p_link, -1, "URL")
        self.tc_urllink = wx.TextCtrl(self.p_link, -1, "")
        self.l_description = wx.StaticText(self.p_link, -1, "Description (optional)")
        self.tc_description = wx.TextCtrl(self.p_link, -1, "", style=wx.TE_MULTILINE)
        self.b_create = wx.Button(self.p_link, -1, "Create post")
        
        """
        Not supported in the tumblr api at this time
        self.b_preview = wx.Button(self.p_link, -1, "Preview")
        """
        
        self.b_cancel = wx.Button(self.p_link, -1, "Cancel")
        self.b_options = wx.Button(self.p_options, -1, "Advanced  options")
        self.l_publishing = wx.StaticText(self.p_options, -1, "Publishing options")
        
        """
        Not supported in the tumblr api at this time
        self.cb_publishing = wx.ComboBox(self.p_options, -1, choices=["publish now", "add to queue", "publish on...", "save as draft", "private"], style=wx.CB_DROPDOWN)        
        """
        
        self.cb_publishing = wx.ComboBox(self.p_options, -1, choices=["publish now", "publish on...", "private"], style=wx.CB_DROPDOWN)
        self.l_date = wx.StaticText(self.p_options, -1, "Date this post")
        self.tc_date = wx.TextCtrl(self.p_options, -1, "")
        self.l_tag = wx.StaticText(self.p_options, -1, "Tag this post")
        self.tc_tag = wx.TextCtrl(self.p_options, -1, "", style=wx.TE_MULTILINE)

        """"
        Not supported in the tumlr api at this time
        self.l_url = wx.StaticText(self.p_options, -1, "Set a custom post URL")
        self.tc_url = wx.TextCtrl(self.p_options, -1, "/post/123456/")
        """

        self.Bind(wx.EVT_BUTTON, self.OnCreateLink, id = self.b_create.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnCancel, id = self.b_cancel.GetId())
        self.Bind(wx.EVT_COMBOBOX, self.GetParent().OnPublishingOptions, id = self.cb_publishing.GetId())

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Link.__set_properties
        self.SetTitle("Add a Link")
        self.SetBackgroundColour(wx.Colour(55, 85, 113))
        self.l_addlink.SetMinSize((255, 80))
        self.l_addlink.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.l_addlink.SetFont(wx.Font(50, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.l_name.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.l_name.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.tc_name.SetMinSize((600, 50))
        self.tc_name.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.tc_name.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.l_urllink.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.l_urllink.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Lucida Grande"))
        self.tc_urllink.SetMinSize((600, 50))
        self.tc_urllink.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Lucida Grande"))
        self.l_description.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.l_description.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Lucida Grande"))
        self.tc_description.SetMinSize((604, 150))
        self.tc_description.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.tc_description.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Lucida Grande"))
        self.p_link.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.b_options.SetMinSize((141, 30))
        self.l_publishing.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.cb_publishing.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.cb_publishing.SetSelection(0)
        self.l_date.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.tc_date.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.l_tag.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.tc_tag.SetMinSize((201, 80))
        self.tc_tag.SetBackgroundColour(wx.Colour(255, 255, 255))
        #self.l_url.SetBackgroundColour(wx.Colour(255, 255, 255))
        #self.tc_url.SetBackgroundColour(wx.Colour(221, 221, 221))
        #self.tc_url.SetForegroundColour(wx.Colour(192, 192, 192))
        #self.tc_url.SetFont(wx.Font(13, wx.DECORATIVE, wx.NORMAL, wx.NORMAL, 0, "Lucida Grande"))
        self.p_options.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.panel.SetBackgroundColour(wx.Colour(55, 85, 113))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Link.__do_layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        gs_link = wx.FlexGridSizer(1, 2, 0, 0)
        s_options = wx.StaticBoxSizer(self.s_options_staticbox, wx.VERTICAL)
        s_link = wx.StaticBoxSizer(self.s_link_staticbox, wx.VERTICAL)
        s_buttons = wx.BoxSizer(wx.HORIZONTAL)
        s_link.Add(self.l_addlink, 0, wx.ALL|wx.EXPAND, 2)
        s_link.Add(self.l_name, 0, wx.ALL|wx.EXPAND, 2)
        s_link.Add(self.tc_name, 0, wx.ALL|wx.EXPAND, 2)
        s_link.Add(self.l_urllink, 0, wx.ALL|wx.EXPAND, 2)
        s_link.Add(self.tc_urllink, 0, wx.ALL|wx.EXPAND, 2)
        s_link.Add(self.l_description, 0, wx.ALL|wx.EXPAND, 2)
        s_link.Add(self.tc_description, 0, wx.ALL|wx.EXPAND, 2)
        s_buttons.Add(self.b_create, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 2)
        #s_buttons.Add(self.b_preview, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2)
        s_buttons.Add(self.b_cancel, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 345)
        s_link.Add(s_buttons, 1, wx.EXPAND, 0)
        self.p_link.SetSizer(s_link)
        gs_link.Add(self.p_link, 1, wx.ALL|wx.EXPAND, 20)
        s_options.Add(self.b_options, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 30)
        s_options.Add(self.l_publishing, 0, wx.ALL|wx.EXPAND, 5)
        s_options.Add(self.cb_publishing, 0, wx.ALL|wx.EXPAND, 5)
        s_options.Add(self.l_date, 0, wx.ALL|wx.EXPAND, 5)
        s_options.Add(self.tc_date, 0, wx.ALL|wx.EXPAND, 5)
        s_options.Add(self.l_tag, 0, wx.ALL|wx.EXPAND, 5)
        s_options.Add(self.tc_tag, 0, wx.ALL|wx.EXPAND, 5)
        #s_options.Add(self.l_url, 0, wx.ALL|wx.EXPAND, 5)
        #s_options.Add(self.tc_url, 0, wx.ALL|wx.EXPAND, 5)
        self.p_options.SetSizer(s_options)
        gs_link.Add(self.p_options, 1, wx.ALL|wx.EXPAND, 20)
        self.panel.SetSizer(gs_link)
        sizer.Add(self.panel, 1, wx.EXPAND, 0)
        self.SetSizer(sizer)
        sizer.Fit(self)
        self.Layout()
        # end wxGlade

# end of class Link
    def OnCreateLink(self, evt):
    	self.name = self.tc_name.GetValue().encode('utf-8')
    	self.urllink = self.tc_urllink.GetValue()
    	self.description = self.tc_description.GetValue().encode('utf-8')
        self.tags = self.tc_tag.GetValue().encode('utf-8')
        self.tags = string.replace(self.tags,' ', ',')
        self.date = self.tc_date.GetValue().encode('utf-8')

        if self.cb_publishing.GetValue() == 'private':
        	self.private = 1
        else:
        	self.private = 0
        
        if self.urllink:
            #self.format = None
            self.api = Api(self.api.name, self.api.email, self.api.password, self.private, self.date, self.tags)
            try:
                self.post = self.api.write_link(self.name,self.urllink,self.description)
            except:
                print "posteado en el blog primario"
            self.Close()
        else:
            Message('URL is required')
    def OnCancel(self, evt):
	    self.Close()

if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    d_link = Link(None, -1, "")
    app.SetTopWindow(d_link)
    d_link.Show()
    app.MainLoop()
