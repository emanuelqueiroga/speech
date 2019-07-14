#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 23:46:04 2019

@author: manolo
"""
# Putting a gif image on a canvas with Tkinter
# tested with Python24 by  vegaseat  25jun2005
from tkinter import *
# create the canvas, size in pixels
canvas = Canvas(width = 300, height = 200, bg = 'yellow')
# pack the canvas into a frame/form
canvas.pack(expand = YES, fill = BOTH)
# load the .gif image file
# put in your own gif file here, may need to add full path
# like 'C:/WINDOWS/Help/Tours/WindowsMediaPlayer/Img/mplogo.gif'
gif1 = PhotoImage(file = './gif/00_loading.gif')
# put gif image on canvas
# pic's upper left corner (NW) on the canvas is at x=50 y=10
canvas.create_image(50, 10, image = gif1, anchor = NW)
# run it ...
mainloop()