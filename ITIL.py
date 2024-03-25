import streamlit as st
import pandas as pd
import random

st.title("Streamlit Quiz App for ITIL4 Exam")
# Funzione per ottenere l'input dell'utente come un intero compreso tra 0 e 3
def get_integer_input(prompt, key):
    while True:
        try:
            value = int(st.text_input(prompt, key=key+str(random.randint(0,100000)), default=0))
            if 0 <= value <= 3:
                return value
            else:
                st.error("Inserisci un numero compreso tra 0 e 3.")
        except ValueError:
            st.error("Inserisci un numero valido.")

# Carica il dataframe con le domande e le risposte
df_test = pd.read_csv('ITIL4_Exam.csv')
n_domande=15
test = df_test.sample(n_domande).reset_index(drop=True)
test.index=test.index+1
# Inizializza il punteggio corretto
corrette = 0
answer = []
# Per ogni riga del dataframe, visualizza la domanda e le opzioni di risposta
for i, row in test.iterrows():
    st.write(f'Question {i}):')
    st.write(f'{row["domanda"]}')
    ## Aggiungi la risposta giusta alla lista delle risposte errate
    row["giusta"] = eval(row["giusta"])
    row["errate"] = eval(row["errate"])
    answer = row["errate"] + row["giusta"]
    random.shuffle(answer)
    for j, a in enumerate(answer):
        st.write(f"\t{j}. {a}\n")

    # Ottieni la risposta dall'utente
    scelta = get_integer_input("Inserisci risposta 0 - 3:", key=f"input_{i}")
    
    # Controlla se la risposta è corretta
    if answer[scelta] == row["giusta"][0]:
        corrette += 1
    else:
        st.write(f"Errato, risposta corretta: {row['giusta'][0]}")

# Visualizza il punteggio totale
st.write(f"Your final score is {corrette}/{len(test)}")

