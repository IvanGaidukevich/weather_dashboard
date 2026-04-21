import dash_bootstrap_components as dbc
from dash import dcc

def create_layout():
    return dbc.Container([
        dbc.NavbarSimple(
            brand="🌦 Прогноз  погоды 🌦",
            brand_href="#",
            color="primary",
            dark=True,
            className="weather-navbar mb-4",
        ),
        dbc.Tabs(
            id='weather-tabs',
            active_tab='live-weather-tab',
            className="weather-tabs",
            children=[
                dbc.Tab(
                    label='Текущий прогноз',
                    tab_id='live-weather-tab',
                    children=[
                        dbc.Row([
                            dbc.Col([
                                dbc.Input(id='city-input', value='Санкт-Петербург', type='text', placeholder="Введите город", debounce=True),
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
                                                    label='Скользящее среднее AP',
                                                    value=False,
                                                ),
                                                width=12,
                                                md=6,
                                            ),
                                        ], className="mb-3"),
                                        dbc.Label("Размер окна (часы)"),
                                        dcc.Slider(
                                            id='ma-window',
                                            min=2,
                                            max=8,
                                            step=1,
                                            value=3,
                                            marks={i: str(i) for i in [2, 4, 6, 8]},
                                        ),
                                    ]),
                                    className="weather-card mt-3"
                                ),
                            ], width=6, xs=12, md=6),
                            dbc.Col(dbc.Card(id='weather-output', 
                                             body=True, class_name='weather-card'), 
                                             width=6, xs=12, md=6),
                        ], className="mb-3 mt-3"),

                        dbc.Row([
                            dbc.Col(dcc.Graph(id='temp-graph'), 
                                    width=6, xs=12, md=6),
                            dbc.Col(dcc.Graph(id='ap-graph'), 
                                    width=6, xs=12, md=6),
                        ], className="mb-3"),

                        dbc.Row([
                            dbc.Col(dcc.Graph(id='wind-dir-graph'), 
                                    width=12, xs=12, md=12),
                        ], className="mb-3"),
                    ]
                ),
                dbc.Tab(
                    label='Исторические данные',
                    tab_id='historical-weather-tab',
                    children=[
                        dbc.Row([
                            dbc.Col([
                                dbc.Label('Год начала'),
                                dcc.Dropdown(
                                    id='db-start-year',
                                    options=[],
                                    value=None,
                                    clearable=False,
                                    placeholder='Выберите стартовый год',
                                    className='mb-3',
                                    style={'color': 'black'}
                                ),
                            ], width=12, md=3),
                            dbc.Col([
                                dbc.Label('Год конца'),
                                dcc.Dropdown(
                                    id='db-end-year',
                                    options=[],
                                    value=None,
                                    clearable=False,
                                    placeholder='Выберите конечный год',
                                    className='mb-3',
                                    style={'color': 'black'}

                                ),
                            ], width=12, md=3),
                            dbc.Col([
                                dbc.Label('Показывать линии'),
                                dbc.Row([
                                    dbc.Col(dbc.Switch(id='show-db-avg', 
                                                       label='Средняя температура', 
                                                       value=True), 
                                                       width=12, md=4),
                                    dbc.Col(dbc.Switch(id='show-db-min', 
                                                       label='Минимальная температура', 
                                                       value=True), 
                                                       width=12, md=4),
                                    dbc.Col(dbc.Switch(id='show-db-max', 
                                                       label='Максимальная температура', 
                                                       value=True), 
                                                       width=12, md=4),
                                ]),
                            ], width=12, md=6),
                        ], className='weather-card mt-3 mb-3 mx-2 p-3'),
                        dbc.Row([
                            dbc.Col(dcc.Graph(id='db-temp-graph'), 
                                    width=12),
                        ]),
                    ]
                ),
            ]
        ),
    ], fluid=True)