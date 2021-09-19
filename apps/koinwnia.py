import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import pathlib
from app import app
from .utils import update_figure as update_fig, header_md, DEFAULT_STYLE

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

# figure update with specified margin
def update_figure(figure, title):
    return update_fig(figure, title, margin=dict(l=30, r=30, t=150, b=70))


""" DATASETS AND FIGURES CODE """


# Dataset 1
erwtisi_6 = pd.read_csv(DATA_PATH.joinpath("erwtisi_6_apr20.csv"))

# Figure 1
fig = px.bar(
    erwtisi_6,
    x="erwtisi",
    y="timi",
    labels={"apantisi": "", "timi": ""},
    color_discrete_sequence=px.colors.qualitative.Pastel,
    facet_col_wrap=1,
    facet_col="vathmos",
    facet_row_spacing=0.08,
    height=500,
)
# remove "=" from layout
for a in fig.layout.annotations:
    a.text = a.text.split("=")[1]
# automated figure modifications
update_figure(
    fig,
    "Την περίοδο αυτή, κάνετε τα παρακάτω<br>περισσότερο,το ίδιο, ή λιγότερο, σε σύγκριση με 3-4 μήνες πριν;",
)
# show percentage when hovering
fig.update_traces(hovertemplate="<br>".join(["%{y}%"]))


# Dataset 2
data = {"apantisi": ["1", "2", "3", "4", "5"], "timi": [14.4, 15, 33, 27.2, 10.4]}
erwtisi_5 = pd.DataFrame(data, columns=["apantisi", "timi"])

# Figure 2
fig_2 = px.bar(
    erwtisi_5,
    x="timi",
    y="apantisi",
    labels={"timi": "", "apantisi": ""},
    color_discrete_sequence=px.colors.qualitative.Antique,
)
# automated figure modifications
update_figure(
    fig_2,
    'Πόσο άγχος αισθάνεστε ότι έχετε σε μια κλίμακα 1-5;<br><span style="font-size: 11px;">(1=καθόλου άγχος έως 5=πάρα πολύ άγχος)</span>',
)
# hover info modifications & specific legend position
fig_2.update_layout(
    hovermode="y", legend=dict(yanchor="top", y=1.10, xanchor="center", x=0.47)
)
# show percentage when hovering
fig_2.update_traces(hovertemplate="<br>".join(["%{x}%"]))


# Dataset 3
erwtisi_11 = pd.read_csv(DATA_PATH.joinpath("erwtisi_11_sept20.csv"))

# Figure 3
fig_3 = px.bar(
    erwtisi_11,
    x="vathmos",
    y="erwtisi",
    color="apantisi",
    labels={"erwtisi": "", "vathmos": ""},
    color_discrete_sequence=px.colors.qualitative.Antique,
    text="vathmos",
)
update_figure(fig_3, "Ποιο από τα παρακάτω ισχύει για εσάς προσωπικά;")
# specific legend position and modifications
fig_3.update_layout(
    hovermode="y",
    legend=dict(yanchor="top", y=1.05, xanchor="center", x=0.47),
    autosize=True,
    width=900,
    height=800,
    margin=dict(l=300, r=100, b=50, t=100, pad=4),
)
# hover info & smaller text in graph
fig_3.update_traces(textfont_size=10, hovertemplate="<br>".join(["%{x}%"]))


# Dataset 4
erwtisi_19 = pd.read_csv(DATA_PATH.joinpath("erwtisi_19_sept20.csv"))

# Figure 4
fig_4 = px.bar(
    erwtisi_19,
    x="timi",
    y="apantisi",
    color="vathmos",
    labels={"apantisi": "", "timi": ""},
    color_discrete_sequence=px.colors.qualitative.Bold,
    facet_col_wrap=2,
    text="timi",
    facet_col="date",
    height=500,
    width=1000,
)
# remove "=" from layout
for a in fig_4.layout.annotations:
    a.text = a.text.split("=")[1]
# automated figure update
update_figure(
    fig_4,
    "Ποιες θα είναι οι μακροχρόνιες επιπτώσεις της πανδημίας; Θα επηρεάσει θετικά, ουδέτερα ή αρνητικά...",
)
# specific legend position
fig_4.update_layout(
    hovermode="y", legend=dict(yanchor="top", y=1.16, xanchor="center", x=0.47)
)
# smaller text in graph & hover info modifications
fig_4.update_traces(textfont_size=13, hovertemplate="<br>".join(["%{x}%"]))


# Dataset 5
erwtisi_13 = pd.read_csv(DATA_PATH.joinpath("erwtisi_13_dash.csv"))

# Figure 5
fig_5 = px.bar(
    erwtisi_13,
    x="apantisi",
    y="timi",
    labels={"timi": "", "apantisi": ""},
    color="apantisi",
    text="timi",
    color_discrete_sequence=px.colors.qualitative.Vivid,
)
update_figure(
    fig_5,
    "Σκέφτεστε να εμβολιαστείτε όταν θα είναι διαθέσιμο δωρεάν ένα εμβόλιο<br>κατά του νέου κορωνοϊού, εγκεκριμένο από<br>την Ε.Ε. και τις υγειονομικές αρχές της χώρας μας;",
)
# smaller text in graph & hover info modifications
fig_5.update_layout(margin=dict(l=30, r=30, t=200, b=70))
fig_5.update_traces(
    textfont_size=12, textposition="inside", hovertemplate="<br>".join(["%{y}%"])
)


# Dataset 6
erwtisi_14 = pd.read_csv(DATA_PATH.joinpath("erwtisi_14_dash.csv"))

# Figure 6
fig_6 = px.bar(
    erwtisi_14,
    x="timi",
    y="apantisi",
    labels={"apantisi": "", "timi": ""},
    color_discrete_sequence=px.colors.qualitative.Dark2,
    text="timi",
)
update_figure(
    fig_6,
    "Με ποια από τις παρακάτω προτάσεις συμφωνείτε περισσότερο;<br>(N=66.3%, Σίγουρα/Μάλλον Ναι)",
)
# smaller text in graph & hover info modifications
fig_6.update_traces(textfont_size=12, hovertemplate="<br>".join(["%{x}%"]))
# show x labels when hovering
fig_6.update_layout(hovermode="x")


# Dataset 7
erwtisi_4 = pd.read_csv(DATA_PATH.joinpath("erwtisi_4_jan21.csv"))

# Figure 7
fig_7 = px.bar(
    erwtisi_4,
    x="timi",
    y="apantisi",
    labels={"apantisi": "", "timi": ""},
    color_discrete_sequence=px.colors.qualitative.Pastel2,
    facet_col_wrap=1,
    text="timi",
    facet_col="date",
)
# remove "=" from layout
for a in fig_7.layout.annotations:
    a.text = a.text.split("=")[1]
# automated figure update
update_figure(
    fig_7,
    'Πόσο σημαντική είναι καθεμία από τις παρακάτω απειλές που<br>αντιμετωπίζει σήμερα η χώρα μας;<span style="font-size: 11px;"><br>(0=καθόλου σημαντική έως 10=πάρα πολύ σημαντική)</span>',
)
# specific legend position & hover info modifications
fig_7.update_layout(
    hovermode="y", legend=dict(yanchor="top", y=1.10, xanchor="center", x=0.47)
)
# smaller text in graph
fig_7.update_traces(textfont_size=12, hovertemplate="<br>".join(["%{x}"]))


# Dataset 8
erwtisi_7 = pd.read_csv(DATA_PATH.joinpath("erwtisi_7_jan21.csv"))

# Figure 8
fig_8 = px.bar(
    erwtisi_7,
    x="date",
    y="timi",
    labels={"timi": "", "date": ""},
    color_discrete_sequence=px.colors.qualitative.Plotly,
    text="timi",
    facet_col="apantisi",
    facet_col_wrap=4,
)
for a in fig_8.layout.annotations:
    a.text = a.text.split("=")[1]
# automated figure update
update_figure(
    fig_8,
    "Ποια είναι η κύρια πηγή ενημέρωσής σας αναφορικά<br>με την πανδημία του κορωνοϊού;",
)
# smaller text in grapha & hover info modifications
fig_8.update_traces(textfont_size=10, hovertemplate="<br>".join(["%{y}%"]))


# Dataset 9
erwtisi_7 = pd.read_csv(DATA_PATH.joinpath("erwtisi_7_march21.csv"))

# Figure 9
fig_9 = px.bar(
    erwtisi_7,
    x="timi",
    y="erwtisi",
    color="vathmos",
    labels={"erwtisi": "", "timi": ""},
    color_discrete_sequence=px.colors.qualitative.Pastel2,
    facet_col_wrap=1,
    text="timi",
    height=700,
    facet_col="date",
)
# remove "=" from layout
for a in fig_9.layout.annotations:
    a.text = a.text.split("=")[1]
# automated figure update
update_figure(fig_9, "Πόσο έχει αλλάξει η καθημερινή σας ζωή εξαιτίας της πανδημίας;")
# specific legend position & hover info modifications
fig_9.update_layout(
    hovermode="y", legend=dict(yanchor="top", y=1.10, xanchor="center", x=0.47)
)
# smaller text in graph
fig_9.update_traces(textfont_size=10, hovertemplate="<br>".join(["%{x}%"]))


# Dataset 10
erwtisi_14 = pd.read_csv(DATA_PATH.joinpath("erwtisi_14_march21.csv"))

# Figure 10
fig_10 = px.bar(
    erwtisi_14,
    x="timi",
    y="perifereia",
    color="apantisi",
    labels={"perifereia": "", "timi": ""},
    color_discrete_sequence=px.colors.qualitative.Vivid,
    text="timi",
)
# automated figure update
update_figure(
    fig_10, "Eίναι ικανοποιητικός ο ρυθμός εμβολιασμών μέχρι τώρα ή όχι; (NUTS 1)"
)
# hover info modifications
fig_10.update_layout(hovermode="y")
# smaller text in graph & hover info modifications
fig_10.update_traces(textfont_size=12, hovertemplate="<br>".join(["%{x}%"]))


# Dataset 11
erwtisi_1 = pd.read_csv(DATA_PATH.joinpath("erwtisi_1_dash.csv"))

# Figure 11
fig_11 = px.line(
    erwtisi_1,
    x="date",
    y="timi",
    color="apantisi",
    labels={"timi": ""},
    color_discrete_sequence=px.colors.qualitative.Pastel1,
)
# automated figure update
update_figure(
    fig_11,
    "Η χώρα μας αυτή την περίοδο κινείται προς τη σωστή ή προς τη λάθος κατεύθυνση;",
)
# add markets to lines
fig_11.data[0].update(mode="markers+lines")
fig_11.data[1].update(mode="markers+lines")
fig_11.data[2].update(mode="markers+lines")
fig_11.data[3].update(mode="markers+lines")
# show percentage when hovering
fig_11.update_traces(hovertemplate="<br>".join(["%{y}%"]))
fig_11.update_layout(font=dict(size=10))


# Dataset 12
erwtisi_2 = pd.read_csv(DATA_PATH.joinpath("erwtisi_2.csv"))
# Figure 12
fig_12 = px.bar(
    erwtisi_2,
    x="value",
    y="Unnamed: 0",
    color="date",
    labels={"value": "", "Unnamed: 0": ""},
    color_discrete_sequence=px.colors.qualitative.Bold,
    facet_col_wrap=2,
    height=1000,
    facet_col="date",
    text="value",
)
# remove "=" from layout
for a in fig_12.layout.annotations:
    a.text = a.text.split("=")[1]
# automated figure update
update_figure(
    fig_12,
    'Ποια συναισθήματα σας διακατέχουν πιο έντονα<br>σήμερα ως Έλληνα/Ελληνίδα;<span style="font-size: 11px;"> (πρώτη αναφορά)</span>',
)
# specific legend position & hover info modifications
fig_12.update_layout(
    hovermode="y", legend=dict(yanchor="top", y=1.06, xanchor="center", x=0.47)
)
# hover info modifications
fig_12.update_traces(textfont_size=12, hovertemplate="<br>".join(["%{x}%"]))


# Dataset 13
erwtisi_8 = pd.read_csv(DATA_PATH.joinpath("erwtisi_8_dash.csv"))

# Figure 13
fig_13 = px.bar(
    erwtisi_8,
    x="foreas",
    y="timi",
    color="date",
    labels={"timi": "", "foreas": ""},
    color_discrete_sequence=px.colors.qualitative.Pastel1,
    barmode="group",
)
# automated figure update
update_figure(
    fig_13,
    'Πόση εμπιστοσύνη έχετε στους παρακάτω,<br> αναφορικά με την αντιμετώπιση της πανδημίας του κορωνοϊού;<br></span><span style="font-size: 11px;">(μέσοι όροι, από 1=καθόλου εμπιστοσύνη έως 5=απόλυτη εμπιστοσύνη</span>)',
)
# smaller text in graph
fig_13.update_traces(textposition="outside", textfont_size=12)


# Dataset 14
erwtisi_19 = pd.read_csv(DATA_PATH.joinpath("erwtisi_19.csv"))
# Figure 14
fig_14 = px.bar(
    erwtisi_19,
    x="date",
    y="timi",
    color="apantisi",
    labels={"apantisi": "", "timi": ""},
    color_discrete_sequence=px.colors.qualitative.T10,
    barmode="group",
    text="timi",
)
# automated figure update
update_figure(
    fig_14, "Εσείς προσωπικά σκέφτεστε να εμβολιαστείτε ή όχι κατά του νέου κορωνοϊού;"
)
# smaller text in graph & hover info modifications
fig_14.update_traces(
    textposition="inside", textfont_size=12, hovertemplate="<br>".join(["%{y}%"])
)


# Dataset 15
erwtisi_32 = pd.read_csv(DATA_PATH.joinpath("erwtisi_32.csv"))
# Figure 15
fig_15 = px.bar(
    erwtisi_32,
    x="date",
    y="timi",
    color="apantisi",
    labels={"timi": "", "apantisi": "Απάντηση"},
    color_discrete_sequence=px.colors.qualitative.Safe,
    text="timi",
    facet_col_wrap=2,
    facet_col="apantisi",
    height=900,
)
# remove "=" from layout
for a in fig_15.layout.annotations:
    a.text = a.text.split("=")[1]
# automated figure update
update_figure(fig_15, "Ποια είναι η εργασιακή σας κατάσταση αυτή την περίοδο;")
# specific legend position
fig_15.update_layout(
    margin=dict(l=30, r=30, t=250, b=50),
    legend=dict(yanchor="top", y=1.2, xanchor="center", x=0.47),
)
# smaller text in graph & hover info modifications
fig_15.update_traces(textfont_size=12, hovertemplate="<br>".join(["%{y}%"]))


""" LAYOUT CODE """


layout = html.Div(
    children=[
        html.Br(),
        header_md,
        html.Br(),
        html.Div(
            [
                html.Div(
                    children=[
                        html.H4(
                            "ΚΟΙΝΩΝΙΚΕΣ ΕΠΙΠΤΩΣΕΙΣ & ΑΠΟΨΕΙΣ",
                            style={
                                "font-family": "arial",
                                "fontSize": 22,
                                "textAlign": "center",
                            },
                        ),
                        html.Br(),
                        html.Label(
                            [
                                "Επιλεγμένες ερωτήσεις 6 ερευνών του οργανισμού έρευνας και ανάλυσης «διαΝΕΟσις». Οι ",
                                html.A(
                                    "έρευνες",
                                    href="https://www.dianeosis.org/research/covid-19/",
                                ),
                                " αυτές διεξήχθησαν τον Απρίλιο, Σεπτέμβριο και Δεκέμβριο 2020, και Ιανουάριο, Μάρτιο και Μάιο 2021, οι οποίες απαρτίζονται από ερωτήσεις με κεντρικό άξονα την πανδημία. Κατά μέσο όρο, σε κάθε έρευνα έλαβαν μέρος 1.153 άτομα ηλικίας 17 ετών και άνω. Αθροίσματα που υπολείπονται του 100% ή υπερβαίνουν το 100%, οφείλονται σε στρογγυλοποιήσεις.",
                            ],
                            style={
                                "font-family": "arial",
                                "width": "100%",
                                "height": 50,
                                "textAlign": "center",
                                "border": "none",
                                "resize": "none",
                                "float": "center",
                            },
                        ),
                        html.Br(),
                        html.Br(),
                        html.H6(
                            "Πρώτο lockdown - Απρίλιος 2020",
                            style={
                                "font-family": "arial",
                                "textAlign": "center",
                                "text-decoration": "underline",
                            },
                        ),
                        dcc.Graph(figure=fig, style=DEFAULT_STYLE),
                        dcc.Graph(figure=fig_2, style=DEFAULT_STYLE),
                        html.H6(
                            "Λήξη πρώτου lockdown - Σεπτέμβριος 2020",
                            style={
                                "font-family": "arial",
                                "textAlign": "center",
                                "text-decoration": "underline",
                            },
                        ),
                        dcc.Graph(
                            figure=fig_3,
                            style={"height": "80%", "width": "60%", "margin": "0 auto"},
                        ),
                        dcc.Graph(
                            figure=fig_4,
                            style={"height": "80%", "width": "80%", "margin": "0 auto"},
                        ),
                        html.H6(
                            "Δεύτερο lockdown - Δεκέμβριος, Ιανουάριος & Μάρτιος 2021",
                            style={
                                "font-family": "arial",
                                "textAlign": "center",
                                "text-decoration": "underline",
                            },
                        ),
                        dcc.Graph(figure=fig_5, style=DEFAULT_STYLE),
                        dcc.Graph(figure=fig_6, style=DEFAULT_STYLE),
                        dcc.Graph(figure=fig_7, style=DEFAULT_STYLE),
                        dcc.Graph(figure=fig_8, style=DEFAULT_STYLE),
                        dcc.Graph(figure=fig_9, style=DEFAULT_STYLE),
                        dcc.Graph(figure=fig_10, style=DEFAULT_STYLE),
                        html.H6(
                            "Λήξη δεύτερου lockdown - Μάιος 2021",
                            style={
                                "font-family": "arial",
                                "textAlign": "center",
                                "text-decoration": "underline",
                            },
                        ),
                        dcc.Graph(figure=fig_11, style=DEFAULT_STYLE),
                        dcc.Graph(figure=fig_13, style=DEFAULT_STYLE),
                        dcc.Graph(figure=fig_15, style=DEFAULT_STYLE),
                        dcc.Graph(figure=fig_12, style=DEFAULT_STYLE),
                        dcc.Graph(
                            figure=fig_14,
                            style={"height": "80%", "width": "50%", "margin": "0 auto"},
                        ),
                    ]
                ),
            ]
        ),
    ]
)
