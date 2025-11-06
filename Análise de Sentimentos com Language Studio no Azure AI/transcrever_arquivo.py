import os
import json
import azure.cognitiveservices.speech as speechsdk

SPEECH_KEY = "<speech-key>"
SPEECH_REGION = "<speech-region>"
AUDIO_FILE = "WhatAICanDo.wav" # Audio convertido para formato wav

def transcrever_audio(arquivo_audio):
    speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
    speech_config.speech_recognition_language = "en-US"

    audio_input = speechsdk.AudioConfig(filename=arquivo_audio)
    recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)

    print(f"🎧 Transcrevendo: {arquivo_audio} ...")

    result = recognizer.recognize_once_async().get()

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("✅ Texto reconhecido:")
        print(result.text)

        txt_file = "transcricao.txt"
        with open(txt_file, "w", encoding="utf-8") as f:
            f.write(result.text)
        print(f"💾 Texto salvo em: {txt_file}")

        json_file = "transcricao.json"
        try:
            data = json.loads(result.json)
            with open(json_file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"📦 JSON completo salvo em: {json_file}")
        except Exception as e:
            print("⚠️ Erro ao salvar JSON:", e)

    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("❌ Nenhuma fala reconhecida.")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation = result.cancellation_details
        print("⚠️ Cancelado:", cancellation.reason)
        print("Detalhes:", cancellation.error_details)

if __name__ == "__main__":
    transcrever_audio(AUDIO_FILE)
