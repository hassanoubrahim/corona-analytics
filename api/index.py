"""Importing the required libraries"""

import pandas as pd
import plotly.graph_objs as go
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

"""Reading data from CSV"""
data = pd.read_csv('data.csv')

"""Building the plotting functions"""

def plot_continent_data(data, keyword):
    # (Function implementation remains the same)

def get_continent_sorted_data(data, continent, sortedby="TotalCases", ascending=False):
    # (Function implementation remains the same)

def get_top_k_countries(data, k_countries=10, sortedby="TotalCases", ascending=False):
    # (Function implementation remains the same)

def plot_top_k_countries(n_countries, sortby):
    # (Function implementation remains the same)

def plot_boxplots(data, keyword="Deaths/1M pop"):
    # (Function implementation remains the same)

def init_figure():
    # (Function implementation remains the same)

"""Building the app"""

# Initializing the app
app = Dash(__name__)
server = app.server

# Building the app layout
app.layout = html.Div([
    html.H1("Corona Tracker DashBoard", style={"text-align": "center"}),
    html.Br(),
    html.Div([
        html.Br(),
        html.H2("Corona Cases/Recovered/Deaths by Continent", style={"text-align": "center"}),
        html.Br(),
        dcc.Dropdown(id="select_keyword",
                     options=[
                         dict(label="Today's Data", value="New"),
                         dict(label="Total Data", value="Total")],
                     multi=False,
                     value="New",
                     style={"width": "40%"}
                     ),
        dcc.Graph(id="continent_corona_bar", figure=init_continent_fig)
    ]),

    # (Remaining layout remains the same)
])

# Defining the application callbacks
@app.callback(
    Output("continent_corona_bar", "figure"),
    Input("select_keyword", "value")
)
def update_continent_corona_bar(value):
    return plot_continent_data(data, keyword=value)

@app.callback(
    Output("k_countries_sorted", "figure"),
    Input("select_attribute", "value"),
    Input("select_k_countries", "value")
)
def update_k_countries_sorted(attribute, n_countries):
    return plot_top_k_countries(n_countries, attribute)

@app.callback(
    Output("continent_box_plot", "figure"),
    Input("select_box_attribute", "value")
)
def update_continent_box_plot(value):
    return plot_boxplots(data, keyword=value)

@app.callback(
    Output("map_plot", "figure"),
    Input("select_map_attribute", "value")
)

@app.callback(
    Output("my-graph", "figure"),
    [Input("value-selected", "value")]
)
def update_figure(selected):
    # (Function implementation remains the same)

if __name__ == "__main__":
    app.run_server()
