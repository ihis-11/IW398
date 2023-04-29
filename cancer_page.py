from dash import html
from nav_bar import create_nav_bar

def create_all_page():
    # inserting the incidence page
    incidence = html.Div([
        html.H3('Incidence Rate', style= {'color':'darkblue', 'text-align':'center'}), 
        html.Iframe(id='map', srcDoc=open('cancer_incidence.html', 'r').read(), width='100%', height='600')],
        style = {'width': '50%', 'float': 'left'})
    
    # inserting the mortality page
    mortality = html.Div([
        html.H3('Mortality Rate', style= {'color':'darkblue', 'text-align':'center'}),
        html.Iframe(id='map', srcDoc=open('cancer_mortality.html', 'r').read(), width='100%', height='600')],
        style = {'margin-left': '50%'})
    
    layout = html.Div([
        create_nav_bar('All Types of Cancer'),
        incidence,
        mortality])
    return layout

def create_colorectal_page():
    # inserting the incidence page
    incidence = html.Div([
        html.H3('Incidence Rate', style= {'color':'darkblue', 'text-align':'center'}), 
        html.Iframe(id='map', srcDoc=open('colorectal_incidence.html', 'r').read(), width='100%', height='600')],
        style = {'width': '50%', 'float': 'left'})
    
    # inserting the mortality page
    mortality = html.Div([
        html.H3('Mortality Rate', style= {'color':'darkblue', 'text-align':'center'}), 
        html.Iframe(id='map', srcDoc=open('colorectal_mortality.html', 'r').read(), width='100%', height='600')],
        style = {'margin-left': '50%'})
    
    layout = html.Div([
        create_nav_bar('Colorectal Cancer'),
        incidence,
        mortality])
    return layout

def create_lung_page():
    # inserting the incidence page
    incidence = html.Div([
        html.H3('Incidence Rate', style= {'color':'darkblue', 'text-align':'center'}), 
        html.Iframe(id='map', srcDoc=open('lung_incidence.html', 'r').read(), width='100%', height='600')],
        style = {'width': '50%', 'float': 'left'})
    
    # inserting the mortality page
    mortality = html.Div([
        html.H3('Mortality Rate', style= {'color':'darkblue', 'text-align':'center'}), 
        html.Iframe(id='map', srcDoc=open('lung_mortality.html', 'r').read(), width='100%', height='600')],
        style = {'margin-left': '50%'})
    
    layout = html.Div([
        create_nav_bar('Lung & Bronchus Cancer'),
        incidence,
        mortality])
    return layout

def create_oral_page():
    # inserting the incidence page
    incidence = html.Div([
        html.H3('Incidence Rate', style= {'color':'darkblue', 'text-align':'center'}), 
        html.Iframe(id='map', srcDoc=open('oral_incidence.html', 'r').read(), width='100%', height='600')],
        style = {'width': '50%', 'float': 'left'})
    
    # inserting the mortality page
    mortality = html.Div([
        html.H3('Mortality Rate', style= {'color':'darkblue', 'text-align':'center'}), 
        html.Iframe(id='map', srcDoc=open('oral_mortality.html', 'r').read(), width='100%', height='600')],
        style = {'margin-left': '50%'})
    
    layout = html.Div([
        create_nav_bar('Oral & Pharynx Cancer'),
        incidence,
        mortality])
    return layout

def create_pancreas_page():
    # inserting the incidence page
    incidence = html.Div([
        html.H3('Incidence Rate', style= {'color':'darkblue', 'text-align':'center'}), 
        html.Iframe(id='map', srcDoc=open('pancreas_incidence.html', 'r').read(), width='100%', height='600')],
        style = {'width': '50%', 'float': 'left'})
    
    # inserting the mortality page
    mortality = html.Div([
        html.H3('Mortality Rate', style= {'color':'darkblue', 'text-align':'center'}), 
        html.Iframe(id='map', srcDoc=open('pancreas_mortality.html', 'r').read(), width='100%', height='600')],
        style = {'margin-left': '50%'})
    
    layout = html.Div([
        create_nav_bar('Pancreatic Cancer'),
        incidence,
        mortality])
    return layout