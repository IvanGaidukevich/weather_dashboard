from dash import Input, Output, html
from utils.data_loader import load_data
from assets.plotly_theme import apply_theme
import plotly.graph_objects as go



def calc_moving_average(values, window):
    if not values:
        return []
    window = max(1, int(window))
    result = []
    for i in range(len(values)):
        start = max(0, i - window + 1)
        current = values[start:i + 1]
        result.append(sum(current) / len(current))
    return result


def register_callbacks_live(app):

    @app.callback(
            Output('weather-output', 'children'),
            Output('temp-graph', 'figure'),
            Output('ap-graph', 'figure'),
            Output('wind-dir-graph', 'figure'),
            Input('city-input', 'value'),
            Input('show-temp-ma', 'value'),
            Input('show-ap-ma', 'value'),
            Input('ma-window', 'value')
    )
    def update_dashboard(city: str, show_temp_ma: bool, show_ap_ma: bool, ma_window: int):
        data = load_data(city)

        weather_info = html.Div([
            html.H4(f"{data['city']}"),
            html.Img(src=f"https:{data['icon']}"),
            html.H5(f"{data['temp']} C"),
            html.P(data['condition'])
        ])

    
        temp_fig = go.Figure(
            data=[go.Scatter(x=data["hours"], y=data["temps"], mode='lines+markers', name='Температура')],
            layout=go.Layout(title='Температура по часам', xaxis_title='Время', yaxis_title='Температура (°C)', 
                            )
        )

        if show_temp_ma:
            temp_ma = calc_moving_average(data['temps'], ma_window)
            temp_fig.add_trace(
                go.Scatter(
                    x=data['hours'],
                    y=temp_ma,
                    mode='lines',
                    name=f"Cр. t окно {ma_window}",
                    line=dict(width=3, dash='dash')
                )
            )



        ap_fig = go.Figure(
            data=[go.Scatter(x=data["hours"], y=data["ap"], mode='lines+markers', name='Атмосферное давление')],
            layout=go.Layout(title='Атмосферное давление по часам', xaxis_title='Время', yaxis_title='АД (мм рт.ст.)', 
                            )
        )

        if show_ap_ma:
            ap_ma = calc_moving_average(data['ap'], ma_window)
            ap_fig.add_trace(
                go.Scatter(
                    x=data['hours'],
                    y=ap_ma,
                    mode='lines',
                    name=f"Cр. АД окно {ma_window}",
                    line=dict(width=3, dash='dash')
                )
            )



        wind_dir_fig = go.Figure(
            data=go.Scatterpolar(
                r=data["wind"], 
                theta=data["wind_dirs"], 
                mode='lines+markers', 
                name='Ветер',
                customdata=data["hours"],
                hovertemplate="<b>Время:</b> %{customdata}<br><b>Скорость ветра:</b> %{r} м/с<br><b>Направление:</b> %{theta}°<br><extra></extra>"
            ),
        )

        wind_dir_fig.update_layout(
            title='Направление и скорость ветра (м/с)',
            polar=dict(
                angularaxis=dict(
                    direction="clockwise",
                    tickmode="array",
                    rotation=90,
                    tickvals=[0, 45, 90, 135, 180, 225, 270, 315],
                    ticktext=["С", "СВ", "В", "ЮВ", "Ю", "ЮЗ", "З", "СЗ"]
                )
                
            )
            
        )

        return weather_info, apply_theme(temp_fig), apply_theme(ap_fig), apply_theme(wind_dir_fig)