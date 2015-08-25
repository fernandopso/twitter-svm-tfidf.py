#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
#Libraries for Interface Grafics
import gtk, gobject, glib
import pygtk
pygtk.require('2.0')

class Alert(gtk.Window):
    def __init__(self):
        super(Alert,self).__init__()
        self.set_title("Aviso")
        self.set_size_request(300, 100)
        self.set_position(gtk.WIN_POS_CENTER)

        fixed = gtk.Fixed()

        # create the image and associate the pixbuf
        path = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(path, "images/alert.png")
        pixbuf = gtk.gdk.pixbuf_new_from_file_at_size(icon_path , 24, 24)
        self.image = gtk.Image()
        self.image.set_from_pixbuf(pixbuf)
        fixed.put(self.image, 30, 15)

        #Label to alert user.
        self.labelAlert = gtk.Label("Nenhum arquivo selecionado!")
        fixed.put(self.labelAlert, 60, 20)

        #Button to exit the window 'Treinar Dados'.
        self.bt_exit = gtk.Button("Ok")
        self.bt_exit.connect("clicked", self.on_clickedExit)
        self.bt_exit.set_size_request(60, 30)
        fixed.put(self.bt_exit, 125, 50)

        self.add(fixed)
        self.show_all()

    def on_clickedExit(self, *args):
        self.destroy()