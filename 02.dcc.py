import dash
from dash import dcc
from dash import html

app = dash.Dash()

app.layout = html.Div([
    html.Label('Dropdown'),  
    dcc.Dropdown(
        options=[
            {'label': 'North Carolina', 'value': 'NC'},
            {'label': 'Chicago', 'value': 'CHI'},
            {'label': 'California', 'value': 'CA'},
        ],
        value='NC'
    ),
    html.Label('Multi-Select Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'North Carolina', 'value': 'NC'},
            {'label': 'Chicago', 'value': 'CHI'},
            {'label': 'California', 'value': 'CA'},
        ],
        value=['CHI', 'NC'],
        multi=True
    ),

    # SLIDER: https://dash.plotly.com/dash-core-components/slider

    html.Label('Slider'),  
    dcc.Slider(
        min=5,
        max=15,
        step=0.5,
        marks={i: str(i) for i in range(-5, 16)}, 
        value=3
    ),

    # City Name:
    html.Label('City Name'), 
    dcc.RadioItems( 
        options=[
            {'label': 'Raleigh', 'value': 'Raleigh'},  # Fixed the value for 'Raleigh'
            {'label': 'Urbana Champaign', 'value': 'Urbana Champaign'},  # Fixed the value for 'Urbana Champaign'
            {'label': 'San Francisco', 'value': 'San Francisco'},  # Fixed the value for 'San Francisco'
        ],
        value='Raleigh',  # Changed the default value to 'Raleigh'
        style={'width': '50%'}  # Fixed the style dictionary syntax
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)


 



