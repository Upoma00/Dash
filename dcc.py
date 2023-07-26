import dash
from dash import dcc
from dash import html
import numpy as np
import plotly.graph_objects as go

app = dash.Dash(__name__)

np.random.seed(42)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

app.layout = html.Div([
    dcc.Graph(
        id='scatter',
        figure={
            'data': [
                go.Scatter(
                    x=random_x,
                    y=random_y,
                    mode='markers',
                    marker={
                        'size': 12,
                        'color': 'rgb(51, 204, 153)',
                        'symbol': 'pentagon',
                        'line': {'width': 2}
                    }
                )
            ],
            'layout': go.Layout(
                title='Random Data ScatterPlot',
                xaxis={'title': 'X-axis'},
                yaxis={'title': 'Y-axis'},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
