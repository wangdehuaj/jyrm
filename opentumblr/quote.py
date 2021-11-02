#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Mon May  4 00:07:38 2009

import wx
import string
try:
    from opentumblr.tumblr import Api
except ImportError:
    from tumblr import Api
# begin wxGlade: extracode
# end wxGlade



class Quote(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Quote.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, args[0], **kwds)
        self.api = args[1]
        self.panel = wx.Panel(self, -1)
        self.p_options = wx.Panel(self.panel, -1)
        self.p_quote = wx.Panel(self.panel, -1)
        self.s_options_staticbox = wx.StaticBox(self.p_options, -1, "")
        self.s_quote_staticbox = wx.StaticBox(self.p_quote, -1, "")
        self.l_addquote = wx.StaticText(self.p_quote, -1, "Add a Quote")
        self.l_quote = wx.StaticText(self.p_quote, -1, "Quote")
        self.tc_quote = wx.TextCtrl(self.p_quote, -1, "")
        self.l_source = wx.StaticText(self.p_quote, -1, "Source ( optional )")
        self.tc_source = wx.TextCtrl(self.p_quote, -1, "")
        self.b_create = wx.Button(self.p_quote, -1, "Create post")
        self.b_preview = wx.Button(self.p_quote, -1, "Preview")
        self.b_cancel = wx.Button(self.p_quote, -1, "Cancel")
        self.b_options = wx.Button(self.p_options, -1, "Advanced  options")
        self.l_publishing = wx.StaticText(self.p_options, -1, "Publishing options")
        self.cb_publishing = wx.ComboBox(self.p_options, -1, choices=["publish now", "add to queue", "publish on...", "save as draft", "private"], style=wx.CB_DROPDOWN)
        self.l_date = wx.StaticText(self.p_options, -1, "Date this post")
        self.tc_date = wx.TextCtrl(self.p_options, -1, "")
        self.l_tag = wx.StaticText(self.p_options, -1, "Tag this post")
        self.tc_tag = wx.TextCtrl(self.p_options, -1, "", style=wx.TE_MULTILINE)
        self.l_url = wx.StaticText(self.p_options, -1, "Set a custom post URL")
        self.tc_url = wx.TextCtrl(self.p_options, -1, "/post/123456/")

        self.Bind(wx.EVT_BUTTON, self.OnCreateQuote, id = self.b_create.GetId())

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Quote.__set_properties
        self.SetTitle("Add a Quote")
        self.SetBackgroundColour(wx.Colour(55, 85, 113))
        self.l_addquote.SetMinSize((-1, 80))
        self.l_addquote.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.l_addquote.SetFont(wx.Font(40, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.l_quote.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.l_quote.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.tc_quote.SetMinSize((600, 150))
        self.tc_quote.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 1, ""))
        self.l_source.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.l_source.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.tc_source.SetMinSize((600, 150))
        self.tc_source.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.p_quote.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.b_options.SetMinSize((141, 30))
        self.l_publishing.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.cb_publishing.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.cb_publishing.SetSelection(0)
        self.l_date.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.tc_date.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.l_tag.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.tc_tag.SetMinSize((201, 80))
        self.tc_tag.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.l_url.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.tc_url.SetBackgroundColour(wx.Colour(221, 221, 221))
        self.tc_url.SetForegroundColour(wx.Colour(192, 192, 192))
        self.tc_url.SetFont(wx.Font(13, wx.DECORATIVE, wx.NORMAL, wx.NORMAL, 0, "Lucida Grande"))
        self.p_options.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.panel.SetBackgroundColour(wx.Colour(55, 85, 113))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Quote.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        gs_quote = wx.FlexGridSizer(1, 2, 0, 0)
        s_options = wx.StaticBoxSizer(self.s_options_staticbox, wx.VERTICAL)
        s_quote = wx.StaticBoxSizer(self.s_quote_staticbox, wx.VERTICAL)
        s_buttons = wx.BoxSizer(wx.HORIZONTAL)
        s_quote.Add(self.l_addquote, 0, wx.ALL|wx.EXPAND, 2)
        s_quote.Add(self.l_quote, 0, wx.ALL|wx.EXPAND, 2)
        s_quote.Add(self.tc_quote, 0, wx.ALL|wx.EXPAND, 10)
        s_quote.Add(self.l_source, 0, wx.ALL|wx.EXPAND, 2)
        s_quote.Add(self.tc_source, 0, wx.ALL|wx.EXPAND, 10)
        s_buttons.Add(self.b_create, 0, wx.ALL|wx.EXPAND, 2)
        s_buttons.Add(self.b_preview, 0, wx.ALL|wx.EXPAND, 2)
        s_buttons.Add(self.b_cancel, 0, wx.LEFT|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 363)
        s_quote.Add(s_buttons, 1, wx.ALL|wx.EXPAND, 2)
        self.p_quote.SetSizer(s_quote)
        gs_quote.Add(self.p_quote, 1, wx.ALL|wx.EXPAND, 20)
        s_options.Add(self.b_options, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 30)
        s_options.Add(self.l_publishing, 0, wx.ALL|wx.EXPAND, 5)
        s_options.Add(self.cb_publishing, 0, wx.ALL|wx.EXPAND, 5)
        s_options.Add(self.l_date, 0, wx.ALL|wx.EXPAND, 5)
        s_options.Add(self.tc_date, 0, wx.ALL|wx.EXPAND, 5)
        s_options.Add(self.l_tag, 0, wx.ALL|wx.EXPAND, 5)
        s_options.Add(self.tc_tag, 0, wx.ALL|wx.EXPAND, 5)
        s_options.Add(self.l_url, 0, wx.ALL|wx.EXPAND, 5)
        s_options.Add(self.tc_url, 0, wx.ALL|wx.EXPAND, 5)
        self.p_options.SetSizer(s_options)
        gs_quote.Add(self.p_options, 1, wx.ALL|wx.EXPAND, 20)
        self.panel.SetSizer(gs_quote)
        sizer_1.Add(self.panel, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

# end of class Quote
    def OnCreateQuote(self, evt):
    	self.quote = self.tc_quote.GetValue().encode('utf-8')
    	self.source = self.tc_source.GetValue().encode('utf-8')
        self.tags = self.tc_tag.GetValue().encode('utf-8')
        self.tags = string.replace(self.tags,' ', ',')
        self.date = self.tc_date.GetValue().encode('utf-8')

        if self.cb_publishing.GetValue() == 'private':
        	self.private = 1
        else:
        	self.private = 0


        #self.format = None
        self.api = Api(self.api.name, self.api.email, self.api.password, self.private, self.date, self.tags)
    	try:
    		self.post = self.api.write_quote(self.quote, self.source)
    	except:
    		print "posteado en el blog primario"
    	self.Close()

if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    d_quote = Quote(None, -1, "")
    app.SetTopWindow(d_quote)
    d_quote.Show()
    app.MainLoop()
