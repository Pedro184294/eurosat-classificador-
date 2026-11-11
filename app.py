
import json
import numpy as np
import streamlit as st
import tensorflow as tf

from PIL import Image, UnidentifiedImageError


# Configurações da página
st.set_page_config(
    page_title="EuroSAT - Classificador",
    page_icon="🛰️",
    layout="wide"
)


# Ícones das classes
ICONES_CLASSES = {
    "Residential": "🏘️",
    "Industrial": "🏭",
    "Forest": "🌳",
    "River": "🌊"
}


# Carregamento do modelo
@st.cache_resource
def carregar_modelo():
    return tf.keras.models.load_model(
        "modelo_final/cnn_eurosat.keras",
        compile=False
    )


# Carregamento das classes
@st.cache_data
def carregar_classes():
    with open(
        "modelo_final/classes.json",
        "r",
        encoding="utf-8"
    ) as arquivo:
        return json.load(arquivo)


# Tratamento de erros no carregamento
try:
    modelo = carregar_modelo()
    classes = carregar_classes()

except Exception as erro:
    st.error(f"Erro ao carregar o modelo ou as classes: {erro}")
    st.stop()


# Cabeçalho
st.title("🛰️ Classificação de Imagens de Satélite")

st.subheader(
    "Monitoramento Territorial com Inteligência Artificial"
)

st.write(
    """
    Aplicação desenvolvida com uma Rede Neural Convolucional
    (CNN), treinada com imagens do conjunto de dados EuroSAT.

    O sistema identifica quatro categorias de áreas territoriais
    a partir de imagens de satélite.
    """
)

st.divider()


# Classes identificadas
st.markdown("### Classes identificadas pelo modelo")

col1, col2, col3, col4 = st.columns(4)

col1.info("🏘️ Residential")
col2.info("🏭 Industrial")
col3.info("🌳 Forest")
col4.info("🌊 River")

st.divider()


# Upload da imagem
st.markdown("### Envie uma imagem de satélite")

arquivo_imagem = st.file_uploader(
    "Selecione uma imagem no formato JPG, JPEG ou PNG",
    type=["jpg", "jpeg", "png"]
)


# Classificação
if arquivo_imagem is not None:

    try:
        imagem = Image.open(arquivo_imagem).convert("RGB")

        col_imagem, col_resultado = st.columns(2)

        with col_imagem:
            st.markdown("#### Imagem enviada")

            st.image(
                imagem,
                caption="Imagem original",
                width="stretch"
            )

        # Pré-processamento
        imagem_processada = imagem.resize((64, 64))

        imagem_array = np.array(
            imagem_processada,
            dtype=np.float32
        )

        imagem_array = imagem_array / 255.0

        imagem_array = np.expand_dims(
            imagem_array,
            axis=0
        )

        # Previsão do modelo
        previsoes = modelo.predict(
            imagem_array,
            verbose=0
        )[0]

        indice_classe = int(np.argmax(previsoes))

        nome_classe = classes[str(indice_classe)]

        confianca = float(previsoes[indice_classe])

        with col_resultado:

            st.markdown("#### Resultado da classificação")

            icone = ICONES_CLASSES.get(
                nome_classe,
                "🛰️"
            )

            st.success(
                f"{icone} Classe identificada: **{nome_classe}**"
            )

            st.metric(
                label="Confiança da previsão",
                value=f"{confianca * 100:.2f}%"
            )

            st.progress(confianca)

            st.markdown("#### Probabilidade por classe")

            for indice, probabilidade in enumerate(previsoes):

                nome = classes[str(indice)]

                icone_classe = ICONES_CLASSES.get(
                    nome,
                    "🛰️"
                )

                st.write(
                    f"{icone_classe} **{nome}** — "
                    f"{probabilidade * 100:.2f}%"
                )

                st.progress(float(probabilidade))

    except (UnidentifiedImageError, OSError):

        st.error(
            "Não foi possível abrir a imagem. "
            "Envie um arquivo JPG, JPEG ou PNG válido."
        )

    except Exception as erro:

        st.error(
            f"Erro durante a classificação: {erro}"
        )


# Rodapé
st.divider()

st.caption(
    "Projeto acadêmico - Global Solution | "
    "Classificação de Imagens com Redes Neurais Convolucionais"
)
