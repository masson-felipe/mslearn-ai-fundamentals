import requests
import json
from datetime import datetime

subscription_key = "<chave-api>"
endpoint = "<url-endpoint>"

url = f"{endpoint}/computervision/imageanalysis:analyze"
params = {
    "features": "caption",
    "model-version": "latest",
    "language": "en",
    "api-version": "2024-02-01"
}

headers = {
    "Ocp-Apim-Subscription-Key": subscription_key,
    "Content-Type": "application/json"
}

body = {
    "url": "https://portal.vision.cognitive.azure.com/dist/assets/ImageCaptioningSample3-e03062c2.png"
}

response = requests.post(url, headers=headers, params=params, json=body)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_filename = f"resultado_add_captions_{timestamp}.json"

with open(output_filename, "w", encoding="utf-8") as f:
    json.dump(response.json(), f, indent=2, ensure_ascii=False)

print(f"✅ Resultado salvo em: {output_filename}")
print(f"Status code: {response.status_code}")

# Imagens para teste:
# https://learn.microsoft.com/azure/ai-services/computer-vision/media/quickstarts/presentation.png
# https://portal.vision.cognitive.azure.com/dist/assets/ImageCaptioningSample1-bbe41ac5.png
# https://portal.vision.cognitive.azure.com/dist/assets/ImageCaptioningSample3-e03062c2.png