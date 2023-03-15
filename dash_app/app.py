import pandas as pd
from dash import Dash, dcc, html
from dash import dash_table
import dash_bootstrap_components as dbc
import dash 
import os

# Get the path of the current file
file_path = os.path.abspath(__file__)

# Get the path of the root directory
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(file_path)))
COVID_IMG = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTeqOxnyNX_UCarYAKSkIsY7CWQZlBzULPyMg&usqp=CAU"

data_file_path = "/TBC-AIP-2023-A7_Telewire-Analytics/data/raw/data.csv"

data = (
    pd.read_csv(root_dir+data_file_path,encoding='latin1')
)



app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
app.title = "Telewire Analytics"

############################## navigation bar ################################

navbar = dbc.Navbar( id = 'navbar', children = [


    html.A(
    dbc.Row([
        dbc.Col(html.Img(src = COVID_IMG, height = "120px")),
        dbc.Col(
            dbc.NavbarBrand("CELL TOWER ANOMALY DETECTOR", style = {'color':'black', 'fontSize':'35px','fontFamily':'Times New Roman'}
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
dash_body = [
    dbc.Row(
    [
    dash_table.DataTable(
        id='table',
        columns=[{'name': i, 'id': i} for i in data.columns],
        data=data.head(3).to_dict('records')
    )

    ]

    ),
    dbc.Row(
        [
            dbc.Col(html.Img(src="https://www.pngitem.com/pimgs/m/271-2719410_bar-chart-with-four-columns-showing-progression-cell.png",height = "240px")
            ),
            dbc.Col(html.Img(src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRG-gfguToHxv_fQOIN6m_CHbDVJ_XWEBtGNQ&usqp=CAU",height = "240px")
            ),
        ],
        className="second-row",
    ),

    dbc.Row(
        [
            # dbc.Col(html.Img(src="https://www.pngitem.com/pimgs/m/271-2719410_bar-chart-with-four-columns-showing-progression-cell.png",height = "240px")
            # ),
            dbc.Col(
                [dcc.Graph(
        figure={
            'data': [{'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Example'}],
            'layout': {
                'title': 'Example Graph'
            }
        }
    )
                ]
            ),
            dbc.Col(html.Img(src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQfRvEftey4G_8IINazNVP8uCQdSreRS1HCWQ&usqp=CAU",height = "240px")
            ),
        ],
        className="third-row",
    ),

    ]

# Define page layout
page_layout = html.Div(
    className="page_layout",
    children=[
        dbc.Col(navbar, className="header"),
        dbc.Col(dash_body, className="body"),
    ],
)


# Overall layout
app.layout = html.Div(id="main", className="app", children=page_layout) 

if __name__ == "__main__":
    app.run_server(debug=True)