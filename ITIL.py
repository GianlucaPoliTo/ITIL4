import streamlit as st
import pandas as pd
import random
import time
import streamlit_book as stb

st.title("Streamlit Quiz App for ITIL4 Exam")
# Funzione per ottenere l'input dell'utente come un intero compreso tra 0 e 3

def get_integer_input(prompt, ):
    value = st.number_input("Insert answer 0 - 3", min_value=0, max_value=3, value=None)
    return value

# Carica il dataframe con le domande e le risposte
df_test = pd.read_csv('ITIL4_Exam.csv')
# Inizializza il punteggio corretto
for row in df_test.iterrows():
    row["giusta"] = eval(row["giusta"])
    row["sbagliate"] = eval(row[”sbagliate"])
    answers = row["giusta"]+row["sbagliate"]
    random.shuffle(answers)
    index = answers.index(row["giusta"])
    question = row["domanda"]
    single_choice(question, answers, index, success='Correct answer', error='Wrong answer', button='Check answer')

