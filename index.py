import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app
from app import server


# Connect to your app pages
from apps import arxiki, koinwnia, oikonomia


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('Εξέλιξη Πανδημίας  |  ', href='/apps/arxiki'),
        dcc.Link('Οικονομία  |  ', href='/apps/oikonomia'),
        dcc.Link('Κοινωνία', href='/apps/koinwnia'),
    ], className="row"),
    html.Div(id='page-content', children=[])
])



@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/arxiki':
        return arxiki.layout
    if pathname == '/apps/oikonomia':
        return oikonomia.layout
    if pathname == '/apps/koinwnia':
        return koinwnia.layout
    else:
        return arxiki.layout



if __name__ == '__main__':
    app.run_server(debug=False)