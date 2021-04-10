#!/usr/bin/env python
# -*- coding: us-ascii -*-
# generated by wxGlade 0.6.3 on Mon Mar  9 13:53:58 2009

import wx

# begin wxGlade: extracode
# end wxGlade



class Dashboard(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Dashboard.__init__
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.bmap_text = wx.BitmapButton(self, -1, wx.Bitmap("/home/jyr/opentumblr/opentumblr/images/text.png", wx.BITMAP_TYPE_ANY))
        self.bmap_photo = wx.BitmapButton(self, -1, wx.Bitmap("/home/jyr/opentumblr/opentumblr/images/photo.png", wx.BITMAP_TYPE_ANY))
        self.bmap_quote = wx.BitmapButton(self, -1, wx.Bitmap("/home/jyr/opentumblr/opentumblr/images/quote.png", wx.BITMAP_TYPE_ANY))
        self.bmap_link = wx.BitmapButton(self, -1, wx.Bitmap("/home/jyr/opentumblr/opentumblr/images/link.png", wx.BITMAP_TYPE_ANY))
        self.bmap_chat = wx.BitmapButton(self, -1, wx.Bitmap("/home/jyr/opentumblr/opentumblr/images/chat.png", wx.BITMAP_TYPE_ANY))
        self.bmap_audio = wx.BitmapButton(self, -1, wx.Bitmap("/home/jyr/opentumblr/opentumblr/images/audio.png", wx.BITMAP_TYPE_ANY))
        self.bmap_video = wx.BitmapButton(self, -1, wx.Bitmap("/home/jyr/opentumblr/opentumblr/images/video.png", wx.BITMAP_TYPE_ANY))
        self.bmap_config = wx.BitmapButton(self, -1, wx.Bitmap("/home/jyr/opentumblr/opentumblr/images/text.png", wx.BITMAP_TYPE_ANY))
        self.bmap_exit = wx.BitmapButton(self, -1, wx.Bitmap("/home/jyr/opentumblr/opentumblr/images/text.png", wx.BITMAP_TYPE_ANY))

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Dashboard.__set_properties
        self.SetBackgroundColour(wx.Colour(44, 71, 98))
        self.bmap_text.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.bmap_text.SetSize(self.bmap_text.GetBestSize())
        self.bmap_photo.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.bmap_photo.SetSize(self.bmap_photo.GetBestSize())
        self.bmap_quote.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.bmap_quote.SetSize(self.bmap_quote.GetBestSize())
        self.bmap_link.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.bmap_link.SetSize(self.bmap_link.GetBestSize())
        self.bmap_chat.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.bmap_chat.SetSize(self.bmap_chat.GetBestSize())
        self.bmap_audio.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.bmap_audio.SetSize(self.bmap_audio.GetBestSize())
        self.bmap_video.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.bmap_video.SetSize(self.bmap_video.GetBestSize())
        self.bmap_config.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.bmap_config.SetSize(self.bmap_config.GetBestSize())
        self.bmap_exit.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.bmap_exit.SetSize(self.bmap_exit.GetBestSize())
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Dashboard.__do_layout
        grid_sizer_dashboard = wx.GridSizer(3, 3, 0, 0)
        grid_sizer_dashboard.Add(self.bmap_text, 0, wx.ALL, 5)
        grid_sizer_dashboard.Add(self.bmap_photo, 0, wx.ALL, 5)
        grid_sizer_dashboard.Add(self.bmap_quote, 0, wx.ALL, 5)
        grid_sizer_dashboard.Add(self.bmap_link, 0, wx.ALL, 5)
        grid_sizer_dashboard.Add(self.bmap_chat, 0, wx.ALL, 5)
        grid_sizer_dashboard.Add(self.bmap_audio, 0, wx.ALL, 5)
        grid_sizer_dashboard.Add(self.bmap_video, 0, wx.ALL, 5)
        grid_sizer_dashboard.Add(self.bmap_config, 0, wx.ALL, 5)
        grid_sizer_dashboard.Add(self.bmap_exit, 0, wx.ALL, 5)
        self.SetSizer(grid_sizer_dashboard)
        grid_sizer_dashboard.Fit(self)
        # end wxGlade

# end of class Dashboard

