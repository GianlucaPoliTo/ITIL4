import streamlit as st
import pandas as pd
import random
import time
st.title("Streamlit Quiz App for ITIL4 Exam")
# Funzione per ottenere l'input dell'utente come un intero compreso tra 0 e 3

def get_integer_input(prompt, ):
    value = st.number_input("Insert answer 0 - 3", min_value=0, max_value=3, value=None)
    return value

# Carica il dataframe con le domande e le risposte
df_test = pd.read_csv('ITIL4_Exam.csv')
# Inizializza il punteggio corretto
corrette = 0
sbagliate = 0
answer = []
scelta = None
row = df_test.sample(1)

# Per ogni riga del dataframe, visualizza la domanda e le opzioni di risposta
st.write(f'#### Question:')
st.write(f'###### {row["domanda"]}')
## Aggiungi la risposta giusta alla lista delle risposte errate
#row["giusta"] = eval(row["giusta"])
#row["errate"] = eval(row["errate"])
answer = row["errate"].to_list() + row["giusta"].to_list()
random.shuffle(answer)
for j, a in enumerate(answer):
    st.write(f"\t{j}. {a}\n")
    # Ottieni la risposta dall'utente
scelta = get_integer_input("Inserisci risposta 0 - 3:")
    # Controlla se la risposta è corretta
if answer[scelta] == row["giusta"][0]:
    corrette += 1
else:
    st.write(f"Errato, risposta corretta: {row['giusta'][0]}")
    sbagliate +=1
    


