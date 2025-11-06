# LAB 02: Trabalhando com Machine Learning na Prática no Azure ML

Neste laboratório, foram utilizados diversos recursos do **Azure AI Services**, explorando suas funcionalidades práticas para **visão computacional** e **análise de imagens**.

No meu relatório abaixo, você encontrará:

1. Laboratório: **Detectando rostos no Vision Studio**
2. Laboratório: **Extraindo texto de imagens (Extract text from images)**
3. Laboratório: **Adicionando legendas a imagens (Add Captions to Images)**
4. Laboratório: **Adicionando legendas densas a imagens (Add Dense Captions to Images)**
5. Script: **Python consumindo a API do serviço “Extract text from images”**
6. Script: **Python consumindo a API do serviço “Add Captions to Images”**
7. Script: **Python consumindo a API do serviço “Add Dense Captions to Images”**

Os três scripts criados são simples, mas ilustram como uma aplicação real pode se comunicar com os serviços de IA do Azure de forma automatizada.

---

# **LAB 01: Detectando rostos no Vision Studio**

Este laboratório explora o serviço **Azure AI Face**, que permite detectar rostos em imagens e identificar atributos faciais como expressão, presença de óculos, máscara, entre outros.

O objetivo é **configurar o recurso**, **enviar imagens de teste** e observar como o sistema localiza rostos e retorna coordenadas e metadados.

---

## 1. Criar um recurso Azure AI Services

1. No portal do Azure (`https://portal.azure.com`), clique em **+ Criar um recurso**.
2. Procure por **Azure AI Services** e inicie a criação do recurso.

   * **Assinatura (Subscription):** sua assinatura Azure.
   * **Grupo de recursos (Resource group):** selecione ou crie um novo grupo.
   * **Região (Region):** East US.
   * **Nível de preço (Pricing tier):** Standard S0.
   * Marque a caixa de confirmação dos termos de uso.
3. Clique em **Revisar + criar** e depois em **Criar**. Aguarde o término da implantação.

![](steps/Pasted%20image%2020251027005005.png)

---

## 2. Conectar o recurso ao Vision Studio

1. Em outra aba do navegador, acesse [Vision Studio](https://portal.vision.cognitive.azure.com).
2. Faça login com a mesma conta e diretório usados na criação do recurso.
3. Na página inicial do Vision Studio, selecione **View all resources**.
4. Marque o recurso criado anteriormente e clique em **Select as default resource**.
5. Feche a janela de configurações clicando no “x” no canto superior direito.

![](steps/Pasted%20image%2020251027005513.png)

---

## LAB 01: Detectar rostos no Vision Studio

1. No [Vision Studio](https://portal.vision.cognitive.azure.com), vá até a aba **Face** e selecione **Detect faces in an image**.
2. Aceite a política de uso do recurso.
3. Teste as imagens de exemplo disponíveis no serviço ou com imagens próprias.
   * Faça upload de uma imagem com rostos visíveis (ex: `face-detection/01/person-without-mask.png`).
5. O serviço processará a imagem e exibirá:

   * Retângulos de delimitação ao redor de cada rosto.
   * Atributos faciais, como expressão, orientação, óculos, máscara e qualidade de reconhecimento.
6. Visualize a aba **JSON** para ver o resultado completo, com IDs, coordenadas e níveis de confiança.
7. Repita o teste com imagens diferentes (iluminação, múltiplas pessoas, rostos parciais) para avaliar os limites do modelo.

![](steps/Pasted%20image%2020251027005647.png)

Foram feitos testes com as quatro imagens de exemplo disponíveis no serviço **Face Detection**.
Cada entrada e resultado estão salvos na pasta `face-detection`, contendo as imagens e os arquivos JSON correspondentes.

---

# **LAB 02: Extract Text from Images**

O serviço **Extract Text from Images (OCR)** faz parte do **Azure AI Vision** e permite detectar e interpretar texto embutido em imagens. Essa funcionalidade é amplamente usada para **digitalização de documentos**, **leitura de placas**, e **extração automática de dados**.

![](steps/Pasted%20image%2020251027014156.png)

Com o mesmo recurso criado no laboratório 01, alteramos o serviço para **Extract Text from Images**.

Foram feitos testes via interface do Azure com as três imagens de exemplo disponíveis no serviço.
Os resultados estão salvos na pasta `extract-text`, contendo a imagem de entrada e o arquivo JSON de saída de cada teste.

Além disso, foi criado um script Python (`extract_text_from_files.py`) que simula uma aplicação real consumindo a API desse serviço.

Em um caso de uso real, seria necessário adaptar algumas coisas no script:

* O **payload** ser dinâmico, recebendo imagens enviadas pelos usuários.
* A **URL** e a **API Key** armazenadas em um arquivo `.env` para segurança.

Para executar o script, voce deve gerar a URL e API Key, alterar no arquivo e executar o script:

```bash
python extract_text_from_files.py
```

O script salva os resultados em arquivos JSON dentro da pasta `storage/result-scripts`, com o prefixo `resultado_`.

---

# **LAB 03: Add Captions to Images**

O serviço **Add Captions to Images** gera uma **legenda descritiva em linguagem natural** (frase legível por humanos) que resume o conteúdo principal da imagem.

Esse recurso é útil para **acessibilidade**, **indexação de imagens**, e **descrição automática** de conteúdo visual.

Com o mesmo recurso criado no laboratório 01, alteramos o serviço para **Add Captions to Images**.

![](steps/Pasted%20image%2020251027020722.png)

Foram feitos testes via interface do Azure com imagens de exemplo.
O resultado pode ser visualizado no print acima.

Também foi criado um script Python (`add_captions_to_images.py`) para simular o consumo da API do serviço:

Em um caso de uso real, seria necessário adaptar algumas coisas no script:

* O **payload** ser dinâmico, recebendo imagens enviadas pelo usuários.
* A **URL** e a **API Key** armazenadas em um arquivo `.env` para segurança.

Para executar o script, voce deve gerar a URL e API Key, alterar no arquivo e executar o script:

```bash
python add_captions_to_images.py
```

Os resultados são salvos na pasta `storage/result-scripts`, com o prefixo `resultado_add_captions_`.

---

# **LAB 04: Add Dense Captions to Images**

O serviço **Add Dense Captions to Images** vai além das legendas simples, ele gera **múltiplas descrições detalhadas (dense captions)** sobre regiões específicas da imagem.
Isso permite identificar **vários objetos e contextos simultaneamente**, tornando-o útil para **análise de cenas**, **catalogação de imagens complexas**, e **IA multimodal**.

Com o mesmo recurso criado no laboratório 01, alteramos o serviço para **Add Dense Captions to Images**.

![](steps/Pasted%20image%2020251027022118.png)

Foram realizados testes via interface do Azure com imagens de exemplo.
Os resultados estão registrados no print acima.

Também foi criado um script Python (`add_dense_captions_to_images.py`) que consome a API desse serviço.

Em um caso de uso real, seria necessário adaptar algumas coisas no script:

* O **payload** ser dinâmico, recebendo imagens enviadas pelo usuários.
* A **URL** e a **API Key** armazenadas em um arquivo `.env` para segurança.

Para executar o script, voce deve gerar a URL e API Key, alterar no arquivo e executar o script:

```bash
python add_dense_captions_to_images.py
```

Os resultados são salvos em arquivos JSON dentro da pasta `storage/result-scripts`, com o prefixo `resultado_add_dense_captions_`.

---

**Conclusão:**

Durante os quatro laboratórios, foi possível compreender na prática como os serviços de **Azure AI Vision** e **Azure AI Face** funcionam, e como podem ser integrados a aplicações reais através de chamadas HTTP simples.

Esses experimentos demonstram o poder das **APIs de Inteligência Artificial do Azure** para análise visual, reconhecimento facial, extração de texto e geração de legendas automáticas, pilares fundamentais em aplicações modernas de visão computacional.

---