import numpy as np

# -------------------------------------------------------
# 1. Crea un array NumPy:
#    - primi 50 valori da 0 a 49 con arange
#    - altre 50 posizioni casuali tra 49 e 101
# -------------------------------------------------------

prima_parte = np.arange(0, 50)                           # [0..49]
seconda_parte = np.random.randint(49, 102, size=50)      # [49..101]
arr = np.concatenate([prima_parte, seconda_parte])      # ndarray finale (100 elementi)

print("ARRAY ORIGINALE (prima del cambio dtype):")
print(arr)
print("\nDtype:", arr.dtype)
print("Shape:", arr.shape)
print("-" * 60)

# -------------------------------------------------------
# 2. Modifica il tipo di dato (dtype) in float64
# -------------------------------------------------------
arr = arr.astype(np.float64)

print("ARRAY DOPO CONVERSIONE A float64:")
print(arr)
print("\nNuovo dtype:", arr.dtype)
print("Shape:", arr.shape)
print("-" * 60)

# -------------------------------------------------------
# 3. Slicing per ottenere:
#    - i primi 10 elementi
#    - gli ultimi 7 elementi
#    - gli elementi dall'indice 5 all'indice 20 escluso
#    - ogni quarto elemento dell'array
# -------------------------------------------------------
primi_10 = arr[:10]
ultimi_7 = arr[-7:]
da_5_a_20 = arr[5:20]
ogni_quarto = arr[::4]

# -------------------------------------------------------
# 4. Modifica tramite slicing gli elementi dall'indice
#    10 a 15 (escluso) assegnando loro il valore 999
# -------------------------------------------------------
arr[10:15] = 999.0

# -------------------------------------------------------
# 5. Fancy indexing:
#    - elementi in posizione [0, 3, 7, 12, 25, 33, 48]
#    - tutti gli elementi pari (maschera booleana)
#    - tutti gli elementi maggiori della media dell'array
# -------------------------------------------------------
indici = [0, 3, 7, 12, 25, 33, 48]
posizioni_specifiche = arr[indici]

maschera_pari = (arr % 2 == 0)
elementi_pari = arr[maschera_pari]

media = arr.mean()
sopra_media = arr[arr > media]

# -------------------------------------------------------
# 6. Stampa finale
# -------------------------------------------------------
print("\nARRAY ORIGINALE DOPO TUTTE LE MODIFICHE:")
print(arr)
print("-" * 60)

print("Primi 10 elementi:", primi_10)
print("Ultimi 7 elementi:", ultimi_7)
print("Elementi da indice 5 a 19:", da_5_a_20)
print("Ogni quarto elemento:", ogni_quarto)
print("-" * 60)

print("Elementi in posizioni [0, 3, 7, 12, 25, 33, 48]:")
print(posizioni_specifiche)

print("\nElementi pari (fancy indexing con maschera booleana):")
print(elementi_pari)

print("\nMedia dell'array:", media)
print("Elementi maggiori della media:")
print(sopra_media)
