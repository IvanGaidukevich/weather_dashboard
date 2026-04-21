import plotly.graph_objects as go

COLORS = {
    'text': '#10212e',
    'grid': '#d7e7f3',
    'surface': '#ffffff',
    'accent': '#ff7a18',
    'violet':'#786fa6',
    'pink':'#f8a5c2',
    'blue': '#63cdda',
}

def apply_theme(fig: go.Figure):
    fig.update_layout(
        font = {'color': COLORS['text'], 'family': 'Space Grotesk, sans-serif'},
        plot_bgcolor = COLORS['surface'],
        colorway = [
            COLORS['violet'],
            COLORS['pink'],
            COLORS['blue']
        ],
    )

    fig.update_xaxes(
        showgrid = True,
        gridwidth = 1,
        gridcolor = COLORS['grid'])
    
    fig.update_yaxes(
        showgrid = True,
        gridwidth = 1,
        gridcolor = COLORS['grid'])

    return fig

