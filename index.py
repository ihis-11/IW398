from dash import html, dcc
from app import app
from dash.dependencies import Input, Output
from cancer_page import create_colorectal_page, create_lung_page, create_oral_page, create_pancreas_page, create_all_page
from social_factors_pages import create_nutrition_page, create_substance_page, create_healthcare_page
from diabetes_page import create_diabetes_page, create_obesity_page, create_physical_inactivity_page

server = app.server # server for the app
app.config.suppress_callback_exceptions = True # to avoid the app crashing when there is a callback problem

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/diabetes':
        return create_diabetes_page()
    if pathname == '/pancreas':
        return create_pancreas_page()
    if pathname == '/oral':
        return create_oral_page()
    if pathname == '/lung':
        return create_lung_page()
    if pathname == '/colorectal':
        return create_colorectal_page()
    if pathname == '/nutrition':
        return create_nutrition_page()
    if pathname == '/healthcare':
        return create_healthcare_page()
    if pathname == '/substance':
        return create_substance_page()
    if pathname == '/obesity':
        return create_obesity_page()
    if pathname == '/physical':
        return create_physical_inactivity_page()
    else:
        return create_all_page()


if __name__ == '__main__':
    app.run_server(debug=True)