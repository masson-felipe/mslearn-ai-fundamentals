import requests
import json
from datetime import datetime

subscription_key = "<chave-api>"
endpoint = "<url-endpoint>"

url = f"{endpoint}/computervision/imageanalysis:analyze"
params = {
    "features": "denseCaptions",
    "model-version": "latest",
    "language": "en",
    "api-version": "2024-02-01"
}

headers = {
    "Ocp-Apim-Subscription-Key": subscription_key,
    "Content-Type": "application/json"
}

body = {
    "url": "https://portal.vision.cognitive.azure.com/dist/assets/ImageTaggingSample0-276aeff6.jpg"
}

response = requests.post(url, headers=headers, params=params, json=body)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_filename = f"resultado_add_dense_captions_{timestamp}.json"

with open(output_filename, "w", encoding="utf-8") as f:
    json.dump(response.json(), f, indent=2, ensure_ascii=False)

print(f"✅ Resultado salvo em: {output_filename}")
print(f"Status code: {response.status_code}")

# Imagens para teste:
# https://portal.vision.cognitive.azure.com/dist/assets/DenseCaptioningSample3-eac10a5d.png
# https://portal.vision.cognitive.azure.com/dist/assets/DenseCaptioningSample0-2569b3c1.png
# https://portal.vision.cognitive.azure.com/dist/assets/ImageTaggingSample0-276aeff6.jpg