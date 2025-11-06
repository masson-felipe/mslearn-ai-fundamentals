# **LAB 03: Análise de Sentimentos com Language Studio e Azure AI Speech**

Neste laboratório, exploramos dois dos principais serviços de Inteligência Artificial do Azure voltados para **linguagem natural e fala**: o **Azure AI Speech** e o **Language Studio (Análise de Sentimentos)**.

Esses serviços permitem criar aplicações que **ouvem, falam e entendem o significado de textos e áudios**, sendo amplamente utilizados em assistentes virtuais, chatbots, ferramentas de transcrição e sistemas de atendimento automatizado.

No meu relatório abaixo, você encontrará:

1. Laboratório: **Azure AI Speech**
2. Laboratório: **Language Studio (Análise de Sentimentos)**
3. Script: **Python consumindo a API do serviço “Azure AI Speech”**
4. Script: **Python consumindo a API do serviço “Language Studio (Análise de Sentimentos)”**

Os dois scripts criados são simples, mas demonstram como aplicações reais podem se comunicar automaticamente com os serviços de IA do Azure.

---

# **LAB 01: Azure AI Speech**

O **Azure AI Speech** é um serviço que converte **fala em texto** e **texto em fala** (Speech-to-Text e Text-to-Speech).
Ele é usado em soluções que precisam **transcrever reuniões, gerar legendas automáticas, transformar textos em narrações realistas** ou até permitir que **assistentes virtuais conversem em linguagem natural** com os usuários.

Neste laboratório, exploramos o **Azure AI Foundry**, uma plataforma integrada da Microsoft para criar e testar aplicações inteligentes, incluindo o Speech Playground, onde é possível experimentar o serviço de forma prática.

---

## **1. Criar um projeto no portal Azure AI Foundry**

1. No navegador, acesse o portal [Azure AI Foundry](https://ai.azure.com) e entre com suas credenciais da Azure.
2. Feche quaisquer dicas ou painéis de ajuda abertos automaticamente e volte à página inicial.
3. Role até o final da página e selecione o bloco **Explore Azure AI Services**.
4. Na página de serviços, clique em **Speech**.
5. Em seguida, selecione **Go to Speech playground**.
6. Crie um novo projeto com as seguintes configurações:

   * **Project name:** nome válido de sua escolha
   * **Subscription:** sua assinatura Azure
   * **Resource group:** selecione ou crie um grupo de recursos
   * **Region:** East US
   * **Resource type:** selecione **Azure AI Foundry** e crie um recurso válido
7. Clique em **Create** e aguarde a criação do projeto.
8. Após a criação, você será redirecionado ao **Speech Playground**, uma interface para testar os recursos do Azure AI Speech.

![](steps/Pasted%20image%2020251027032231.png)

---

## **2. Explorando o Speech-to-Text (fala para texto)**

1. Utilize o arquivo de áudio `WhatAICanDo.m4a`.
2. No portal do Azure AI Foundry, acesse o **Speech Playground** e selecione a aba **Speech to text** → **Real-time transcription**.
3. Clique em **Upload files** e envie o arquivo `WhatAICanDo.m4a`.
4. O serviço processará o áudio e exibirá **a transcrição em tempo real**.
   * É possível ouvir a gravação enquanto o texto é gerado.
5. Revise o resultado na seção **Output → Text**, onde estará o texto transcrito automaticamente.

![](steps/Pasted%20image%2020251027032642.png)

---

## **3. Script: Consumindo a API do serviço “Azure AI Speech”**

Desenvolvi  um script simples em Python (`transcrever_arquivo.py`) para simular uma aplicação consumindo diretamente a API do Azure AI Speech.

Em um cenário real, o script deve considerar:

* **Entrada dinâmica:** o áudio pode vir de um microfone, upload do usuário ou arquivo externo.
* **Segurança:** a **API Key** e a **região** devem ser armazenadas em um arquivo `.env`.

### Execução do script:

```bash
python transcrever_arquivo.py
```

Durante a execução, o script envia o arquivo de áudio para a API e salva os resultados em dois arquivos:

* `transcricao.txt` → contém o texto transcrito.
* `transcricao.json` → contém dados estruturados retornados pela API.

Exemplo da execução:
![](steps/Pasted%20image%2020251027041238.png)

O teste foi realizado com o arquivo `WhatAICanDo.m4a`, disponível na pasta `storage/`, onde também se encontram os resultados gerados.

---

# **LAB 02: Language Studio (Análise de Sentimentos)**

O **Language Studio** faz parte do **Azure AI Language Service**, um conjunto de ferramentas para processamento de linguagem natural (NLP).
Ele é capaz de **analisar sentimentos, extrair opiniões, classificar textos e detectar entidades**, auxiliando empresas a entender o tom emocional de mensagens, e-mails ou avaliações de clientes.

Neste laboratório, o foco é a **Análise de Sentimentos (Sentiment Analysis)**, que identifica se um texto possui **polaridade positiva, negativa, neutra ou mista**.

---

## **1. Criar um recurso “Language Service”**

1. No [portal Azure](https://portal.azure.com), crie um novo recurso do tipo **Language Service**.
2. Configure-o com:

   * **Subscription:** sua assinatura Azure
   * **Resource group:** selecione ou crie um grupo
   * **Region:** East US
   * **Pricing tier:** Standard S0
3. Aguarde o provisionamento do serviço.

![](steps/Pasted%20image%2020251028001224.png)

---

## **2. Acessar o Language Studio**

1. Vá até [https://language.cognitive.azure.com/home](https://language.cognitive.azure.com/home).
2. Faça login com a conta vinculada à assinatura da Azure.
3. Conecte o recurso **Language Service** criado anteriormente.

---

## **3. Executar a Análise de Sentimentos**

1. No menu lateral, selecione **Classify Text → Analyze sentiment and mine opinions**.
2. Será aberto o **playground interativo** do serviço, onde é possível testar manualmente a API.

![](steps/Pasted%20image%2020251028002423.png)

3. Insira textos de exemplo para analisar, como avaliações de produtos, mensagens ou comentários.
4. Clique em **Run** para processar o texto.
5. O resultado exibirá:

   * **Sentiment geral:** positivo, negativo, neutro ou misto;
   * **Probabilidades (confidence scores)** para cada categoria;
   * **Opiniões detectadas**, como sentimentos sobre entidades específicas.

![](steps/Pasted%20image%2020251028003141.png)

---

## **4. Script: Consumindo a API do serviço “Language Studio (Análise de Sentimentos)”**

Foi desenvolvido um script Python (`analisar_sentimento.py`) que consome a API de Análise de Sentimentos do Azure.

Em um caso de uso real, recomenda-se:

* **Entrada dinâmica:** os textos podem vir de usuários ou coleta automática (por exemplo, web scrapping de avaliações de sites).
* **Segurança:** armazenar **URL** e **API Key** no arquivo `.env`.

### ▶️ Execução do script:

```bash
python analisar_sentimento.py
```

O script no momento envia quatro textos fixos para a API e salva os resultados em formato JSON na pasta:

```
storage/sentimento_resultado.json
```
Exemplo de execução:

![](steps/Pasted%20image%2020251028004058.png)

O resultado inclui a classificação de sentimento de cada texto, juntamente com os **níveis de confiança e opiniões extraídas**.

---

# **Conclusão**

Com esses dois laboratórios, foi possível compreender o potencial dos serviços de **Azure AI Speech** e **Language Studio** dentro do ecossistema Azure AI.

* O **Speech Service** demonstrou como é simples transformar áudio em texto, possibilitando aplicações de acessibilidade, legendagem automática e análise de reuniões.
* O **Language Studio** evidenciou o poder do **processamento de linguagem natural**, permitindo identificar sentimentos e extrair percepções de grandes volumes de texto.

Ambos os serviços são altamente integráveis via API, permitindo o desenvolvimento de **aplicações inteligentes, acessíveis e automatizadas**, que combinam fala e entendimento de linguagem natural, pilares da Inteligência Artificial moderna.

---