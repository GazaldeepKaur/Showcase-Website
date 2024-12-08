import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
col1, col2 = st.columns(2)
with col1:
    st.image('images/photo.png')

with col2:
    st.title('Ardit Sulce')
    st.write('Shakira, the daughter of a Lebanese father and a Colombian mother, '
             'started belly dancing at an early age. By age 10 she had begun writing songs '
             'and participating in talent competitions. A local theater producer helped her '
             'land an audition with a Sony Corp. executive in 1990, and Shakira was subsequently '
             'signed to a record deal. Her first two albums, Magia (1991) and Peligro (1993), '
             'were only moderately successful, however. After taking a break from recording to '
             'act in the Colombian telenovela El oasis, Shakira resumed her music career in impressive '
             'fashion with Pies descalzos (1995). The album produced several hits, including “Estoy aquí,” '
             '“Pienso en ti,” and “Un poco de amor.”')

st.write("Shakira (born February 2, 1977, Barranquilla, Colombia) is a Colombian singer, songwriter, "
         "musician, and dancer who built a successful career in both Spanish- and English-speaking markets "
         "to become one of the most popular Latin American recording artists of the early 21st century.")

col3, empty_col, col4 = st.columns([1.5,0.5,1.5])
df = pd.read_csv('data.csv', sep=';')
with col3:
    for index, row in df[:10].iterrows():
        st.title(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.title(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[Source Code]({row['url']})")

