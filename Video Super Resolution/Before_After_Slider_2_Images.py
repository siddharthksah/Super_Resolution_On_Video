import dash  # pip install dash
import dash_html_components as html
from dash_extensions import BeforeAfter  # pip install dash-extensions==0.0.47 or higher
import dash_bootstrap_components as dbc  # dash-bootstrap-components

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container([
    dbc.Row(
        dbc.Col([
            html.H1("Before/After Image Comparison using slider in Python", style={'textAlign': 'center'})
        ], width=12)
    ),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            BeforeAfter(before="assets/real.jpg", after="assets/upscaled.jpg", width=960, height=640,
                        defaultProgress=0.5),
        ], width=6)

    ]),

])

if __name__ == '__main__':
    app.run_server(debug=True, port=8002)