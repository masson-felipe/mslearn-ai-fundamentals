import urllib.request
import json

data = { "input_data": { "columns": [ "day", "mnth", "year", "season", "holiday", "weekday", "workingday", "weathersit", "temp", "atemp", "hum", "windspeed" ], "index": [0], "data": [[1,1,2025,2,0,1,1,2,0.3,0.3,0.3,0.3]] } }

body = str.encode(json.dumps(data))

url = '<url-endpoint>'
api_key = '<chave-api>'

if not api_key:
    raise Exception("⚠️ Uma chave deve ser fornecida para chamar o endpoint.")

# Cabeçalhos da requisição
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f'Bearer {api_key}'
}

# Cria e envia a requisição
req = urllib.request.Request(url, body, headers)

try:
    with urllib.request.urlopen(req) as response:
        result = response.read().decode('utf-8')
        print("✅ Resposta do endpoint:")
        print(result)

except urllib.error.HTTPError as error:
    print(f"❌ A requisição falhou com o código: {error.code}")
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))