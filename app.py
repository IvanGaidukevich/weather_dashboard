from dash import Dash
import dash_bootstrap_components as dbc
from layouts import create_layout
from callbacks import register_callbacks


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = 'Погодный дашборд'
app.layout = create_layout()
server = app.server


register_callbacks(app)

if __name__ == '__main__':
    app.run(debug=False)