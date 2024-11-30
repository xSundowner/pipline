import firebase_admin
from firebase_admin import credentials, firestore, storage
import datetime
import pandas as pd
import json
import plotly.express as px
import plotly.figure_factory as ff
import io

file_path = 'MandaPix.json'

cred = credentials.Certificate(file_path)
firebase_admin.initialize_app(cred, {
    'storageBucket':'projeto-1676a.appspot.com'
})

db = firestore.client()
bucket = storage.bucket()

blobs = bucket.list_blobs()

all_dfs = []
for blob in blobs:
    file_content = blob.download_as_text()
    df = pd.read_csv(io.StringIO(file_content))
    all_dfs.append(df)

df = all_dfs[1]
valores = df['Teacher_Quality'].value_counts()

fig0 = px.bar(
    x=valores.index,
    y=valores.values,
    title='Avaliação da qualidade dos professores',
    labels={'x': 'Qualidade dos professores', 'y': 'Qnt de alunos que avaliaram'}
)

df = all_dfs[1]
valores = df['Internet_Access'].value_counts()

fig1 = px.bar(
    x=valores.index,
    y=valores.values,
    title='Estudantes com acesso à internet',
    labels={'x': 'Acesso à Internet', 'y': 'Número de Alunos'}
)

df = all_dfs[2]
valores = df['Gender'].value_counts()

fig2 = px.bar(
    x=valores.index,
    y=valores.values,
    title='Gênero dos Estudantes',
    labels={'x': 'F = Feminino / M = Masculino', 'y': 'Quantidade de Alunos'}
)

df = all_dfs[3]
valores = df['Socioeconomic_Status'].value_counts()

fig3 = px.bar(
    x=valores.index,
    y=valores.values,
    title='Status Socioeconômico',
    labels={'x': 'Avaliação', 'y': 'Quantidade de Alunos'}
)

df = all_dfs[4]
valores = df['Sleep_Quality'].value_counts()

fig4 = px.bar(
    x=valores.index,
    y=valores.values,
    title='Avaliação da Qualidade de Sono',
    labels={'x': 'Nota (0 a 10)', 'y': 'Quantidade de Alunos'}
)

fig0.show()
fig1.show()
fig2.show()
fig3.show()
fig4.show()