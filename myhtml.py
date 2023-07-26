import dash
from dash import dcc
from dash import html

app = dash.Dash()

app.layout = html.Div(
    children=[
        html.Div(
            'This is the outermost Div',
            style={'color': 'red', 'border': '2px green solid', 'width': 500, 'height': 200}
        ),
        html.Div(
            'This is the inner Div',
            style={'color': 'blue', 'border': '2px blue solid', 'borderRadius': 5, 'padding': 10, 'width': 220}
        ),
        html.Div(
            'This is another inner Div',
            style={'color': 'green', 'border': '2px green solid', 'margin': 10, 'width': 220}
        ),
    ],
)

if __name__ == '__main__':
    app.run_server(debug=True)
