from ibm_watson import PersonalityInsightsV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from pathlib import Path
from os.path import join, dirname


authenticator = IAMAuthenticator('O3scp3HLHGiMK56gn2bxgx4chJoWZg_MSEANWL8-wdek')
personality_insights = PersonalityInsightsV3(
    version='2017-10-13',
    authenticator=authenticator
)

personality_insights.set_service_url('https://api.eu-gb.personality-insights.watson.cloud.ibm.com/instances/f1b658b9-0d36-4f21-993e-123430f02866')

# Ruta haciia la carpeta contenedora del archivo . txt
DIRECTORY_PATH = '/Users/lorenaspg1/profiles/'

# Simboliza los archivos que se van a enviar a Watson- ir añadiendo a la carpeta archivos.txt
files = ['profile.txt']

# Aqui se guardan los resultados HTTP Response de Watson
watson_responses = []

# Ejecuta la peticion a Watson y guarda los resultados en la lista profiles
def get_results():
    for file in files:
        with open(join(dirname(DIRECTORY_PATH), file)) as profile_txt:
            profile = personality_insights.profile(
                    profile_txt.read(),
                    accept="text/csv",
                    content_type='text/plain',
                    content_language='es',
                    accept_language='es',
                    raw_scores=True,
                    csv_headers=True,
                    consumption_preferences=True,
                ).get_result()
            watson_responses.append(profile)


get_results()

# Lista de CSV's devueta por Watson
csvs = []

# Obtenemos el contenido de la respuesta de Watson, el CSV en bytes
def get_response_content():
    for response in watson_responses:
        csvs.append(response.content)


get_response_content()

def create_csv():
    for i in range(0, len(csvs)):
        path = "./myCSV{}.csv".format(i)
        Path(path).touch()
        myFile = open(path, 'w')
        with myFile:
            myFile.write(csvs[i].decode())


create_csv()
