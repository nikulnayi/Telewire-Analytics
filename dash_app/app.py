import pandas as pd
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
import dash 
import os

# Get the path of the current file
file_path = os.path.abspath(__file__)

# Get the path of the root directory
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(file_path)))
COVID_IMG = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTeqOxnyNX_UCarYAKSkIsY7CWQZlBzULPyMg&usqp=CAU"

data_file_path = "\\TBC-AIP-2023-A7_Telewire-Analytics\\data\\raw\\data.csv"

data = (
    pd.read_csv(root_dir+data_file_path,encoding='latin1')
)



app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
app.title = "Telewire Analytics"

############################## navigation bar ################################

navbar = dbc.Navbar( id = 'navbar', children = [


    html.A(
    dbc.Row([
        dbc.Col(html.Img(src = COVID_IMG, height = "80px")),
        dbc.Col(
            dbc.NavbarBrand("Cell Tower Anomaly Detection", style = {'color':'black', 'fontSize':'25px','fontFamily':'Times New Roman'}
                            )

            )


        ],align = "center",
        ),
    href = '/'
    ),
    
                dbc.Row(
            [
        dbc.Col( 
            dbc.Button(id = 'button', children = "Team Members", color = "primary", className = 'ml-auto', href = '/')

            )        
    ],

     className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
)
    # dbc.Button(id = 'button', children = "Support Us", color = "primary", className = 'ml-auto', href = '/')


    ])
app.layout = html.Div(id='parent', children=[navbar])

if __name__ == "__main__":
    app.run_server(debug=True)