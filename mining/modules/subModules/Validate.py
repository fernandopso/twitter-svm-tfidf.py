#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Validate:
    def __init__(self):
        super(Validate, self).__init__()
        self.set_title("Validate")
        self.set_size_request(300, 100)
        self.set_position(gtk.WIN_POS_CENTER)

        fixed = gtk.Fixed()

        #Label to alert user.
        self.labelAlert = gtk.Label("Qual seria a opção correta?")
        fixed.put(self.labelAlert, 60, 20)

        self.bt_positivo = gtk.Button("Positivo")
        self.bt_positivo.connect("clicked", self.on_clicked, 1)
        self.bt_positivo.set_size_request(80, 30)
        fixed.put(self.bt_positivo, 10, 50)

        #Button to exit the window 'Treinar Dados'.
        self.bt_negativo = gtk.Button("Negativo")
        self.bt_negativo.connect("clicked", self.on_clicked, 2)
        self.bt_negativo.set_size_request(80, 30)
        fixed.put(self.bt_negativo, 110, 50)

        #Button to exit the window 'Treinar Dados'.
        self.bt_neutro = gtk.Button("Neutro")
        self.bt_neutro.connect("clicked", self.on_clicked, 3)
        self.bt_neutro.set_size_request(80, 30)
        fixed.put(self.bt_neutro, 210, 50)        

        self.add(fixed)
        self.show_all()

    def on_clicked(self, button, i, *args):
        print i
        self.destroy()