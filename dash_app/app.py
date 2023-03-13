import pandas as pd
from dash import Dash, dcc, html
import os

# Get the path of the current file
file_path = os.path.abspath(__file__)

# Get the path of the root directory
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(file_path)))
data_file_path = "\\TBC-AIP-2023-A7_Telewire-Analytics\\data\\raw\\data.csv"
data = (
    pd.read_csv(root_dir+data_file_path,encoding='latin1')
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
                )

            )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)