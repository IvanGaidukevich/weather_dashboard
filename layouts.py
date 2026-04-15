import dash_bootstrap_components as dbc
from dash import dcc

def create_layout():
    return dbc.Container([
        dbc.NavbarSimple(brand='Погодный дашборд', color='primary', dark=True, className='mb-3'),
        dbc.Row([
            dbc.Col([
                dbc.Input(id='city-input', 
                          placeholder='Введите город...', 
                          type='text', 
                          value='Москва', 
                          debounce=True),
                
                   dbc.Card(
                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col(
                                dbc.Switch(
                                    id='show-temp-ma',
                                    label='Скользящее среднее t',
                                    value=False,
                                ),
                                width=12,
                                md=6,
                            ),
                            dbc.Col(
                                dbc.Switch(
                                    id='show-ap-ma',
                                    label='Скользящее среднее AД',
                                    value=False,
                                ),
                                width=12,
                                md=6,
                            ),
                        ], className='mb-3'),
                        dbc.Label("Размер окна"),
                        dcc.Slider(
                            id='ma-window',
                            min=2,
                            max=8,
                            step=1,
                            value=3,
                            marks={i: str(i) for i in [2, 4, 6, 8]},
                            tooltip={"placement": "bottom", "always_visible": False},
                           
                        ),
                    ]),
                    className='mt-3'
                ),
                ], width=6, xs=12, md=6),

            dbc.Col([
                dbc.Card(id='weather-output', body=True)
                ], width=6, xs=12, md=6),
        ], className='mb-3'),
        dbc.Row([
            dbc.Col([
                dcc.Graph(id='temp-graph')
                ], width=6, xs=12, md=6),
            dbc.Col([
                dcc.Graph(id='ap-graph')
                ], width=6, xs=12, md=6),
        ], className='mb-3'),
        dbc.Row([
            dbc.Col([
                dcc.Graph(id='wind-dir-graph')
                ], width=12, xs=12, md=12),
        ], className='mb-3'),
    ], fluid=True)