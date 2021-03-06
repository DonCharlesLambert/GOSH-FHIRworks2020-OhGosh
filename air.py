"""
AIR💨
3) A suitable package that is made available and deployable as a demonstrator
This file contains file produces the deployable application, showing patient data through
graphs and charts

The file is titled air as it creates a window
"""

from tkinter import *
from tkinter.ttk import Progressbar
from functools import partial
from threading import Thread
from time import sleep
from os import path, remove
from glob import glob
from PIL import Image, ImageTk
from water import *
from earth import *


class Aang:
    logo = None
    graph_image = None
    graph = None
    chart_type = None
    progress = None

    def __init__(self):
        root = Tk()
        self.root = root
        root.config(bg=BACKGROUND_COLOR)
        root.resizable(False, False)
        self.add_logo()
        self.add_graph()
        self.add_menu()
        self.add_loading()
        root.mainloop()

    def add_logo(self):
        global logo
        logo = self.get_image(75, 75, "img\logo.png")
        Label(self.root, image=logo, bg=BACKGROUND_COLOR).grid(row=1, columnspan=6)

    def add_menu(self):
        self.chart_type = StringVar(self.root)
        choices = {'Pie Chart', 'Bar Chart'}
        self.chart_type.set('Pie Chart')

        chart_selector = OptionMenu(self.root, self.chart_type, *choices)
        chart_selector.config(bg=BACKGROUND_COLOR, width=12)
        chart_selector.grid(row=2)
        Button(self.root, text="Marital Status", command=partial(self.get_diagram, MARITAL), bg=BACKGROUND_COLOR, width=15).grid(row=3)
        Button(self.root, text="Gender", command=partial(self.get_diagram, GENDER), bg=BACKGROUND_COLOR, width=15).grid(row=4)
        Button(self.root, text="Age", command=partial(self.get_diagram, AGE), bg=BACKGROUND_COLOR, width=15).grid(row=5)
        Button(self.root, text="Multiple Birthdays", command=partial(self.get_diagram, MULTIPLE_BIRTH), bg=BACKGROUND_COLOR, width=15).grid(row=6)
        Button(self.root, text="Refresh", command=self.refresh, bg=BACKGROUND_COLOR, width=15).grid(row=7)

    def add_graph(self):
        self.graph_image = self.get_image(480, 360, r"img\bg.png")
        self.graph = Label(self.root, image=self.graph_image, bg=BACKGROUND_COLOR)
        self.graph.grid(column=2, rowspan=6)

    def add_loading(self):
        self.progress = Progressbar(self.root)
        self.progress.grid(row=8)

    def get_diagram(self, field):
        Thread(target=partial(self.show_diagram, field)).start()
        Thread(target=self.simulate_loading).start()

    def show_diagram(self, field):
        if self.chart_type.get() == "Bar Chart":
            location = r"data\bar" + str(field) + ".png"
            if not path.exists(location):
                location = bar_chart_for_field(field)
        else:
            location = r"data\pie" + str(field) + ".png"
            if not path.exists(location):
                location = pie_chart_for_field(field)
        self.graph_image = self.get_image(480, 360, location)
        self.graph.configure(image=self.graph_image)

    def simulate_loading(self):
        old_image = self.graph_image
        while self.graph_image == old_image:
            self.progress['value'] = (self.progress['value'] + 10) % 100
            sleep(0.3)
        self.progress['value'] = 0

    def refresh(self):
        #delete all images
        files = glob('data/*')
        for f in files:
            remove(f)

    @staticmethod
    def get_image(width, height, img):
        img = Image.open(img)
        img = img.resize((width, height), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)  # convert to PhotoImage
        return img


Aang()
