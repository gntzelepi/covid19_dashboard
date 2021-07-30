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

# Dataset 1
gdp_2 = pd.read_csv(DATA_PATH.joinpath("gdp_2.csv"))
# convert 'yeay' column format
gdp_2['year'] = pd.to_datetime(gdp_2['year'], format='%Y') 

# Figure 1
fig = px.bar(gdp_2, x='quarter', y='OBS_VALUE', color='year', barmode='group', text='metavoli',
                   color_discrete_sequence=px.colors.qualitative.Set2,
                   labels= {'value': 'Τιμή', 'OBS_VALUE':"", 'klados': 'Κατηγορία', 'year':"Ημερομηνία"})
# automated figure modifications
update_figure(fig, '<span style="font-size: 15px;"> ΑΕΠ (εκατ. ευρώ) & τριμηνιαία μεταβολή ανά έτος (%)</span>')
# legend names
fig.data[0].name = '2019'
fig.data[1].name = '2020'
fig.data[2].name = '2021'
# hover info modifications
fig.update_traces(
    hovertemplate="<br>".join(["%{y}"]))


# Dataset 2
expenditure = pd.read_csv(DATA_PATH.joinpath("expenditure.csv"))
# gibberish to greek
old = {'A;CLV_I15;P31_S14_S15;EL': 'Ιδιωτική κατανάλωση',
       'A;CLV_I15;P3_S13;EL': 'Δημόσια κατανάλωση',
       'A;CLV_I15;P5G;EL': 'Επενδυτικές δαπάνες',
       'A;CLV_I15;P6;EL': 'Εξαγωγές',
       'A;CLV_I15;P7;EL': 'Εισαγωγές'
}
expenditure = expenditure.replace(old)
# make index values numeric
expenditure['value'] = pd.to_numeric(expenditure.value) 
expenditure['date'] = pd.to_datetime(expenditure['date'], format='%Y')

# Figure 2
fig_2 = px.bar(expenditure, y='value', x='freq;unit;na_item;geo\TIME_PERIOD', color='date', barmode='group', text='metavoli',
                   color_discrete_sequence=px.colors.qualitative.Set2,
                   labels= {'index_value': 'Τιμή', 'date': 'Ημερομηνία', 'component': 'Κατηγορία', "value":""})

# automated figure modifications
update_figure(fig_2, '<span style="font-size: 15px;">Δαπάνες ανά κατηγορία & ετήσια μεταβολή (%)<br></span><span style="font-size: 12px;"> (2015=100)</span>')
# legend names
fig_2.data[0].name = '2019'
fig_2.data[1].name = '2020'
# hover info modifications
fig_2.update_traces(
    hovertemplate="<br>".join(["%{y}"]))


# Dataset 3
income = pd.read_csv(DATA_PATH.joinpath('income.csv'))
#gibberish to greek
old = {
    'B2A3G: Operating surplus and mixed income, gross': 'Aκαθάριστο λειτουργικό πλεόνασμα / μεικτό εισόδημα',
    'D1: Compensation of employees': 'Αμοιβές εξαρτημένης εργασίας',
    "D2X3: Taxes on production and imports less subsidies": 'Φόροι σε παραγωγή, εισαγωγές μείον επιδοτήσεις'
}
income = income.replace(old)
income['TIME_PERIOD'] = pd.to_datetime(income['TIME_PERIOD'], format='%Y')

# Figure 3
fig_3 = px.bar(income, y='OBS_VALUE', x='na_item', color='TIME_PERIOD', barmode='group',text='metavoli',
                   color_discrete_sequence=px.colors.qualitative.Pastel1,
                   labels= {'index_value': 'Τιμή', 'date': 'Ημερομηνία', 'component': 'Κατηγορία', 'OBS_VALUE':""})
# automated figure modifications
update_figure(fig_3, '<span style="font-size: 15px;">Εισοδήματα παραγωγικών συντελεστών & μεταβολή (%)<br></span><span style="font-size: 12px;">(εκατ. ευρώ σε τρέχουσες τιμές)</span>')
# legend names
fig_3.data[0].name = '2019'
fig_3.data[1].name = '2020'
# hover info modifications
fig_3.update_traces(
    hovertemplate="<br>".join(["%{y}"])
)

# Dataset 4
hicp = pd.read_csv(DATA_PATH.joinpath('hicp.csv'))
# locate greece
hicp_gr = hicp.loc[hicp['freq;unit;coicop;geo\TIME_PERIOD']=='M;RCH_A;CP00;EL']
# create new dataset format
hicp_gr = hicp_gr.set_index('freq;unit;coicop;geo\TIME_PERIOD').stack().reset_index()
drop_values = ['Unnamed: 0', 'country_code']
hicp_gr = hicp_gr[hicp_gr['level_1'].str.contains('|'.join(drop_values))==False]
hicp_gr.columns = ['country', 'date', 'index_value']
# convert object to float
hicp_gr['index_value'] = pd.to_numeric(hicp_gr.index_value) 

# Figure 4
fig_4 = px.line(hicp_gr, y='index_value', x='date', color_discrete_sequence=['rgb(102, 197, 204)'],
                labels= {'index_value': 'Τιμή', 'date': 'Ημερομηνία'})
# automated figure modifications
update_figure(fig_4, 'Εξέλιξη Εναρμονισμένου Δείκτη Τιμών Καταναλωτή (ετήσιος ρυθμός μεταβολής)')
# add markers to line
fig_4.data[0].update(mode='markers+lines')


# Dataset 5
components = pd.read_csv(DATA_PATH.joinpath('components.csv'))
# replace english values
old = {"Food and beverages" : "Φαγητό, αναψυκτικά",
       "Alcohol, tobacco" : "Αλκοόλ, καπνός",
       "Clothing, shoes": "Ρούχα, παπούτσια",
       "Housing, electricity, gas etc.": "Στέγαση, ηλεκτρικό ρεύμα κ.α.",
       "Household equipment": "Οικιακός εξοπλισμός",
       "Health": "Υγεία",
       "Transport": "Μεταφορές",
       "Communication": "Επικοινωνία",
       "Recreation and culture": "Ψυχαγωγία, πολιτισμός",
       "Education": "Εκπαίδευση",
       "Restaurants, hotels": "Εστιατόρια, ξενοδοχεία",
       "Miscellaneous": "Διάφορα"
      }
components = components.replace(old)

# Figure 5
fig_5 = px.bar(components, y='metavoli ', x='freq;unit;coicop;geo\TIME_PERIOD', 
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


# Dataset 6
unempl = pd.read_csv(DATA_PATH.joinpath("unemployment_age.csv"))
# change index
unempl = unempl.set_index('freq;s_adj;age;unit;sex;geo\TIME_PERIOD').stack().reset_index()
# drop values
drop_values = ['Unnamed: 0', 'country_code']
unempl = unempl[unempl['level_1'].str.contains('|'.join(drop_values))==False]
# re-format column names
unempl.columns = ['age', 'date', 'index_value']

# Figure 6
fig_6 = px.line(unempl, x='date', y='index_value', labels={"index_value": "", 'age':'Ηλικιακή ομάδα'}, color='age',
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


# Dataset 7
current_account = pd.read_csv(DATA_PATH.joinpath("current_account.csv"))
old = {"CA: Current account": "Ισοζύγιο τρεχουσών συναλλαγών",
       "G: Goods": "Ισοζύγιο αγαθών",
       "IN1: Primary income": "Ισοζύγιο πρωτογενών εισοδημάτων",
       "IN2: Secondary income": "Ισοζύγιο δευτερογενών εισοδημάτων",
       "S: Services": "Ισοζύγιο υπηρεσιών"
    
}
current_account = current_account.replace(old)

# Figure 7
fig_7 = px.bar(current_account, x='TIME_PERIOD', y='OBS_VALUE', color='bop_item',
                   color_discrete_sequence=px.colors.qualitative.Set2,
                   labels= {'OBS_VALUE': 'Τιμή', 'bop_item': 'Κατηγορία', 'TIME_PERIOD':"Ημερομηνία"})
# automated figure modifications
update_figure(fig_7, '<span style="font-size: 15px;"> Ισοζύγιο τρεχουσών συναλλαγών (εκατ. ευρώ)</span>')
# fix date format
fig_7.update_xaxes(type='category')
# adjust bar chart width
for data in fig_7.data:
    data["width"] = 0.3


# Dataset 8
xae = pd.read_csv(DATA_PATH.joinpath("xae.csv"))
old = {
    "metapoiisi": "Μεταποίηση",
    "xrimatopistotikes": "Χρηματοπιστωτικές δραστηριότητες",
    "akiniti": "Διαχείριση ακίνητης περιουσίας",
    "agorapolisies": "Ιδιωτικές αγοραπωλησίες ακινήτων"
}

xae = xae.replace(old)

# Figure 8
fig_8 = px.bar(xae, x='year', y='value', color='klados', barmode='group',
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
