import pandas as pd
import numpy as np

import plotly.graph_objects as go

from flask import Flask
from dash import Dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output


df = pd.read_csv('games.csv')
df = df[df['Year_of_Release'] >= 2000]
# переводим object в float в столбце User_Score
df['User_Score'] = pd.to_numeric(df['User_Score'], errors='coerce')
df = df.dropna(axis=0)


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Flask(__name__)
dash_app = Dash(__name__, server=app, external_stylesheets=external_stylesheets)


dash_app.layout = html.Div([
    html.H1('История состояния игровой индустрии'),

    html.Div(
        [html.P('Данный дашборд показывает информацию о выпуске компьтерных играх в определенном временном интервале.'),
         html.P(
             'По установленным фильтрациям Вы можете увидеть график, \
             показывающий выпуск игр по годам и платформам, график оценок игр определнного жанра, \
             а также количество игр при заданных параметрах.'),
         html.U("Инструкция:"),
         html.P('1. Для установки интересующих жанров воспользуйтесть фильтром жанров'),
         html.P('2. Для установки возрастных рейтингов воспользуйтесь фильтром рейтингов'),
         html.P('3. Варьирование интервала годов выпуска осуществляется с помощью ползунка внизу'), ],
        style={'padding': '20px 20px 20px 20px'}),

    html.Div(children=[
        html.Div([
            html.Label('Фильтр жанров'),
            dcc.Dropdown(
                options=[{'label': genre, 'value': genre} for genre in df['Genre'].unique()],
                id='genre--dropdown',
                value=['Sports', 'Racing'],
                multi=True
            )], style={'display': 'inline-block', 'width': '45%', 'padding': '20px 20px 20px 20px'}),

        html.Div([
            html.Label('Фильтр рейтингов'),
            dcc.Dropdown(
                options=[{'label': rating, 'value': rating} for rating in df['Rating'].unique()],
                id='rating--dropdown',
                value='E',
                multi=True
            )], style={'display': 'inline-block', 'width': '45%', 'padding': '20px 20px 20px 20px'}),
    ], className='row'),

    html.Div(children=[
        html.Div(html.Label(id='output-num-filt-games'),
                 style={'padding': '40px 20px 20px 20px'}),
    ], className='row'),

    html.Div([
        dcc.Graph(id='plot_1')
    ], style={'float': 'left', 'width': '49%', 'display': 'inline-block',
              }),
    html.Div([
        dcc.Graph(id='plot_2')
    ], style={'float': 'right', 'width': '49%', 'display': 'inline-block',
              }),

    html.Div([
        html.Label(id='output-years'),
        dcc.RangeSlider(
            min=2000,
            max=int(df['Year_of_Release'].max()),
            step=None,
            marks={year: {'label': str(year)} for year in df['Year_of_Release'].unique()},
            value=[2001, 2006],
            id='bound-year--slider',
            updatemode='mouseup'
        )], style={'width': '49%', 'display': 'inline-block', 'padding': '40px 20px 20px 20px'}),

    #     html.Div(id='output-container-range-slider-non-linear')
])


@dash_app.callback(
    [Output('output-num-filt-games', 'children'),
     Output('output-years', 'children'),
     Output('plot_1', 'figure'), Output('plot_2', 'figure')],
    #     Output('output-container-range-slider-non-linear', 'children'),
    [Input('genre--dropdown', 'value'),
     Input('rating--dropdown', 'value'),
     Input('bound-year--slider', 'value'), ])
def display_plot_1(genre, rating, bound_year):
    fig_1 = go.Figure()
    fig_2 = go.Figure()

    plot_df = df[(df['Year_of_Release'] >= bound_year[0]) & (df['Year_of_Release'] <= bound_year[1]) &
                 (df['Genre'].isin(list(genre))) & (df['Rating'].isin(list(rating)))]

    # make plot 1
    # Stacked area plot, показывающий выпуск игр по годам и платформам.
    uniq_year = np.sort(plot_df['Year_of_Release'].unique())
    for pl, pl_data in plot_df.groupby(by='Platform'):
        year_pl_counter = []
        for year in uniq_year:
            y_data = pl_data[pl_data['Year_of_Release'] == year]
            year_pl_counter += [y_data.shape[0]]

        fig_1.add_trace(go.Scatter(
            y=year_pl_counter,
            x=uniq_year,
            name=pl,
            legendgroup='a',
            stackgroup='one',
            hovertemplate="%{x}, %{y}"), )

    # make plot 2
    # Scatter plot с разбивкой по жанрам (каждому жанру соответствует один цвет). По оси X - оценки игроков,
    # по оси Y - оценки критиков.
    for g, g_data in plot_df.groupby(by='Genre'):
        fig_2.add_trace(go.Scatter(
            y=g_data['Critic_Score'],
            x=g_data['User_Score'],
            name=g,
            legendgroup='b',
            mode='markers',
            hovertemplate="%{x}, %{y}",
            # opacity=0.8,
            marker=dict(colorscale='Viridis',
                        line_width=1)), )

    fig_1.update_annotations(patch=dict(font=dict(family="Helvetica", size=15)))
    fig_1.update_layout(  # height=400, width=1200,
        margin=dict(l=20, r=20, t=20, b=20),
        # paper_bgcolor="lightgrey",
        xaxis_title="год релиза",
        legend_title="Игровые платформы",
    )

    fig_2.update_annotations(patch=dict(font=dict(family="Helvetica", size=15)))
    fig_2.update_layout(  # height=400, width=1200,
        margin=dict(l=20, r=20, t=20, b=20),
        # paper_bgcolor="lightgrey",
        xaxis_title="оценки игроков",
        yaxis_title="оценки критиков",
        legend_title="Жанры",
    )

    return ['Количество выбранных игр: {}'.format(plot_df['Name'].shape[0]),
            'Интервал годов выпуска: от %d до %d' % (bound_year[0], bound_year[1]),
            fig_1, fig_2]


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
