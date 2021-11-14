import requests
import os

rest_api_result = []

number_of_requests = int(os.environ['NUMBER_OF_REQUESTS'])
server_url = os.environ['SERVER_URL']

for i in range(0,number_of_requests):
    rest_api_result.append(eval(requests.get(server_url).content.decode("UTF-8")))


count = {}

for response in rest_api_result:
    if response['container_id'] in count.keys():
        count[response['container_id']] += 1
    else:
        count[response['container_id']] = 1

print("################################ TESTANDO PORCENTAGEM DE REQUISIÇÃO #############################################")
for i in count.keys():
    print(f"{i} com {(count[i]*100)/number_of_requests}% das requisições")
print(f"Total de requisições feitas: {number_of_requests}")
print("#################################################################################################################")