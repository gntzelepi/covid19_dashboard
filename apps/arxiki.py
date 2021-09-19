import dash_core_components as dcc
import dash_html_components as html

import pathlib
from app import app
from .utils import header_md

layout = html.Div(
    children=[
        html.Br(),
        html.Div(
            [
                html.Div(
                    children=[
                        html.Br(),
                        dcc.Markdown(
                            "**COVID-19 Dashboard**",
                            style={
                                "font-family": "arial",
                                "textAlign": "center",
                                "text-decoration": "underline",
                                "fontSize": 25,
                            },
                        ),
                        html.Br(),
                        html.Br(),
                        dcc.Markdown(
                            """
                            Το ηλεκτρονικό αυτό ταμπλό, αποτελεί το προϊόν της διπλωματικής εργασίας της Τζελέπη Γεωργίας, 
                            η οποία φοιτά στο τμήμα Μηχανικών Χωροταξίας & Ανάπτυξης, της Πολυτεχνικής Σχολής του Αριστοτελείου 
                            Πανεπιστημίου Θεσσαλονίκης.
                            Η εργασία έχει τίτλο **"COVID-19 με γραφήματα: πως η ελληνική οικονομία & κοινωνία βιώνουν
                            την πανδημία"**. Απώτερος στόχος του παρόντος, συνιστά η αξιοποίησή του ως ένα δυναμικό εργαλείο πληροφόρησης
                            για το σχεδιασμό μελλοντικών πολιτικών και μέτρων, παρακολουθώντας ταυτοχρόνως τις πολύπλευρες εξελίξεις 
                            στη χώρα, εξελίξεις που αφορούν επιδημιολογικά/ιατρικά στοιχεία, βασικά οικονομικά μεγέθη, 
                            όπως επίσης, και αντιλήψεις των πολιτών.
                            """,
                            style={
                                "font-family": "arial",
                                "textAlign": "center",
                                "fontSize": 15,
                            },
                        ),
                        html.Br(),
                        html.Br(),
                        html.Label(
                            [
                                "Ο κώδικας του Dashboard καθώς και οι πηγές των γραφημάτων μπορούν να βρεθούν ",
                                html.A(
                                    "εδώ.",
                                    href="https://github.com/gntzelepi/covid19_dashboard",
                                ),
                            ],
                            style={
                                "font-family": "arial",
                                "width": "100%",
                                "height": 50,
                                "textAlign": "center",
                                "resize": "none",
                                "float": "center",
                            },
                        ),
                        html.Br(),
                        dcc.Markdown(
                            """
                                ***ΠΕΡΙΗΓΗΣΗ***     Πάνω αριστερά εντοπίζονται οι 4 σελίδες του ταμπλό. 
                                Καθεμία λέξη αντιπροσωπεύει και την αντίστοιχη θεματική σελίδα. 
                                """,
                            style={
                                "font-family": "arial",
                                "textAlign": "left",
                                "fontSize": 15,
                            },
                        ),
                        dcc.Markdown(
                            """
                                ***ΧΡΗΣΗ***     Τα γραφήματα των σελίδων είναι διαδραστικά. Συγκεκριμένα,
                                σέρνοντας απλά τον κέρσορα στο επιθυμητό γράφημα, εμφανίζονται εικονίδια
                                τα οποία δίνουν τη δυνατότητα αποθήκευσης του γραφήματος σε μορφή PNG, zoom in
                                και zoom out, επιλογής συγκεκριμένης περιοχής στο γράφημα, κ.α. Εναλλακτικά,
                                zoom in σε γράφημα μπορεί να γίνει επιλέγοντας με ένα κλικ, 
                                και ταυτοχρόνως, σέρνοντας τον κέρσορα, 
                                στην περιοχή επιθυμητής εστίασης. Zoom out γίνεται κάνοντας 
                                διπλό κλικ πάνω στο γράφημα. 
                                """,
                            style={
                                "font-family": "arial",
                                "textAlign": "left",
                                "fontSize": 15,
                            },
                        ),
                    ],
                ),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Div(
                    [
                        html.Img(
                            src=app.get_asset_url("auth.png"),
                            style={
                                "height": "6%",
                                "width": "6%",
                                "float": "left",
                                "position": "relative",
                            },
                        ),
                        html.Img(
                            src=app.get_asset_url("tmxa.png"),
                            style={
                                "height": "6%",
                                "width": "6%",
                                "float": "right",
                                "position": "relative",
                            },
                        ),
                    ],
                    style={"display": "inline-block"},
                ),
            ]
        ),
    ]
)
