import streamlit as st
import pandas as pd
import random

st.title("Streamlit Quiz App for ITIL4 Exam")
# Funzione per ottenere l'input dell'utente come un intero compreso tra 0 e 3
def get_integer_input(prompt, key):
    with st.form(key):
        value = st.number_input("Insert answer 0 - 3", min_value=0, max_value=3, value=None, key=key)
        submitted = st.form_submit_button("Submit")
    return value

# Carica il dataframe con le domande e le risposte
df_test = pd.read_csv('ITIL4_Exam.csv')
n_domande=15
test = df_test.sample(n_domande).reset_index(drop=True)
test.index=test.index+1
# Inizializza il punteggio corretto
corrette = 0
answer = []
scelta = None
# Per ogni riga del dataframe, visualizza la domanda e le opzioni di risposta
for i, row in test.iterrows():
    st.write(f'#### Question {i}):')
    st.write(f'###### {row["domanda"]}')
    ## Aggiungi la risposta giusta alla lista delle risposte errate
    row["giusta"] = eval(row["giusta"])
    row["errate"] = eval(row["errate"])
    answer = row["errate"] + row["giusta"]
    random.shuffle(answer)
    for j, a in enumerate(answer):
        st.write(f"\t{j}. {a}\n")

    # Ottieni la risposta dall'utente
    while scelta == None:
        scelta = get_integer_input("Inserisci risposta 0 - 3:", key=f"input_{i}")
        if scelta != None:
            # Controlla se la risposta è corretta
            if answer[scelta] == row["giusta"][0]:
                corrette += 1
                break
            else:
                st.write(f"Errato, risposta corretta: {row['giusta'][0]}")

# Visualizza il punteggio totale
st.write(f"Your final score is {corrette}/{len(test)}")

