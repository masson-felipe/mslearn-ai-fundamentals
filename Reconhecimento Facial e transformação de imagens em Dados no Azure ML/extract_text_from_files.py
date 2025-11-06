import requests
import json
from datetime import datetime

subscription_key = "<chave-api>"
endpoint = "<url-endpoint>"

url = f"{endpoint}/computervision/imageanalysis:analyze"
params = {
    "features": "caption,read",
    "model-version": "latest",
    "language": "en",
    "api-version": "2024-02-01"
}

headers = {
    "Ocp-Apim-Subscription-Key": subscription_key,
    "Content-Type": "application/json"
}

body = {
    "url": "https://learn.microsoft.com/azure/ai-services/computer-vision/media/quickstarts/presentation.png"
}

response = requests.post(url, headers=headers, params=params, json=body)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_filename = f"resultado_{timestamp}.json"

with open(output_filename, "w", encoding="utf-8") as f:
    json.dump(response.json(), f, indent=2, ensure_ascii=False)

print(f"✅ Resultado salvo em: {output_filename}")
print(f"Status code: {response.status_code}")

# Imagens para teste:
# https://learn.microsoft.com/azure/ai-services/computer-vision/media/quickstarts/presentation.png
# https://portal.vision.cognitive.azure.com/dist/assets/OCR4-SocialSecurity-176168b6.jpg
# https://portal.vision.cognitive.azure.com/dist/assets/OCR5-NationalId-4b306816.jpg