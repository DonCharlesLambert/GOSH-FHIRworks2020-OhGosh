"""
WATER💦
2) A usable API for further developers to build with your technology
Water, Fire & Earth together serve as a usable API for further development
Water is the interface for this API, providing functions to save bar and pie chart images from FHIR patient data

The file is titled water in order to match the running theme of the four elements from the show
Avatar: The Legend of Aang
"""

import matplotlib.pyplot as plot
from fire import *
from earth import GRAPH_FOLDER


def get_xy_data(field):
    fire_style_fire_ball_jutsu = FireData()
    data = fire_style_fire_ball_jutsu.get_data_totals(field)
    x = []
    y = []
    for key in data.keys():
        x.append(key)
        y.append(data[key])
    return x, y


def bar_chart_for_field(field):
    x, y = get_xy_data(field)
    return create_bar_chart(x, y, str(field))


def pie_chart_for_field(field):
    x, y = get_xy_data(field)
    return create_pie_chart(x, y, str(field))


# Creates a bar chart given x and y values
def create_bar_chart(x, y, name):
    save_name = GRAPH_FOLDER + name + ".png"

    fig = plot.figure()
    fig.patch.set_facecolor(BACKGROUND_COLOR)
    ax = plot.subplot()
    ax.patch.set_facecolor(BACKGROUND_COLOR)
    ax.patch.set_alpha(0.5)

    plot.bar(range(len(x)), y, align='center')
    plot.xticks(range(len(x)), x)

    plot.savefig(save_name, facecolor=fig.get_facecolor(), edgecolor='none')
    return save_name


# Creates a pie chart given x and y values
def create_pie_chart(x, y, name):
    save_name = GRAPH_FOLDER + name + ".png"

    fig = plot.figure()
    fig.patch.set_facecolor(BACKGROUND_COLOR)
    ax = plot.subplot()
    ax.patch.set_facecolor(BACKGROUND_COLOR)
    ax.patch.set_alpha(0.5)

    fig1, ax1 = plot.subplots()
    ax1.pie(y, labels=x, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')

    plot.savefig(save_name, facecolor=fig.get_facecolor(), edgecolor='none')
    return save_name

