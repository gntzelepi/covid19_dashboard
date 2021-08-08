import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import pathlib
from app import app


# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

# automated figure update
def update_figure(figure, title):
    layout = figure.update_layout(
        title_text= title, title_x=0.5,
        xaxis_title="",
        xaxis=dict(
            showticklabels= True,
            tickfont=dict(
                family= 'Arial', size=10, color='rgb(82,82,82)')),
        yaxis=dict(
            gridcolor='rgb(243,243,243)'),
        plot_bgcolor='white',
        hovermode="x",
    legend=dict(
        title=None, orientation="h", y=1, yanchor="bottom", x=0.5, xanchor="center"),
        margin=dict(l=30, r=30, t=120, b=50))
    traces = figure.update_traces(hovertemplate=None)
    return figure

""" DATASETS AND FIGURES CODE"""

# GDP Dataset
df = pd.read_csv(DATA_PATH.joinpath("gdp_dash.csv"))

# Figure 1
fig = px.bar(df, x='quarter', y='OBS_VALUE', color='year', barmode='group', text='metavoli',
                   color_discrete_sequence=px.colors.qualitative.Set2,
                   labels= {'value': 'Τιμή', 'OBS_VALUE':"", 'klados': 'Κατηγορία', 'year':"Ημερομηνία"})
# automated figure modifications
update_figure(fig, '<span style="font-size: 15px;"> ΑΕΠ (εκατ. ευρώ) & τριμηνιαία μεταβολή ανά έτος (%)</span>')
# legend names
fig.data[0].name = '2019'
fig.data[1].name = '2020'
fig.data[2].name = '2021'
# hover info modifications
fig.update_traces(hovertemplate="<br>".join(["%{y}"]))



# Expenditure Dataset
df = pd.read_csv(DATA_PATH.joinpath("expenditure_dash.csv"))

# Figure 2
fig_2 = px.bar(df, y='value', x='freq;unit;na_item;geo\TIME_PERIOD', color='date', barmode='group', text='metavoli',
                   color_discrete_sequence=px.colors.qualitative.Set2,
                   labels= {'index_value': 'Τιμή', 'date': 'Ημερομηνία', 'component': 'Κατηγορία', "value":""})
# automated figure modifications
update_figure(fig_2, '<span style="font-size: 15px;">Δαπάνες ανά κατηγορία & ετήσια μεταβολή (%)<br></span><span style="font-size: 12px;"> (2015=100)</span>')
# legend names
fig_2.data[0].name = '2019'
fig_2.data[1].name = '2020'
# hover info modifications
fig_2.update_traces(hovertemplate="<br>".join(["%{y}"]))



# Income Dataset
df = pd.read_csv(DATA_PATH.joinpath('income_dash.csv'))

# Figure 3
fig_3 = px.bar(df, y='OBS_VALUE', x='na_item', color='TIME_PERIOD', barmode='group',text='metavoli',
                   color_discrete_sequence=px.colors.qualitative.Pastel1,
                   labels= {'index_value': 'Τιμή', 'date': 'Ημερομηνία', 'component': 'Κατηγορία', 'OBS_VALUE':""})
# automated figure modifications
update_figure(fig_3, '<span style="font-size: 15px;">Εισοδήματα παραγωγικών συντελεστών & μεταβολή (%)<br></span><span style="font-size: 12px;">(εκατ. ευρώ σε τρέχουσες τιμές)</span>')
# legend names
fig_3.data[0].name = '2019'
fig_3.data[1].name = '2020'
# hover info modifications
fig_3.update_traces(hovertemplate="<br>".join(["%{y}"]))



# HICP Dataset
df = pd.read_csv(DATA_PATH.joinpath('hicp_dash.csv'))

# Figure 4
fig_4 = px.line(df, y='index_value', x='date', color_discrete_sequence=['rgb(102, 197, 204)'],
                labels= {'index_value': 'Τιμή', 'date': 'Ημερομηνία'})
# automated figure modifications
update_figure(fig_4, 'Εξέλιξη Εναρμονισμένου Δείκτη Τιμών Καταναλωτή (ετήσιος ρυθμός μεταβολής)')
# add markers to line
fig_4.data[0].update(mode='markers+lines')



# HICP Components Dataset
df = pd.read_csv(DATA_PATH.joinpath('components_dash.csv'))

# Figure 5
fig_5 = px.bar(df, y='metavoli ', x='freq;unit;coicop;geo\TIME_PERIOD', 
                    color='freq;unit;coicop;geo\TIME_PERIOD',
                   color_discrete_sequence=px.colors.qualitative.Dark24,
                   labels= {'metavoli ': ''})
# automated figure modifications
update_figure(fig_5, '<span style="font-size: 14px;">Μεταβολή μέσου Εν.ΔΤΚ 2020 ανά κατηγορία</span>')
# show x-axis label for each sub-plot
fig_5.update_xaxes(matches=None, showticklabels=True, visible=True, showgrid=True, gridcolor='LightGrey', tickfont=dict(family='Arial', color='black', size=11))
fig_5.update_yaxes(showgrid=True, gridcolor='LightGrey')
# hide legend
fig_5.layout.showlegend = False



# Unemployment Dataset
df = pd.read_csv(DATA_PATH.joinpath("unemployment_dash.csv"))

# Figure 6
fig_6 = px.line(df, x='date', y='index_value', labels={"index_value": "", 'age':'Ηλικιακή ομάδα'}, color='age',
               color_discrete_sequence=['rgb(102, 197, 204)', 'rgb(82,188,163)', 'rgb(29,105,150)'])
# automated figure modifications
update_figure(fig_6, 'Εξέλιξη ποσοστού ανεργίας')
fig_6.data[0].showlegend = True
# add markers to line
fig_6.data[0].update(mode='markers+lines')
# legend names
fig_6.data[0].name = 'Σύνολο'
fig_6.data[1].name = '25-74'
fig_6.data[2].name = '15-24'


# Current Account Dataset
df = pd.read_csv(DATA_PATH.joinpath("current_account_dash.csv"))

# Figure 7
fig_7 = px.bar(df, x='TIME_PERIOD', y='OBS_VALUE', color='bop_item',
                   color_discrete_sequence=px.colors.qualitative.Set2,
                   labels= {'OBS_VALUE': 'Τιμή', 'bop_item': 'Κατηγορία', 'TIME_PERIOD':"Ημερομηνία"})
# automated figure modifications
update_figure(fig_7, '<span style="font-size: 15px;"> Ισοζύγιο τρεχουσών συναλλαγών (εκατ. ευρώ)</span>')
# fix date format
fig_7.update_xaxes(type='category')
# adjust bar chart width
for data in fig_7.data:
    data["width"] = 0.3


# XAE Dataset
df = pd.read_csv(DATA_PATH.joinpath("xae_dash.csv"))

# Figure 8
fig_8 = px.bar(df, x='year', y='value', color='klados', barmode='group',
                   color_discrete_sequence=px.colors.qualitative.Set2, text='value',
                   labels= {'value': 'Τιμή', 'klados': 'Κατηγορία', 'year':"Ημερομηνία"})
update_figure(fig_8, '<span style="font-size: 15px;">Ξένες άμεσες επενδύσεις (εκατ. ευρώ)</span>')
# adjust bar chart width
for data in fig_8.data:
    data["width"] = 0.3
# fix date format
fig_8.update_xaxes(type='category')
# text outside chart
fig_8.update_traces(textposition='inside')
# hover info modifications
fig_8.update_traces(
    hovertemplate="<br>".join(["%{y}"]))


""" LAYOUT CODE """


layout = html.Div(children=[
    html.Br(),
    dcc.Markdown('**ΟΙΚΟΝΟΜΙΚΕΣ ΕΞΕΛΙΞΕΙΣ & ΚΟΙΝΩΝΙΚΕΣ ΕΠΙΠΤΩΣΕΙΣ ΤΗΣ ΠΑΝΔΗΜΙΑΣ COVID-19 ΣΤΗΝ ΕΛΛΑΔΑ**', 
            style={'text-align': 'center', 
                   'font-family': 'arial',
                  'fontSize': 23,
                   'height' : '4%',
                'background-color': 'rgb(243,243,243)', 'border':'4px black solid'}),
    html.Br(),
    
    html.Div([
        html.Div(children=[
            html.H4('ΟΙΚΟΝΟΜΙΚΕΣ ΕΞΕΛΙΞΕΙΣ', style={'font-family': 'arial', 'fontSize': 22, 'textAlign': 'center' }),
            html.Br(),
            dcc.Textarea(value='Πως εξελίχθηκαν βασικά οικονομικά μεγεθη της οικονομίας όπως το ΑΕΠ, η ανεργία και ο πληθωρισμός. Ακόμη, απεικονίζονται το ισοζύγιο πληρωμών και οι ξένες άμεσες επενδύσεις, προκειμένου να εξεταστεί το σύνολο των οικονομικών συναλλαγών των Ελλήνων κατοίκων με τον υπόλοιπο κόσμο και η πρόθεση ξένων επενδυτών να αποκτήσουν διαρκές συμφέρον σε επιχειρήσεις της χώρας.', style={'font-family': 'arial', 'width': '100%', 'height': 5, 'textAlign': 'center', 'border':'none', 'resize': 'none'}),
            html.Br(),
            html.Br(),
            dcc.Graph(figure=fig, style= {'display':'inline-block', 'height': '100%', 'width': '50%'}),
            dcc.Graph(figure=fig_2, style= {'display':'inline-block', 'height': '100%', 'width': '50%'}),
            dcc.Graph(figure=fig_3, style= {'display':'inline-block', 'height': '100%', 'width': '50%'}),
            dcc.Graph(figure=fig_4, style= {'display':'inline-block', 'height': '100%', 'width': '50%'}),
            dcc.Graph(figure=fig_5, style= {'display':'inline-block', 'height': '100%', 'width': '50%'}),
            dcc.Graph(figure=fig_6, style= {'display':'inline-block', 'height': '100%', 'width': '50%'}),
            dcc.Graph(figure=fig_7, style= {'display':'inline-block', 'height': '100%', 'width': '50%'}),
            dcc.Graph(figure=fig_8, style= {'display':'inline-block', 'height': '100%', 'width': '50%'})
    ]),
        
]),

])
