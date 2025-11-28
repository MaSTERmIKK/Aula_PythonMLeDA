import numpy as np
import pandas as pd

# Per rendere i risultati ripetibili
np.random.seed(42)

# ---------------------------------------------------
# 1. Caricare i dati in un DataFrame autogenerandoli
# ---------------------------------------------------
n_persone = 30

nomi = ["Anna", "Marco", "Luca", "Giulia", "Paolo",
        "Sara", "Giorgio", "Marta", "Davide", "Elena"]
citta = ["Milano", "Roma", "Torino", "Napoli", "Bologna",
         "Firenze", "Genova", "Palermo"]

df = pd.DataFrame({
    "Nome": np.random.choice(nomi, size=n_persone),
    "Età": np.random.randint(15, 80, size=n_persone),
    "Città": np.random.choice(citta, size=n_persone),
    "Salario": np.random.randint(1200, 4500, size=n_persone)
})

# Aggiungo qualche duplicato artificiale
df = pd.concat([df, df.iloc[:3]], ignore_index=True)

# Introduco qualche valore mancante artificiale
for col in ["Età", "Salario"]:
    indici_nan = np.random.choice(df.index, size=3, replace=False)
    df.loc[indici_nan, col] = np.nan

print("DATAFRAME INIZIALE (con duplicati e NaN):")
print(df)
print("-" * 60)

# ---------------------------------------------------
# 2. Visualizzare le prime e le ultime cinque righe
# ---------------------------------------------------
print("PRIME 5 RIGHE:")
print(df.head())
print("\nULTIME 5 RIGHE:")
print(df.tail())
print("-" * 60)

# ---------------------------------------------------
# 3. Visualizzare il tipo di dati di ciascuna colonna
# ---------------------------------------------------
print("TIPI DI DATO DELLE COLONNE (dtypes):")
print(df.dtypes)
print("-" * 60)

# ---------------------------------------------------
# 4. Statistiche descrittive per colonne numeriche
#    (media, mediana, deviazione standard)
# ---------------------------------------------------
numeriche = df.select_dtypes(include=["float64", "int64"])
statistiche = numeriche.agg(["mean", "median", "std"])
print("STATISTICHE DESCRITTIVE (colonne numeriche):")
print(statistiche)
print("-" * 60)

# ---------------------------------------------------
# 5. Identificare e rimuovere eventuali duplicati
# ---------------------------------------------------
duplicati = df.duplicated()
print(f"Numero di righe duplicate: {duplicati.sum()}")
df = df.drop_duplicates()
print("DataFrame dopo rimozione duplicati:")
print(df)
print("-" * 60)

# ---------------------------------------------------
# 6. Gestire i valori mancanti sostituendoli con
#    la mediana della rispettiva colonna
# ---------------------------------------------------
for col in numeriche.columns:
    mediana = df[col].median()
    df[col] = df[col].fillna(mediana)

print("DataFrame dopo imputazione dei NaN con la mediana:")
print(df)
print("-" * 60)

# ---------------------------------------------------
# 7. Aggiungere colonna 'Categoria Età'
#    0–18  -> Giovane
#    19–65 -> Adulto
#    >65   -> Senior
# ---------------------------------------------------
def classifica_eta(eta):
    if eta <= 18:
        return "Giovane"
    elif eta <= 65:
        return "Adulto"
    else:
        return "Senior"

df["Categoria Età"] = df["Età"].apply(classifica_eta)

print("DataFrame con nuova colonna 'Categoria Età':")
print(df)
print("-" * 60)

# ---------------------------------------------------
# 8. Salvare il DataFrame pulito in un nuovo file CSV
# ---------------------------------------------------
nome_file = "persone_pulito.csv"
df.to_csv(nome_file, index=False, encoding="utf-8")
print(f"DataFrame pulito salvato in '{nome_file}'.")
