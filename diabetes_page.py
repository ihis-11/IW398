from dash import html
from nav_bar import create_nav_bar

def create_diabetes_page():
    # inserting the incidence page
    incidence = html.Div([
        html.H3('Male', style= {'color':'darkblue', 'text-align':'center'}), 
        html.Iframe(id='map', srcDoc=open('male_diabetes.html', 'r').read(), width='100%', height='600')],
        style = {'width': '50%', 'float': 'left'})
    
    # inserting the mortality page
    mortality = html.Div([
        html.H3('Female', style= {'color':'darkblue', 'text-align':'center'}),
        html.Iframe(id='map', srcDoc=open('female_diabetes.html', 'r').read(), width='100%', height='600')],
        style = {'margin-left': '50%'})
    
    layout = html.Div([
        create_nav_bar('Diagnosed Diabetes'),
        incidence,
        mortality])
    return layout

def create_obesity_page():
    # inserting the incidence page
    incidence = html.Div([
        html.H3('Male', style= {'color':'darkblue', 'text-align':'center'}), 
        html.Iframe(id='map', srcDoc=open('male_obesisty.html', 'r').read(), width='100%', height='600')],
        style = {'width': '50%', 'float': 'left'})
    
    # inserting the mortality page
    mortality = html.Div([
        html.H3('Female', style= {'color':'darkblue', 'text-align':'center'}),
        html.Iframe(id='map', srcDoc=open('female_obesisty.html', 'r').read(), width='100%', height='600')],
        style = {'margin-left': '50%'})
    
    layout = html.Div([
        create_nav_bar('Obesity'),
        incidence,
        mortality])
    return layout

def create_physical_inactivity_page():
    # inserting the incidence page
    incidence = html.Div([
        html.H3('Male', style= {'color':'darkblue', 'text-align':'center'}), 
        html.Iframe(id='map', srcDoc=open('male_physical_inactivity.html', 'r').read(), width='100%', height='600')],
        style = {'width': '50%', 'float': 'left'})
    
    # inserting the mortality page
    mortality = html.Div([
        html.H3('Female', style= {'color':'darkblue', 'text-align':'center'}),
        html.Iframe(id='map', srcDoc=open('female_physical_inactivity.html', 'r').read(), width='100%', height='600')],
        style = {'margin-left': '50%'})
    
    layout = html.Div([
        create_nav_bar('Physical Inactivity'),
        incidence,
        mortality])
    return layout