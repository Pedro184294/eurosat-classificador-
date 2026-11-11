# 🛰️ Global Solution — Classificação de Imagens de Satélite com CNN

## 1. Sobre o projeto

Este projeto foi desenvolvido como parte da **Global Solution**, com o objetivo de aplicar Inteligência Artificial e Visão Computacional na classificação de imagens de satélite.

A solução utiliza uma **Rede Neural Convolucional (CNN)** treinada com imagens do conjunto de dados EuroSAT para identificar diferentes categorias de áreas territoriais.

O sistema permite enviar uma imagem de satélite por meio de uma aplicação web e obter automaticamente a classe prevista pelo modelo, juntamente com o nível de confiança e as probabilidades de cada categoria.

### Aplicação online

🌐 **Acesse a aplicação:**  
https://eurosat-classificador-pedro184294.streamlit.app/

### Repositório GitHub

💻 **Código-fonte:**  
https://github.com/Pedro184294/eurosat-classificador-

---

## 2. Objetivos

- Desenvolver uma Rede Neural Convolucional própria para classificação de imagens.
- Aplicar técnicas de processamento de imagens e Deep Learning.
- Comparar diferentes configurações de arquiteturas CNN.
- Avaliar o desempenho dos modelos por meio de métricas de classificação.
- Disponibilizar o melhor modelo em uma aplicação web interativa.

---

## 3. Tecnologias utilizadas

| Tecnologia | Aplicação |
|---|---|
| Python | Linguagem principal |
| TensorFlow / Keras | Construção e treinamento das CNNs |
| NumPy | Manipulação de dados e matrizes |
| Matplotlib | Visualização dos resultados |
| Scikit-learn | Métricas e avaliação dos modelos |
| Streamlit | Desenvolvimento da aplicação web |
| Pillow | Processamento de imagens |
| Google Colab | Ambiente de treinamento |
| Git e GitHub | Versionamento e armazenamento do projeto |
| Streamlit Community Cloud | Hospedagem da aplicação |

---

## 4. Conjunto de dados

Foi utilizado o conjunto de dados **EuroSAT RGB**, disponibilizado publicamente no Hugging Face.

Fonte: https://huggingface.co/datasets/mteb/eurosat-rgb

O conjunto original contém imagens de satélite divididas em diferentes categorias de uso e cobertura do solo.

Para este projeto, foram selecionadas quatro classes:

| Classe | Descrição |
|---|---|
| Residential | Áreas residenciais |
| Industrial | Áreas industriais |
| Forest | Áreas florestais |
| River | Rios e áreas de água |

### Distribuição dos dados

Foi utilizado um subconjunto balanceado de 800 imagens, com 200 imagens para cada classe.

| Conjunto | Imagens |
|---|---:|
| Treinamento | 560 |
| Validação | 120 |
| Teste | 120 |
| **Total** | **800** |

As imagens foram redimensionadas para 64 × 64 pixels e normalizadas para valores entre 0 e 1.

A divisão dos dados foi realizada de forma estratificada, mantendo a distribuição das quatro classes nos conjuntos de treinamento, validação e teste.

---

## 5. Desenvolvimento das arquiteturas CNN

Foram desenvolvidas e comparadas três configurações de Redes Neurais Convolucionais.

### CNN 1 — Modelo base

Primeira arquitetura utilizada como referência para os experimentos.

Principais características:

- Duas camadas convolucionais.
- Filtros de 32 e 64.
- Camadas de MaxPooling.
- Camada Flatten.
- Camada Dense com 64 neurônios.
- Camada de saída com quatro classes.

### CNN 2 — Arquitetura com Batch Normalization

Segunda configuração, desenvolvida para avaliar uma arquitetura com maior profundidade.

Principais características:

- Três blocos convolucionais.
- Filtros de 32, 64 e 128.
- Batch Normalization.
- Ativação ReLU.
- MaxPooling.
- Global Average Pooling.
- Camada Dense com 128 neurônios.
- Dropout.
- Camada de saída com quatro classes.

### CNN 3 — Arquitetura com aumento de dados

Terceira configuração, desenvolvida para avaliar o uso de técnicas de regularização e aumento de dados.

Principais características:

- Três camadas convolucionais.
- Filtros de 32, 64 e 128.
- Técnicas de Data Augmentation.
- MaxPooling.
- Dropout.
- Global Average Pooling.
- Camada Dense com 64 neurônios.
- Camada de saída com quatro classes.

---

## 6. Comparação dos experimentos

Os modelos foram comparados utilizando a acurácia de validação como critério de seleção.

| Modelo | Melhor acurácia de validação | Resultado |
|---|---:|---|
| CNN 1 | 87,50% | Melhor desempenho |
| CNN 2 | 83,33% | Não selecionado |
| CNN 3 | 82,50% | Não selecionado |

Com base nos resultados, a **CNN 1 foi selecionada** para a avaliação final e integração com a aplicação web.

O conjunto de teste foi mantido separado durante o desenvolvimento e utilizado somente na avaliação final do modelo escolhido.

---

## 7. Avaliação final do modelo

A CNN 1 apresentou os seguintes resultados no conjunto de teste independente, composto por 120 imagens.

### Métricas gerais

| Métrica | Resultado |
|---|---:|
| Accuracy | 86,67% |
| Precision (macro) | 87,43% |
| Recall (macro) | 86,67% |
| F1-Score (macro) | 86,71% |

O modelo classificou corretamente 104 das 120 imagens de teste.

### Resultados por classe

| Classe | Precision | Recall | F1-Score |
|---|---:|---:|---:|
| Residential | 81% | 83% | 82% |
| Industrial | 86% | 83% | 85% |
| Forest | 100% | 83% | 91% |
| River | 83% | 97% | 89% |

### Análises realizadas

Durante a avaliação dos experimentos, foram utilizadas:

- Accuracy.
- Precision.
- Recall.
- F1-Score.
- Matriz de confusão.
- Curvas de acurácia de treinamento e validação.
- Curvas de perda (Loss) de treinamento e validação.

---

## 8. Aplicação web

A aplicação foi desenvolvida com Streamlit e integrada ao modelo CNN treinado.

O usuário pode enviar uma imagem de satélite nos formatos JPG, JPEG ou PNG.

Após o envio, o sistema:

1. Carrega a imagem selecionada.
2. Converte a imagem para RGB.
3. Redimensiona para 64 × 64 pixels.
4. Normaliza os valores dos pixels.
5. Executa a previsão utilizando o modelo CNN.
6. Identifica a classe com maior pontuação.
7. Exibe a confiança da previsão e as probabilidades das quatro classes.

### Classes disponíveis

- 🏘️ Residential
- 🏭 Industrial
- 🌳 Forest
- 🌊 River

### Acesso à aplicação

**Link público:**  
https://eurosat-classificador-pedro184294.streamlit.app/

---

## 9. Estrutura do projeto

```text
eurosat-classificador/
│
├── modelo_final/
│   ├── classes.json
│   └── cnn_eurosat.keras
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

### Descrição dos arquivos

| Arquivo | Descrição |
|---|---|
| `app.py` | Código principal da aplicação Streamlit |
| `requirements.txt` | Dependências necessárias para execução |
| `modelo_final/cnn_eurosat.keras` | Modelo CNN treinado |
| `modelo_final/classes.json` | Mapeamento dos índices para os nomes das classes |
| `.gitignore` | Arquivos e pastas ignorados pelo Git |
| `README.md` | Documentação do projeto |

---

## 10. Como executar o projeto localmente

### Pré-requisitos

- Python 3.11.
- Git.
- VS Code (opcional).

### 1. Clonar o repositório

```bash
git clone https://github.com/Pedro184294/eurosat-classificador-.git
```

### 2. Entrar na pasta do projeto

```bash
cd eurosat-classificador-
```

### 3. Criar o ambiente virtual

```bash
python -m venv .venv
```

### 4. Ativar o ambiente virtual

No Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Instalar as dependências

```bash
python -m pip install -r requirements.txt
```

### 6. Executar a aplicação

```bash
streamlit run app.py
```

A aplicação estará disponível localmente em:

```text
http://localhost:8501
```

---

## 12. Considerações finais

O projeto demonstrou a aplicação de Redes Neurais Convolucionais na classificação de imagens de satélite, desde a preparação dos dados até a disponibilização de um modelo funcional em uma aplicação web.

A comparação entre três configurações de CNN permitiu selecionar a arquitetura com melhor desempenho de validação. Na avaliação final, o modelo escolhido alcançou 86,67% de acurácia no conjunto de teste.

A solução integra conceitos de Inteligência Artificial, Deep Learning, processamento de imagens e desenvolvimento web, demonstrando como essas tecnologias podem contribuir para a análise e classificação de informações territoriais.

---

**Projeto acadêmico desenvolvido para a Global Solution.**  
**Classificação de Imagens de Satélite utilizando Redes Neurais Convolucionais (CNN).**