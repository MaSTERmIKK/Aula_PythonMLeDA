# --------------------------------------------
# Esempio base: variabili e tipi in Python
# --------------------------------------------

# Variabile intera (int)
numero_intero = 10
print("Valore:", numero_intero)
print("Tipo:", type(numero_intero))  # <class 'int'>

# Variabile decimale (float)
numero_decimale = 3.14
print("\nValore:", numero_decimale)
print("Tipo:", type(numero_decimale))  # <class 'float'>

# Variabile testuale (string)
testo = "Ciao, Python!"
print("\nValore:", testo)
print("Tipo:", type(testo))  # <class 'str'>

# Variabile booleana (bool)
vero_o_falso = True
print("\nValore:", vero_o_falso)
print("Tipo:", type(vero_o_falso))  # <class 'bool'>

# Variabile nulla (NoneType)
niente = None
print("\nValore:", niente)
print("Tipo:", type(niente))  # <class 'NoneType'>

# --------------------------------------------
# Esempio di conversione di tipo (casting)
# --------------------------------------------
print("\n--- Esempi di casting ---")

numero_testo = "100"              # stringa
numero_convertito = int(numero_testo)  # convertito in intero
print("Da stringa a intero:", numero_convertito, type(numero_convertito))

float_da_int = float(numero_intero)
print("Da intero a float:", float_da_int, type(float_da_int))
