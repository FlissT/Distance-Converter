#km to miles converter

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Converter(Gtk.Bin): #builds the Gtk stuff
    def __init__(self):
        Gtk.Bin.__init__(self)
        
        self.builder = Gtk.Builder()
        self.builder.add_from_file("distance_converter.glade")
        
        self.convert_box = self.builder.get_object("GtkBox")
        self.add(self.convert_box)
        
        self.label = self.builder.get_object("GtkLabel")
        self.button = self.builder.get_object("GtkButton")
        self.button.connect("clicked", self.clicked_callback)
        self.entry = self.builder.get_object("GtkEntry")
        self.result = self.builder.get_object("GtkResult")

    def convert(self): #function that actually does the converting
        a = 0.62

        user_input = self.entry.get_text()
        km = self.entry
        self.label.set_text("How many kilometres? ")
        km_entry = self.entry.get_text()
        kms = float(km_entry)
        miles = (kms*a)


        self.label.set_text("Here are your miles: ")
        self.result.set_text(str(round(miles, 2)))

    def clicked_callback(self, button): #makes button work
        self.convert()


class MyWindow(Gtk.Window): #pulls it together
    def __init__(self):
        Gtk.Window.__init__(self)

        vbox = Gtk.VBox()
        conv_box = Converter()
        vbox.add(conv_box)
        self.set_title("Km to Mile Converter")

        self.add(vbox)

        self.show_all()
        self.connect("delete-event", self.on_quit)
        
    def on_quit(self, widget, event):
        Gtk.main_quit()

window = MyWindow()


Gtk.main()
