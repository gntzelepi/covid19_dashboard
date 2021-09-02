import dash_core_components as dcc

# automated figure update
def update_figure(figure, title, margin=None):
    layout = figure.update_layout(
        title_text=title,
        title_x=0.5,
        font=dict(
            size=12
        ),
        xaxis_title="",
        xaxis=dict(
            showticklabels=True,
            tickfont=dict(family="Arial", size=10, color="rgb(82,82,82)"),
        ),
        yaxis=dict(gridcolor="rgb(243,243,243)"),
        plot_bgcolor="white",
        hovermode="x unified",
        legend=dict(
            title=None, orientation="h", y=1, yanchor="bottom", x=0.5, xanchor="center"
        ),
        margin=margin,
    )
    traces = figure.update_traces(hovertemplate=None)
    return figure

# header for all pages
header_md = dcc.Markdown(
        "**ΟΙΚΟΝΟΜΙΚΕΣ ΕΞΕΛΙΞΕΙΣ & ΚΟΙΝΩΝΙΚΕΣ ΕΠΙΠΤΩΣΕΙΣ ΤΗΣ ΠΑΝΔΗΜΙΑΣ COVID-19 ΣΤΗΝ ΕΛΛΑΔΑ**",
        style={
            "text-align": "center",
            "font-family": "arial",
            "fontSize": 23,
            "height": "4%",
            "background-color": "rgb(243,243,243)",
            "border": "4px black solid",
        }
)

# default style for graph display in layout
DEFAULT_STYLE = {
    "display": "inline-block",
    "height": "100%",
    "width": "50%",
    "vertical-align": "top",
}
