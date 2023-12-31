# source: adapted from https://plotly.com/python/sunburst-charts/

import plotly.express as px
import numpy as np
import dash
from dash import dcc, html

def example():
    """
    This created a plotly figure.
    Outside an app it can be displayed using fig.show().
    """
    df = px.data.gapminder().query("year == 2007")
    fig = px.sunburst(df, path=['continent', 'country'], values='pop',
                      color='lifeExp', hover_data=['iso_alpha'],
                      color_continuous_scale='RdBu',
                      color_continuous_midpoint=np.average(df['lifeExp'], weights=df['pop']))
    return fig

app = dash.Dash(__name__)
app.title = "PyHEP23"

app.layout = html.Div(
    [html.H2("PyHEP 2023 Demo"),
     dcc.Graph(id='graph', figure=example(), style={'width': '90vh', 'height': '90vh'}),])

if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0", port=8080)
    
