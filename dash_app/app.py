import pandas as pd
from dash import Dash, dcc, html

data = (
    pd.read_csv("../data/raw/data.csv",encoding='latin1')
)
external_stylesheets = [
    {
        "href": (
            "https://codepen.io/chriddyp/pen/bWLwgP.css"
        ),
        "rel": "stylesheet",
    },
]

colors = {
    'background': '#F0F8FF',
    'text': '#00008B'
}

app = Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Telewire Analytics"


app.layout = html.Div(
    children=[
        html.H1(children="Cell Tower Anomaly Detection"),
        html.P(
            children=(
                "Analysis of Cell Tower Data"
                ),
                className="header-description",

            )
    ],
    className='header'
)

if __name__ == "__main__":
    app.run_server(debug=True)