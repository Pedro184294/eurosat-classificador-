# 🛰️ Global Solution — Classificação de Imagens de Satélite com CNN

## 1. Sobre o projeto

Este projeto foi desenvolvido para a **Global Solution**, com o objetivo de aplicar técnicas de Inteligência Artificial e Deep Learning na classificação de imagens de satélite para monitoramento territorial.

A solução utiliza uma **Rede Neural Convolucional (CNN)** treinada com imagens do conjunto de dados EuroSAT RGB, permitindo identificar diferentes tipos de ocupação territorial.

Além do treinamento e da avaliação dos modelos, foi desenvolvida uma aplicação web com Streamlit para permitir que o usuário envie imagens e visualize as classificações realizadas pela rede neural.

## 2. Objetivo

Desenvolver e avaliar modelos próprios de Redes Neurais Convolucionais capazes de classificar imagens de satélite em quatro categorias:

- 🏘️ Residential — áreas residenciais.
- 🏭 Industrial — áreas industriais.
- 🌳 Forest — áreas de floresta.
- 🌊 River — áreas de rios.

O projeto também busca comparar diferentes configurações de CNN e selecionar o modelo com melhor desempenho de validação.

## 3. Tecnologias utilizadas

- Python 3.11
- TensorFlow 2.21.0
- Keras
- NumPy 2.4.6
- Matplotlib
- Scikit-learn
- Streamlit 1.67.0
- Pillow
- Google Colab
- Visual Studio Code
- Git e GitHub

## 4. Conjunto de dados

Foi utilizado o conjunto de dados **EuroSAT RGB**, composto por imagens de satélite de diferentes categorias de ocupação do território.

Fonte: [EuroSAT RGB — Hugging Face](https://huggingface.co/datasets/mteb/eurosat-rgb)

Para este projeto, foram selecionadas quatro classes, com 200 imagens por categoria, totalizando 800 imagens.

### Distribuição dos dados

| Conjunto | Imagens |
|---|---:|
| Treinamento | 560 |
| Validação | 120 |
| Teste | 120 |
| **Total** | **800** |

Cada imagem foi redimensionada para 64 × 64 pixels, convertida para RGB e normalizada para valores entre 0 e 1.

## 5. Desenvolvimento dos modelos CNN

Foram desenvolvidas três configurações de Redes Neurais Convolucionais, com o objetivo de comparar arquiteturas e estratégias de treinamento.

### CNN 1 — Modelo baseline

Arquitetura inicial utilizada como referência para os experimentos.

Características:
- Duas camadas convolucionais.
- Camadas MaxPooling.
- Camada Flatten.
- Camada Dense com 64 neurônios.
- Camada de saída com quatro classes.
- Sem Dropout ou Batch Normalization.

### CNN 2 — Arquitetura com Batch Normalization

Modelo com maior profundidade e normalização das ativações.

Características:
- Três blocos convolucionais.
- Filtros de 32, 64 e 128.
- Batch Normalization.
- ReLU e MaxPooling.
- Global Average Pooling.
- Camada Dense com 128 neurônios.
- Dropout.
- Camada de saída com quatro classes.

### CNN 3 — Modelo com Data Augmentation

Modelo desenvolvido para explorar técnicas de aumento de dados e melhorar a capacidade de generalização.

Características:
- Data Augmentation.
- Três camadas convolucionais.
- Filtros de 32, 64 e 128.
- MaxPooling.
- Dropout.
- Global Average Pooling.
- Camada Dense com 64 neurônios.
- Camada de saída com quatro classes.

## 6. Comparação dos experimentos

Os modelos foram comparados utilizando principalmente os resultados de validação, sem utilizar o conjunto de teste para escolher a arquitetura.

| Modelo | Melhor acurácia de validação |
|---|---:|
| CNN 1 — Baseline | 87,50% |
| CNN 2 — Batch Normalization | 83,33% |
| CNN 3 — Data Augmentation | 82,50% |

A CNN 1 apresentou o melhor resultado de validação entre as configurações avaliadas e foi selecionada para a avaliação final.

## 7. Avaliação final do modelo

Após a seleção do modelo, foi realizada a avaliação no conjunto de teste, separado durante a preparação dos dados.

### Métricas gerais

| Métrica | Resultado |
|---|---:|
| Accuracy | 86,67% |
| Precision | 87,43% |
| Recall | 86,67% |
| F1-score | 86,71% |

### Resultados por classe

| Classe | Precision | Recall | F1-score |
|---|---:|---:|---:|
| Residential | 81% | 83% | 82% |
| Industrial | 86% | 83% | 85% |
| Forest | 100% | 83% | 91% |
| River | 83% | 97% | 89% |

Os resultados demonstram que o modelo conseguiu reconhecer as quatro categorias territoriais, apresentando destaque na classificação das áreas de floresta e rios.

## 8. Aplicação web

Foi desenvolvida uma aplicação utilizando Streamlit para disponibilizar o modelo treinado de maneira simples e interativa.

### Funcionalidades

- Upload de imagens nos formatos JPG, JPEG e PNG.
- Pré-processamento automático das imagens.
- Redimensionamento para 64 × 64 pixels.
- Classificação utilizando o modelo CNN treinado.
- Exibição da classe identificada.
- Apresentação da confiança da previsão.
- Visualização das probabilidades individuais das quatro classes.

### Tecnologias da aplicação

- Python
- Streamlit
- TensorFlow
- NumPy
- Pillow

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
├── README.md
└── .gitignore
```

A pasta `.venv` contém o ambiente virtual local e não deve ser enviada ao GitHub.

## 10. Como executar o projeto

### Pré-requisitos

- Python 3.11
- Visual Studio Code
- Git

### 1. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
```

### 2. Entrar na pasta

```bash
cd eurosat-classificador
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
python -m streamlit run app.py
```

A aplicação estará disponível no navegador em:

```text
http://localhost:8501
```

## 11. Considerações finais

O projeto permitiu explorar o desenvolvimento de Redes Neurais Convolucionais aplicadas à classificação de imagens de satélite.

A comparação entre três configurações de CNN possibilitou avaliar diferentes arquiteturas e estratégias de treinamento, além de selecionar um modelo com base no desempenho de validação.

A implementação da aplicação web com Streamlit tornou possível disponibilizar o modelo treinado para testes interativos, demonstrando uma aplicação prática de Inteligência Artificial no monitoramento territorial.

---

**Projeto acadêmico — FIAP | Global Solution**

Classificação de Imagens de Satélite com Redes Neurais Convolucionais.