# --- Raccolta input ---
booleano_input = input("Inserisci un valore booleano (True/False): ")
intero_input = input("Inserisci un numero intero: ")
stringa_input = input("Inserisci una stringa: ")

# --- Conversioni ---
booleano = booleano_input == "True"
intero = int(intero_input)

# --- Inseriamo in una lista ---
lista_valori = [booleano, intero, stringa_input]

# --- Creiamo il dizionario ---
dizionario = {
    "tipidato": lista_valori
}

# --- Ciclo con .items() ---
for chiave, valore in dizionario.items():
    print("Chiave:", chiave)
    print("Valore:", valore)
