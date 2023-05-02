import dash_bootstrap_components as dbc

def create_nav_bar(page):
    navbar = dbc.NavbarSimple(
        children=[
            dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label="Chronic Conditions",
                children=[
                    dbc.DropdownMenuItem("Diabetes", href='/diabetes'),
                    dbc.DropdownMenuItem("All Types of Cancers", href='/all'),
                    dbc.DropdownMenuItem("Colon & Rectum Cancer", href='/colorectal'),
                    dbc.DropdownMenuItem("Lung & Bronchus Cancer", href='/lung'),
                    dbc.DropdownMenuItem("Oral & Pharnyx Cancer", href='/oral'),
                    dbc.DropdownMenuItem("Pancreatic Cancer", href='/pancreas'),
                ],
            ),
            dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label="Causal Factors",
                children=[
                    dbc.DropdownMenuItem("Obesity", href='/obesity'),
                    dbc.DropdownMenuItem("Physical Inactivity", href='/physical'),
                    dbc.DropdownMenuItem("Nutrition & Food", href='/nutrition'),
                    dbc.DropdownMenuItem("Healthcare", href='/healthcare'),
                    dbc.DropdownMenuItem("Substance Abuse", href='/substance'),
                ],
            ),
        ],
        
        brand=page,
        sticky="top",
        color="darkblue", 
        dark=True,
    )

    return navbar