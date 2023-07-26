import dash
from dash import dcc
from dash import html

app = dash.Dash()

colors = {
    'background': '#111111',
    'text': '#7fdbff'
}

app.layout = html.Div(children=[
    html.H1("Hello dash",
            style={
                'textAlign': 'center',
                'color': colors['text']
            }),
    html.Div(
        children='Dash: A web application',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    dcc.Graph(id='example-graph',
              figure={
                  'data': [
                      {'x': [1, 2, 3, 4], 'y': [4, 1, 2, 5], 'type': 'bar', 'name': 'Iphone'},
                      {'x': [1, 2, 3, 4], 'y': [3, 6, 9, 4], 'type': 'bar', 'name': 'Samsung'},
                  ],
                  'layout': {
                      'plot_bgcolor': colors['background'],
                      'title': 'Dash Data Visualization',
                      'paper_bgcolor': colors['background'],
                      'font': {
                          'color': colors['text']
                      },
                      'xaxis': {'title': 'X-axis label'},
                      'yaxis': {'title': 'Y-axis label'},
                  }
              })
])

if __name__ == '__main__':
    app.run_server(debug=True)

