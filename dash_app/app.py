import pandas as pd
from dash import Dash, dcc, html
from dash import dash_table
import dash_bootstrap_components as dbc
import os, io, base64
from dash.dependencies import Input, Output, State


# Get the path of the current file
file_path = os.path.abspath(__file__)
uploaded_data = None
# Get the path of the root directory
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(file_path)))
COVID_IMG = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTeqOxnyNX_UCarYAKSkIsY7CWQZlBzULPyMg&usqp=CAU"

data_file_path = "/TBC-AIP-2023-A7_Telewire-Analytics/data/raw/data.csv"

data = (
    pd.read_csv(root_dir+data_file_path,encoding='latin1')
)


count_usual = data[data['Unusual']==0]['Unusual'].count()
count_unusual = data[data['Unusual']==1]['Unusual'].count()
app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY,'https://codepen.io/chriddyp/pen/bWLwgP.css'])
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
    ### upload data here
    dbc.Row(
            [
        dbc.Col([
            # dbc.Button(id = 'button', children = "Team Members", color = "primary", className = 'ml-auto', href = '/'),
            
            html.Div(html.H4('Upload Data Here'),
                      style = {'fontWeight':'bold','family':'georgia','width':'100%','color':'#000000',}),
                      
            dcc.Upload(id ='upload-data', 
                       children = html.Button('Upload File'), 
                       style={'margin-right':'100px'}
                    #    mutiple= True
            ),
            # html.Div(id='output-data-upload')
            ])        
    ],

     className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
)
    # dbc.Button(id = 'button', children = "Support Us", color = "primary", className = 'ml-auto', href = '/')


    ])

# Count of Normal and Unusual
def data_for_cases(header, count_value):
    card_content = [
        dbc.CardHeader(header),

        dbc.CardBody(
            [
               dcc.Markdown( dangerously_allow_html = True,
                   children = ["{0}".format(count_value)])


                ]

            )
        ]

    return card_content

# csv data parsing
def data(contents, filename):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    try:
        if '.csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(io.StringIO(decoded.decode('ISO-8859-1')))
        elif '.xls' in filename:
            # Assume that the user uploaded an Excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])
    return df



dash_body = [
    # html.Div(id='output-data-upload'),

    dbc.Row([
        dbc.Col(dbc.Card(data_for_cases("Count of Normal",f'{count_usual}'), color = 'success',style = {'text-align':'center'}, inverse = True),xs = 12, sm = 12, md = 4, lg = 4, xl = 4, style = {'padding':'12px 12px 12px 12px'}),
        # dbc.Col(dbc.Card(data_for_cases("Recovered",f'{recovered:,}',f'{newrecovered:,}' ), color = 'success',style = {'text-align':'center'}, inverse = True),xs = 12, sm = 12, md = 4, lg = 4, xl = 4, style = {'padding':'12px 12px 12px 12px'}),
        dbc.Col(dbc.Card( data_for_cases("Count of Unusual",f'{count_unusual}'), color = 'danger',style = {'text-align':'center'}, inverse = True),xs = 12, sm = 12, md = 4, lg = 4, xl = 4, style = {'padding':'12px 12px 12px 12px'}),
        

        ],id='new_data'),

    html.Br(),
    html.Br(),
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
# App call for file upload
@app.callback(Output('new_data', 'children'),
              Input('upload-data', 'contents'),
              State('upload-data', 'filename'))
def update_output(contents, filename):
    if contents is not None:
        uploaded_data =  data(contents,filename)
        usual_cout = uploaded_data[uploaded_data['Unusual']==0]['Unusual'].count()
        Unusual_cout = uploaded_data[uploaded_data['Unusual']==1]['Unusual'].count()
        children =[
             dbc.Col(dbc.Card(data_for_cases("Count of Normal",f'{usual_cout}'), color = 'success',style = {'text-align':'center'}, inverse = True),xs = 12, sm = 12, md = 4, lg = 4, xl = 4, style = {'padding':'12px 12px 12px 12px'}),
            dbc.Col(dbc.Card( data_for_cases("Count of Unusual",f'{Unusual_cout}'), color = 'danger',style = {'text-align':'center'}, inverse = True),xs = 12, sm = 12, md = 4, lg = 4, xl = 4, style = {'padding':'12px 12px 12px 12px'}),
        
        ]
        return children
        
    else:
        return ''

# Overall layout
app.layout = html.Div(id="main", className="app", children=page_layout) 

if __name__ == "__main__":
    app.run_server(debug=True)