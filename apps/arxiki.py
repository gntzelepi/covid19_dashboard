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
        hovermode="x unified",
    legend=dict(
        title=None, orientation="h", y=1, yanchor="bottom", x=0.5, xanchor="center"))
    traces = figure.update_traces(hovertemplate=None)
    return figure


"""  DATASETS AND FIGURES """

# Dataset 1 including covid cases and deaths
df = pd.read_csv(DATA_PATH.joinpath("owid-covid-data.csv"))
# locate greece in Dataset 1
only_gr = df.loc[df.location=='Greece']
# Figure 1
fig = px.bar(only_gr, y='new_cases', x='date', 
      labels= {'new_cases': 'Αριθμός κρουσμάτων', 'date': 'Ημερομηνία'}, color_discrete_sequence=['rgb(102, 197, 204)'])
# automated Figure 1 modifications
update_figure(fig, 'Ημερήσια κρούσματα COVID-19')


# dataset is the same, so I'm only creating Figure 2
fig_2 = px.bar(only_gr, y='new_deaths', x='date', color_discrete_sequence=['rgb(102, 197, 204)'],
      labels= {'new_deaths': 'Αριθμός Θανάτων', 'date': 'Date'})
# automated figure 2 modifications
update_figure(fig_2,'Ημερήσιοι θάνατοι από COVID-19')


# Dataset 2 including icu admissions
icu_df = pd.read_csv(DATA_PATH.joinpath('icu.csv'))
# rename dataset column
icu_df = icu_df.rename(columns={'Unnamed: 0': 'Date'})
# convert dataset column format to datetime
icu_df['Date'] = pd.to_datetime(icu_df['Date'], dayfirst = True)
# Figure 3 
fig_3 = px.line(x=icu_df['Date'], y=icu_df['���'],
             labels=dict(x='Date', y=""), color_discrete_sequence=['rgb(136,204,238)'])
# automated figure 3 modifications
update_figure(fig_3, 'Εξέλιξη εισαγωγών ΜΕΘ')


# Dataset 3 including tests
tests_df = pd.read_csv(DATA_PATH.joinpath('tests.csv'))
# convert dataset column format to datetime
tests_df['Ημερομηνία'] = pd.to_datetime(tests_df['Ημερομηνία'], dayfirst = True)


# dataset is the same so I am just making the basic Figure 5
fig_5 = px.line(tests_df, x='Ημερομηνία', y=['Θετικότητα ημέρας_1', 'Θετικότητα ΜΟ,  SUM'], 
                       labels={'Θετικότητα ημέρας_1': "", 'value': "Αριθμός εμβολιασμών"}, 
                color_discrete_sequence=['rgb(102, 197, 204)', 'rgb(0, 150, 100)'])
update_figure(fig_5, 'Ποσοστό θετικότητας (ανά ημέρα & μέσος όρος 7 ημερών)')
# legend line names
fig_5['data'][0]['name']='Θετικότητα ημέρας'
fig_5['data'][1]['name']= 'Θετικότητα (μ.ο. 7 ημερών)'
#specific legend position
fig_5.update_layout(yaxis=dict(
    tickformat = '%.format.%3f'),
    legend=dict(
    yanchor="top",
    y=1.05,
    xanchor="center",
    x=0.50
))


# Dataset 4 including vaccinations
vaccinations = pd.read_csv(DATA_PATH.joinpath('vaccinations.csv'), low_memory=False)
# convert dataset column format to datetime
vaccinations['Ημερομηνία'] = pd.to_datetime(vaccinations['Ημερομηνία'], dayfirst = True)
# Figure 6
fig_6 = px.bar(vaccinations, x='Ημερομηνία', y=['1η δόση (ημέρας)', '2η δόση (ημέρας)'], 
               labels = {'Ημερομηνία': 'Date', '1η δόση (ημέρας)': '1st Dose', '2η δόση (ημέρας)': '2nd Dose', 'value': ''},
              color_discrete_sequence=['rgb(0, 150, 300)', 'rgb(148,200,500)'])
# add 7-week average trace
fig_6.add_trace(go.Scatter(x=vaccinations["Ημερομηνία"], y=vaccinations["m.o. week"], mode='lines', marker=dict(color='rgb(208,100,700)')))
# automated figure update
update_figure(fig_6, 'Ημερήσιοι εμβολιασμοί')
# more modifications
fig_6.data[2].name = 'Μέσος όρος 7 ημερών'
#specific legend position
fig_6.update_layout(legend=dict(
    yanchor="top",
    y=1.05,
    xanchor="center",
    x=0.50
))



""" LAYOUT """

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
            html.H4('ΕΞΕΛΙΞΗ ΤΗΣ ΠΑΝΔΗΜΙΑΣ ΣΤΗΝ ΕΛΛΑΔΑ', style={'resize': 'none','font-family': 'arial', 'fontSize': 22, 'textAlign': 'center' }),
            html.Br(),
            dcc.Textarea(value='Η εξέλιξη της πανδημίας στη χώρα, συμπεριλαμβανομένων των κρουσμάτων, θανάτων νοσούντων με COVID-19, εισαγωγών σε ΜΕΘ, εμβολιασμών και θετικότητας των τεστ.', style={'font-family': 'arial', 'width': '100%', 'height': 5, 'textAlign': 'center', 'border':'none'}),
            html.Br(),
            html.Br(),
            dcc.Graph(figure=fig, style= {'display':'inline-block', 'height': '100%', 'width': '50%'}),
            dcc.Graph(figure=fig_2, style= {'display':'inline-block', 'height': '100%', 'width': '50%'}),
            dcc.Graph(figure=fig_3, style= {'display':'inline-block','height': '100%', 'width': '50%'}),
            dcc.Graph(figure=fig_5, style= {'display':'inline-block', 'height': '100%', 'width': '50%'}),
            dcc.Graph(figure=fig_6, style= {'height': '50%', 'width': '50%', 'margin': '0 auto', 'padding': '20px'}),

    ]),
        
]),

])



