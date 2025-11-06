import json
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

LANGUAGE_KEY = "<language-key>"
LANGUAGE_ENDPOINT = "<language-endpoint>"

def authenticate_client():
    credential = AzureKeyCredential(LANGUAGE_KEY)
    client = TextAnalyticsClient(endpoint=LANGUAGE_ENDPOINT, credential=credential)
    return client

client = authenticate_client()

def analisar_sentimento(client, textos):
    result = client.analyze_sentiment(textos, show_opinion_mining=True)
    resultados = []

    for doc in result:
        if doc.is_error:
            resultados.append({"erro": doc.error})
            continue

        doc_info = {
            "documento": doc.sentiment,
            "pontuacao": {
                "positivo": doc.confidence_scores.positive,
                "neutro": doc.confidence_scores.neutral,
                "negativo": doc.confidence_scores.negative,
            },
            "frases": []
        }

        for sentenca in doc.sentences:
            frase_info = {
                "texto": sentenca.text,
                "sentimento": sentenca.sentiment,
                "pontuacao": {
                    "positivo": sentenca.confidence_scores.positive,
                    "neutro": sentenca.confidence_scores.neutral,
                    "negativo": sentenca.confidence_scores.negative,
                },
                "opinioes": []
            }

            for opiniao in sentenca.mined_opinions:
                alvo = opiniao.target
                avaliacao = [
                    {
                        "texto": a.text,
                        "sentimento": a.sentiment,
                        "positivo": a.confidence_scores.positive,
                        "negativo": a.confidence_scores.negative
                    } for a in opiniao.assessments
                ]

                frase_info["opinioes"].append({
                    "alvo": alvo.text,
                    "sentimento": alvo.sentiment,
                    "positivo": alvo.confidence_scores.positive,
                    "negativo": alvo.confidence_scores.negative,
                    "avaliacoes": avaliacao
                })

            doc_info["frases"].append(frase_info)

        resultados.append(doc_info)

    with open("sentimento_resultado.json", "w", encoding="utf-8") as f:
        json.dump(resultados, f, ensure_ascii=False, indent=2)

    print("✅ Resultado salvo em 'sentimento_resultado.json'")

# Texto de teste
textos = [
    "O atendimento foi excelente, mas a comida demorou muito para chegar.",
    "A limpeza do quarto estava horrível, mas a vista era linda.",
    "Tired hotel with poor service The Royal Hotel, London, United Kingdom 5/6/2018 This is an old hotel (has been around since 1950's) and the room furnishings are average - becoming a bit old now and require changing. The internet didn't work and had to come to one of their office rooms to check in for my flight home. The website says it's close to the British Museum, but it's too far to walk.",
    "I can describe my experience of this game in two words: 'TECHNOLOGY RECHARGED!' #bestdayever"
]

analisar_sentimento(client, textos)
