from dash import html
from nav_bar import create_nav_bar

# creates the nutrition page
def create_nutrition_page():
    # inserting the nutrition page
    nutrition = html.Div([
        html.H3('Nutrition Factors', style= {'color':'darkblue', 'text-align':'center'}), 
        html.Iframe(id='map', srcDoc=open('nutrition_factors.html', 'r').read(), width='100%', height='600')],
        style = {'width': '50%', 'float': 'left'})
    
    # inserting the food page
    food = html.Div([
        html.H3('Grocery Stores and Farmer Market Distribution', style= {'color':'darkblue', 'text-align':'center'}), 
        html.Iframe(id='map', srcDoc=open('food_places.html', 'r').read(), width='100%', height='600')],
        style = {'margin-left': '50%'})
    
    layout = html.Div([
        create_nav_bar('Nutrition & Access to Health Data'),
        #html.H2('Nutrition & Access to Health Data', style= {'text-align':'center'}),
        nutrition,
        food,
    ])
    return layout

# creates the healthcare and insurance page
def create_healthcare_page():    
    layout = html.Div([
        create_nav_bar('Healthcare & Access to Care'),
        #html.H2('Healthcare & Access to Care Information', style= {'text-align':'center'}),
        html.Div([html.Iframe(id='map', srcDoc=open('healthcare_factors.html', 'r').read(), width='100%', height='600')])
    ])
    return layout

# creates the substance abuse page
def create_substance_page():    
    layout = html.Div([
        create_nav_bar('Binge Drinking & Smoking'),
        #html.H2('Binge Drinking & Smoking Information', style= {'text-align':'center'}),
        html.Div([html.Iframe(id='map', srcDoc=open('substance_factors.html', 'r').read(), width='100%', height='600')])
    ])
    return layout