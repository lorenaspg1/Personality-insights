from ibm_watson import PersonalityInsightsV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import csv

from pathlib import Path


authenticator = IAMAuthenticator('O3scp3HLHGiMK56gn2bxgx4chJoWZg_MSEANWL8-wdek')
personality_insights = PersonalityInsightsV3(
    version='2017-10-13',
    authenticator=authenticator
)

personality_insights.set_service_url('https://api.eu-gb.personality-insights.watson.cloud.ibm.com/instances/f1b658b9-0d36-4f21-993e-123430f02866')

with open('/Users/lorenaspg1/profile.txt') as profile_txt:
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
#print(json.dumps(profile, indent=2))
print("test")
print(type(profile))
print(profile.content)
responseCsv = profile.content

Path('./myCSV.csv').touch()

#csvProcesado = csv.reader(responseCsv)
#print('csvProcesado: ')
#print(csvProcesado)

myFile = open('./myCSV.csv', 'w')
with myFile:
    writer = csv.writer(myFile)

print('written')


#with open('./myCSV.csv') as File:
 #   writer = csv.writer(File)

