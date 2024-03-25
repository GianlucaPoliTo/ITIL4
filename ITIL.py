import streamlit as st
import pandas as pd
import random

# Funzione per ottenere l'input dell'utente come un intero compreso tra 0 e 3
def get_integer_input(prompt):
    while True:
        try:
            value = int(st.text_input(prompt))
            if 0 <= value <= 3:
                return value
            else:
                st.error("Inserisci un numero compreso tra 0 e 3.")
        except ValueError:
            st.error("Inserisci un numero valido.")

# Carica il dataframe con le domande e le risposte
test = pd.read_csv('ITIL4_Exam.csv')

# Inizializza il punteggio corretto
corrette = 0

# Per ogni riga del dataframe, visualizza la domanda e le opzioni di risposta
for i, row in test.iterrows():
    st.write(f'Domanda {i + 1}):\n{row["domanda"]}')
    answer = row["errate"] + row["giusta"]  # Aggiungi la risposta giusta alla lista delle risposte errate
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

# Visualizza il punteggio totale
st.write(f"Hai ottenuto un punteggio di {corrette}/{len(test)}")

