
my_token = '6949064085:AAGPiPPJkBFVwrcZa6GbpBoUijLdMiM_ir4'
'''
import requests

response = requests.get('https://ubilling.net.ua/aerialalerts/')


print(f"Status code: {response.status_code}")
print("Data:")
print(response.json())
data = response.json()

kiyiv_status = data['states']['Київська область']['alertnow']

if kiyiv_status:
    print("Внимание! В Киевской области воздушная тревога ! ")
else:
    print("В Киевской области нету тревоги , все спокойно ")
'''