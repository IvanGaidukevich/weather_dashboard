from datetime import date
from dash import Input, Output, html
import plotly.graph_objects as go
from utils.db import load_temperature_data, get_temperature_date_bounds


def register_db_temperature_callbacks(app):

    @app.callback(
            Output('db-start-year', 'options'),
            Output('db-end-year', 'options'),
            Output('db-start-year', 'value'),
            Output('db-end-year', 'value'),
            Input('weather-tabs', 'active_tab')
    )
    def init_db_year_range(_active_tab):
        min_date, max_date = get_temperature_date_bounds()
        years = list(range(min_date.year, max_date.year + 1))
        options = [{'label': str(year), 'value': year } for year in years]
        return options, options, min_date.year, max_date.year
    

    @app.callback(
            Output('db-temp-graph', 'figure'),  #show-db-max
            Input('db-start-year', 'value'),
            Input('db-end-year', 'value'),
            Input('show-db-avg', 'value'),
            Input('show-db-min', 'value'),
            Input('show-db-max', 'value')
    )
    def update_db_temperature_graph(start_year, end_year, show_avg, show_min, show_max):
        
        start_year = int(start_year)
        end_year = int(end_year)

        if start_year > end_year:
            start_year, end_year = end_year, start_year

        start_date = date(start_year, 1, 1)
        end_date = date(end_year, 12, 31)

        rows = load_temperature_data(start_date, end_date) # запрос в базу

        dates = [row['date'] for row in rows]

        figure = go.Figure(
                layout=go.Layout(
                    title='Температура в новый год',
                    xaxis_title='Год',
                    yaxis_title='Температура (°C)'
                )
        )

        if show_avg:
            figure.add_trace(go.Scatter(
                x=dates,
                y=[row['avgtemp_c'] for row in rows],
                mode='lines+markers',
                name='Средняя температура'
            ))

        
        if show_min:
            figure.add_trace(go.Scatter(
                x=dates,
                y=[row['mintemp_c'] for row in rows],
                mode='lines+markers',
                name='Минимальная температура'
            ))

        
        if show_max:
            figure.add_trace(go.Scatter(
                x=dates,
                y=[row['maxtemp_c'] for row in rows],
                mode='lines+markers',
                name='Максимальная температура'
            ))

        return figure
