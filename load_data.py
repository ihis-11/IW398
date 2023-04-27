import geopandas as gpd
import pandas as pd

# reading the incidence data for colon & rectum cancer 
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
    incidence_rates = pd.concat([richmond_incidence, bronx_incidence, ny_incidence, kings_incidence, queens_incidence], ignore_index = True)

    return incidence_rates

# reads the mortality data
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

# reading the incidence data for colon & rectum cancer 
def lung_incidence_data():
    bronx_incidence = pd.read_csv('datasets/cancer/lung/bronx/incidenceRate.csv')
    bronx_incidence.insert(0, "boro_code", [2.0]*8, True)

    kings_incidence = pd.read_csv('datasets/cancer/lung/kings/incidenceRate.csv')
    kings_incidence.insert(0, "boro_code", [3.0]*8, True)

    ny_incidence = pd.read_csv('datasets/cancer/lung/ny/incidenceRate.csv')
    ny_incidence.insert(0, "boro_code", [1.0]*8, True)

    queens_incidence = pd.read_csv('datasets/cancer/lung/queens/incidenceRate.csv')
    queens_incidence.insert(0, "boro_code", [4.0]*8, True)

    richmond_incidence = pd.read_csv('datasets/cancer/lung/richmond/incidenceRate.csv')
    richmond_incidence.insert(0, "boro_code", [5.0]*8, True)

    # stack all rates into one data frame
    incidence_rates = pd.concat([richmond_incidence, bronx_incidence, ny_incidence, kings_incidence, queens_incidence], ignore_index = True)

    return incidence_rates

# reads the mortality data
def lung_mortality_data():
    bronx = pd.read_csv('datasets/cancer/lung/bronx/mortalityRate.csv')
    bronx.insert(0, "boro_code", [2.0]*8, True)

    kings = pd.read_csv('datasets/cancer/lung/kings/mortalityRate.csv')
    kings.insert(0, "boro_code", [3.0]*8, True)

    ny = pd.read_csv('datasets/cancer/lung/ny/mortalityRate.csv')
    ny.insert(0, "boro_code", [1.0]*8, True)

    queens = pd.read_csv('datasets/cancer/lung/queens/mortalityRate.csv')
    queens.insert(0, "boro_code", [4.0]*8, True)

    richmond = pd.read_csv('datasets/cancer/lung/richmond/mortalityRate.csv')
    richmond.insert(0, "boro_code", [5.0]*8, True)

    # stack all rates into one data frame
    mortality_rates = pd.concat([richmond, bronx, ny, kings, queens], ignore_index = True)

    return mortality_rates

def nutrition_data():
    fruit_or_veggie = pd.read_csv('datasets/factors/nyc_statistics/fruit_or_veggie_consumption_2018.csv')
    fruit_or_veggie.insert(0, "boro_code", [2.0,3.0, 1.0, 4.0, 5.0], True)
    del fruit_or_veggie['County']

    obsesity = pd.read_csv('datasets/factors/nyc_statistics/obsesity_2018.csv')
    obsesity.insert(0, "boro_code", [2.0,3.0, 1.0, 4.0, 5.0], True)
    del obsesity['County']

    food_stamps = pd.read_csv('datasets/factors/nyc_statistics/food_stamp_2015_2019.csv')
    food_stamps.insert(0, "boro_code", [2.0,3.0, 1.0, 4.0, 5.0], True)
    del food_stamps['County']

    no_realiable_food = pd.read_csv('datasets/factors/nyc_statistics/no_realiable_food_source_2018.csv')
    no_realiable_food.insert(0, "boro_code", [2.0,3.0, 1.0, 4.0, 5.0], True)
    del no_realiable_food['County']

    return (no_realiable_food, food_stamps, fruit_or_veggie, obsesity)

def insurance_data():
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

    return (health_insurance, medicaid, regular_provider, medical_care)

def alc_smoking_data():
    drinking = pd.read_csv('datasets/factors/nyc_statistics/binge_drinking_2018.csv')
    drinking.insert(0, "boro_code", [2.0,3.0, 1.0, 4.0, 5.0], True)
    del drinking['County']

    smokers = pd.read_csv('datasets/factors/nyc_statistics/current_smokers_2018.csv')
    smokers.insert(0, "boro_code", [2.0,3.0, 1.0, 4.0, 5.0], True)
    del smokers['County']

    return (drinking, smokers)

# print(insurance_data())
# print(nutrition_data())
# print(colon_incidence_data())
# print(colon_mortality_data())

