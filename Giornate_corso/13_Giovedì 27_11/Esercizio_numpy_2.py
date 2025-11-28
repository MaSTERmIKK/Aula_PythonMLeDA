"""
Analisi e modello predittivo di churn per compagnia di telecomunicazioni
Usa: pandas, numpy, scikit-learn

File atteso: clienti_telecom.csv
"""

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score, roc_curve, classification_report

# -------------------------------------------------------------------
# 1. CARICAMENTO E ESPLORAZIONE INIZIALE
# -------------------------------------------------------------------

# Carica dati da CSV
df = pd.read_csv("clienti_telecom.csv")

print("\n== Info() ==")
print(df.info())

print("\n== Describe() ==")
print(df.describe(include="all"))

print("\n== Value counts per Churn ==")
print(df["Churn"].value_counts(dropna=False))

# -------------------------------------------------------------------
# 2. PULIZIA DEI DATI
# -------------------------------------------------------------------

# Gestione valori mancanti:
# - per le numeriche: sostituisco con mediana
# - per le categoriche: sostituisco con moda
num_cols = df.select_dtypes(include=[np.number]).columns
cat_cols = df.select_dtypes(exclude=[np.number]).columns

for col in num_cols:
    mediana = df[col].median()
    df[col] = df[col].fillna(mediana)

for col in cat_cols:
    moda = df[col].mode().iloc[0]
    df[col] = df[col].fillna(moda)

# Esempio semplice di correzione anomalie:
# - Età negative o > 100 → NaN → mediana
df.loc[(df["Eta"] < 0) | (df["Eta"] > 100), "Eta"] = np.nan
df["Eta"] = df["Eta"].fillna(df["Eta"].median())

# - Durata_Abbonamento negativa → 0
df.loc[df["Durata_Abbonamento"] < 0, "Durata_Abbonamento"] = 0

# - Tariffa_Mensile <= 0 → mediana
df.loc[df["Tariffa_Mensile"] <= 0, "Tariffa_Mensile"] = np.nan
df["Tariffa_Mensile"] = df["Tariffa_Mensile"].fillna(df["Tariffa_Mensile"].median())

# - Dati_Consumati <= 0 → piccolo valore > 0 per evitare divisioni per zero
df.loc[df["Dati_Consumati"] <= 0, "Dati_Consumati"] = df["Dati_Consumati"].median()

print("\n== Missing values dopo pulizia ==")
print(df.isna().sum())

# -------------------------------------------------------------------
# 3. ANALISI ESPLORATIVA (EDA)
# -------------------------------------------------------------------

# Nuova colonna: Costo_per_GB (tariffa mensile / dati consumati)
df["Costo_per_GB"] = df["Tariffa_Mensile"] / df["Dati_Consumati"]

print("\n== Statistiche per churn (groupby) ==")
print(df.groupby("Churn")[["Eta", "Durata_Abbonamento",
                           "Tariffa_Mensile", "Dati_Consumati",
                           "Servizio_Clienti_Contatti",
                           "Costo_per_GB"]].mean())

# Correlazioni solo numeriche
print("\n== Matrice di correlazione (numeriche) ==")
print(df.select_dtypes(include=[np.number]).corr())

# -------------------------------------------------------------------
# 4. PREPARAZIONE DEI DATI PER LA MODELLAZIONE
# -------------------------------------------------------------------

# Converte Churn in binaria (No=0, Si=1)
df["Churn_bin"] = df["Churn"].map({"No": 0, "Si": 1})

# Normalizzazione / standardizzazione colonne numeriche
feature_cols_num = ["Eta", "Durata_Abbonamento", "Tariffa_Mensile",
                    "Dati_Consumati", "Servizio_Clienti_Contatti",
                    "Costo_per_GB"]

X_num = df[feature_cols_num].values

scaler = StandardScaler()
X_num_scaled = scaler.fit_transform(X_num)

# Se ci fossero categoriche aggiuntive (es. tipo contratto), si potrebbero
# trasformare con pd.get_dummies e concatenare a X_num_scaled.
# Per questa versione teniamo solo le numeriche.

X = X_num_scaled
y = df["Churn_bin"].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# -------------------------------------------------------------------
# 5. ANALISI STATISTICA E PREDITTIVA (MODELLO SEMPLICE)
# -------------------------------------------------------------------

# Modello: Logistic Regression (classico per churn)
log_reg = LogisticRegression(max_iter=1000)
log_reg.fit(X_train, y_train)

# Predizioni
y_pred = log_reg.predict(X_test)
y_proba = log_reg.predict_proba(X_test)[:, 1]

# Metriche
acc = accuracy_score(y_test, y_pred)
auc = roc_auc_score(y_test, y_proba)

print("\n== Risultati Logistic Regression ==")
print("Accuracy:", round(acc, 3))
print("ROC AUC :", round(auc, 3))

print("\n== Classification report ==")
print(classification_report(y_test, y_pred, target_names=["No Churn", "Churn"]))

# (Se vuoi visualizzare la curva ROC puoi usare matplotlib,
#  ma non è strettamente necessario alla consegna.)
