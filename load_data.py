import geopandas as gpd
import pandas as pd

'''
ALL CANCERS DATA
'''

def cancer_incidence_data():
    bronx_incidence = pd.read_csv('datasets/cancer/new_cancers/bronx/newRate.csv')
    bronx_incidence.insert(0, "boro_code", [2.0]*10, True)

    kings_incidence = pd.read_csv('datasets/cancer/new_cancers/kings/newRate.csv')
    kings_incidence.insert(0, "boro_code", [3.0]*10, True)

    ny_incidence = pd.read_csv('datasets/cancer/new_cancers/ny/newRate.csv')
    ny_incidence.insert(0, "boro_code", [1.0]*10, True)

    queens_incidence = pd.read_csv('datasets/cancer/new_cancers/queens/newRate.csv')
    queens_incidence.insert(0, "boro_code", [4.0]*10, True)

    richmond_incidence = pd.read_csv('datasets/cancer/new_cancers/richmond/newRate.csv')
    richmond_incidence.insert(0, "boro_code", [5.0]*10, True)

    # stack all rates into one data frame
    incidence_rates = pd.concat([richmond_incidence, bronx_incidence, ny_incidence, 
                                 kings_incidence, queens_incidence], ignore_index = True)

    return incidence_rates

def cancer_mortality_data():
    bronx = pd.read_csv('datasets/cancer/cancer_death/bronx/mortalityRate.csv')
    bronx.insert(0, "boro_code", [2.0]*10, True)

    kings = pd.read_csv('datasets/cancer/cancer_death/kings/mortalityRate.csv')
    kings.insert(0, "boro_code", [3.0]*10, True)

    ny = pd.read_csv('datasets/cancer/cancer_death/ny/mortalityRate.csv')
    ny.insert(0, "boro_code", [1.0]*10, True)

    queens = pd.read_csv('datasets/cancer/cancer_death/queens/mortalityRate.csv')
    queens.insert(0, "boro_code", [4.0]*10, True)

    richmond = pd.read_csv('datasets/cancer/cancer_death/richmond/mortalityRate.csv')
    richmond.insert(0, "boro_code", [5.0]*10, True)

    # stack all rates into one data frame
    mortality_rates = pd.concat([richmond, bronx, ny, kings, queens], ignore_index = True)

    return mortality_rates

'''
COLON & RECTUM DATA
'''

def colon_incidence_data():
    bronx_incidence = pd.read_csv('datasets/cancer/colon/bronx/incidenceRate.csv')
    bronx_incidence.insert(0, "boro_code", [2.0]*8, True)

    kings_incidence = pd.read_csv('datasets/cancer/colon/kings/incidenceRate.csv')
    kings_incidence.insert(0, "boro_code", [3.0]*8, True)

    ny_incidence = pd.read_csv('datasets/cancer/colon/ny/incidenceRate.csv')
    ny_incidence.insert(0, "boro_code", [1.0]*8, True)

    queens_incidence = pd.read_csv('datasets/cancer/colon/queens/incidenceRate.csv')
    queens_incidence.insert(0, "boro_code", [4.0]*8, True)

    richmond_incidence = pd.read_csv('datasets/cancer/colon/richmond/incidenceRate.csv')
    richmond_incidence.insert(0, "boro_code", [5.0]*8, True)

    # stack all rates into one data frame
    incidence_rates = pd.concat([richmond_incidence, bronx_incidence, ny_incidence, 
                                 kings_incidence, queens_incidence], ignore_index = True)

    return incidence_rates

def colon_mortality_data():
    bronx = pd.read_csv('datasets/cancer/colon/bronx/mortalityRate.csv')
    bronx.insert(0, "boro_code", [2.0]*8, True)

    kings = pd.read_csv('datasets/cancer/colon/kings/mortalityRate.csv')
    kings.insert(0, "boro_code", [3.0]*8, True)

    ny = pd.read_csv('datasets/cancer/colon/ny/mortalityRate.csv')
    ny.insert(0, "boro_code", [1.0]*8, True)

    queens = pd.read_csv('datasets/cancer/colon/queens/mortalityRate.csv')
    queens.insert(0, "boro_code", [4.0]*8, True)

    richmond = pd.read_csv('datasets/cancer/colon/richmond/mortalityRate.csv')
    richmond.insert(0, "boro_code", [5.0]*8, True)

    # stack all rates into one data frame
    mortality_rates = pd.concat([richmond, bronx, ny, kings, queens], ignore_index = True)

    return mortality_rates

'''
LUNG & BRONCHUS CANCER DATA
'''

def lung_incidence_data():
    bronx_incidence = pd.read_csv('datasets/cancer/lung/bronx/incidenceRate.csv')
    bronx_incidence.insert(0, "boro_code", [2.0]*10, True)

    kings_incidence = pd.read_csv('datasets/cancer/lung/kings/incidenceRate.csv')
    kings_incidence.insert(0, "boro_code", [3.0]*10, True)

    ny_incidence = pd.read_csv('datasets/cancer/lung/ny/incidenceRate.csv')
    ny_incidence.insert(0, "boro_code", [1.0]*10, True)

    queens_incidence = pd.read_csv('datasets/cancer/lung/queens/incidenceRate.csv')
    queens_incidence.insert(0, "boro_code", [4.0]*10, True)

    richmond_incidence = pd.read_csv('datasets/cancer/lung/richmond/incidenceRate.csv')
    richmond_incidence.insert(0, "boro_code", [5.0]*10, True)

    incidence_rates = pd.concat([richmond_incidence, bronx_incidence, ny_incidence, 
                                 kings_incidence, queens_incidence], ignore_index = True)

    return incidence_rates


def lung_mortality_data():
    bronx = pd.read_csv('datasets/cancer/lung/bronx/mortalityRate.csv')
    bronx.insert(0, "boro_code", [2.0]*10, True)

    kings = pd.read_csv('datasets/cancer/lung/kings/mortalityRate.csv')
    kings.insert(0, "boro_code", [3.0]*10, True)

    ny = pd.read_csv('datasets/cancer/lung/ny/mortalityRate.csv')
    ny.insert(0, "boro_code", [1.0]*10, True)

    queens = pd.read_csv('datasets/cancer/lung/queens/mortalityRate.csv')
    queens.insert(0, "boro_code", [4.0]*10, True)

    richmond = pd.read_csv('datasets/cancer/lung/richmond/mortalityRate.csv')
    richmond.insert(0, "boro_code", [5.0]*10, True)

    # stack all rates into one data frame
    mortality_rates = pd.concat([richmond, bronx, ny, kings, queens], ignore_index = True)

    return mortality_rates

'''
ORAL & PHARYNX CANCER DATA
'''

def oral_incidence_data():
    bronx_incidence = pd.read_csv('datasets/cancer/oral/bronx/incidenceRate.csv')
    bronx_incidence.insert(0, "boro_code", [2.0]*10, True)

    kings_incidence = pd.read_csv('datasets/cancer/oral/kings/incidenceRate.csv')
    kings_incidence.insert(0, "boro_code", [3.0]*10, True)

    ny_incidence = pd.read_csv('datasets/cancer/oral/ny/incidenceRate.csv')
    ny_incidence.insert(0, "boro_code", [1.0]*10, True)

    queens_incidence = pd.read_csv('datasets/cancer/oral/queens/incidenceRate.csv')
    queens_incidence.insert(0, "boro_code", [4.0]*10, True)

    richmond_incidence = pd.read_csv('datasets/cancer/oral/richmond/incidenceRate.csv')
    richmond_incidence.insert(0, "boro_code", [5.0]*10, True)

    incidence_rates = pd.concat([richmond_incidence, bronx_incidence, ny_incidence, 
                                 kings_incidence, queens_incidence], ignore_index = True)

    return incidence_rates


def oral_mortality_data():
    bronx = pd.read_csv('datasets/cancer/oral/bronx/mortalityRate.csv')
    bronx.insert(0, "boro_code", [2.0]*10, True)

    kings = pd.read_csv('datasets/cancer/oral/kings/mortalityRate.csv')
    kings.insert(0, "boro_code", [3.0]*10, True)

    ny = pd.read_csv('datasets/cancer/oral/ny/mortalityRate.csv')
    ny.insert(0, "boro_code", [1.0]*10, True)

    queens = pd.read_csv('datasets/cancer/oral/queens/mortalityRate.csv')
    queens.insert(0, "boro_code", [4.0]*10, True)

    richmond = pd.read_csv('datasets/cancer/oral/richmond/mortalityRate.csv')
    richmond.insert(0, "boro_code", [5.0]*10, True)

    # stack all rates into one data frame
    mortality_rates = pd.concat([richmond, bronx, ny, kings, queens], ignore_index = True)

    return mortality_rates


'''
PANCREATIC CANCER DATA
'''

def pancreas_incidence_data():
    bronx_incidence = pd.read_csv('datasets/cancer/pancreas/bronx/incidenceRate.csv')
    bronx_incidence.insert(0, "boro_code", [2.0]*10, True)

    kings_incidence = pd.read_csv('datasets/cancer/pancreas/kings/incidenceRate.csv')
    kings_incidence.insert(0, "boro_code", [3.0]*10, True)

    ny_incidence = pd.read_csv('datasets/cancer/pancreas/ny/incidenceRate.csv')
    ny_incidence.insert(0, "boro_code", [1.0]*10, True)

    queens_incidence = pd.read_csv('datasets/cancer/pancreas/queens/incidenceRate.csv')
    queens_incidence.insert(0, "boro_code", [4.0]*10, True)

    richmond_incidence = pd.read_csv('datasets/cancer/pancreas/richmond/incidenceRate.csv')
    richmond_incidence.insert(0, "boro_code", [5.0]*10, True)

    incidence_rates = pd.concat([richmond_incidence, bronx_incidence, ny_incidence, 
                                 kings_incidence, queens_incidence], ignore_index = True)

    return incidence_rates

def pancreas_mortality_data():
    bronx = pd.read_csv('datasets/cancer/pancreas/bronx/mortalityRate.csv')
    bronx.insert(0, "boro_code", [2.0]*10, True)

    kings = pd.read_csv('datasets/cancer/pancreas/kings/mortalityRate.csv')
    kings.insert(0, "boro_code", [3.0]*10, True)

    ny = pd.read_csv('datasets/cancer/pancreas/ny/mortalityRate.csv')
    ny.insert(0, "boro_code", [1.0]*10, True)

    queens = pd.read_csv('datasets/cancer/pancreas/queens/mortalityRate.csv')
    queens.insert(0, "boro_code", [4.0]*10, True)

    richmond = pd.read_csv('datasets/cancer/pancreas/richmond/mortalityRate.csv')
    richmond.insert(0, "boro_code", [5.0]*10, True)

    # stack all rates into one data frame
    mortality_rates = pd.concat([richmond, bronx, ny, kings, queens], ignore_index = True)

    return mortality_rates

'''
SOCIO-ECONOMIC FACTORS DATA
'''

def nutrition_data():
    fruit_or_veggie = pd.read_csv('datasets/factors/nyc_statistics/fruit_or_veggie_consumption_2018.csv')
    fruit_or_veggie.insert(0, "boro_code", [2.0,3.0, 1.0, 4.0, 5.0], True)
    del fruit_or_veggie['County']

    obesity = pd.read_csv('datasets/factors/nyc_statistics/obsesity_2018.csv')
    obesity.insert(0, "boro_code", [2.0,3.0, 1.0, 4.0, 5.0], True)
    del obesity['County']

    food_stamps = pd.read_csv('datasets/factors/nyc_statistics/food_stamp_2015_2019.csv')
    food_stamps.insert(0, "boro_code", [2.0,3.0, 1.0, 4.0, 5.0], True)
    del food_stamps['County']

    no_realiable_food = pd.read_csv('datasets/factors/nyc_statistics/no_realiable_food_source_2018.csv')
    no_realiable_food.insert(0, "boro_code", [2.0,3.0, 1.0, 4.0, 5.0], True)
    del no_realiable_food['County']

    return (no_realiable_food, food_stamps, fruit_or_veggie, obesity)

def insurance_data():
    dental_visit = pd.read_csv('datasets/factors/nyc_statistics/dental_visit_2018.csv')
    dental_visit.insert(0, "boro_code", [2.0,3.0, 1.0, 4.0, 5.0], True)
    del dental_visit['County']

    health_insurance = pd.read_csv('datasets/factors/nyc_statistics/adults_health_insurance_2019.csv')
    health_insurance.insert(0, "boro_code", [2.0,3.0, 1.0, 4.0, 5.0], True)
    del health_insurance['County']

    medicaid = pd.read_csv('datasets/factors/nyc_statistics/medicaid_2015_2019.csv')
    medicaid.insert(0, "boro_code", [2.0,3.0, 1.0, 4.0, 5.0], True)
    del medicaid['County']

    medical_care = pd.read_csv('datasets/factors/nyc_statistics/no_medical_care.csv')
    medical_care.insert(0, "boro_code", [2.0,3.0, 1.0, 4.0, 5.0], True)
    del medical_care['County']

    regular_provider = pd.read_csv('datasets/factors/nyc_statistics/regular_health_care_provider.csv')
    regular_provider.insert(0, "boro_code", [2.0,3.0, 1.0, 4.0, 5.0], True)
    del regular_provider['County']

    return (health_insurance, medicaid, regular_provider, medical_care, dental_visit)

def alc_smoking_data():
    drinking = pd.read_csv('datasets/factors/nyc_statistics/binge_drinking_2018.csv')
    drinking.insert(0, "boro_code", [2.0,3.0, 1.0, 4.0, 5.0], True)
    del drinking['County']

    smokers = pd.read_csv('datasets/factors/nyc_statistics/current_smokers_2018.csv')
    smokers.insert(0, "boro_code", [2.0,3.0, 1.0, 4.0, 5.0], True)
    del smokers['County']

    return (drinking, smokers)
