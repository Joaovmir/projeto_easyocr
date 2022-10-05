import streamlit as st
import cv2
import easyocr

arquivo_imagem = st.file_uploader("Escolha uma imagem", type=['jpg', 'png'])

if arquivo_imagem:
    with open(f'imagens/{arquivo_imagem.name}' , 'wb') as arquivo:
        arquivo.write(arquivo_imagem.getbuffer())
    st.image(arquivo_imagem)
    
    imagem = cv2.imread(f'imagens/{arquivo_imagem.name}')
    leitor = easyocr.Reader(['pt','en'])
    resultado = leitor.readtext(imagem)
    st.write(resultado)
    texto_corrido = ' '.join(resultado)
    st.write(texto_corrido)
    with open(f'textos/{texto_corrido[:10]}.txt' , 'w') as arquivo:
        arquivo.write(texto_corrido)
    st.success("Arquivos salvos")