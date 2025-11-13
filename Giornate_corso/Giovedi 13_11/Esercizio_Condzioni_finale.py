# --- Esercizio 1: Controllo età per vedere un film ---

eta_input = input("Inserisci la tua età: ")
eta = int(eta_input)   # converto in numero

if eta < 18:
    print("Mi dispiace, non puoi vedere questo film.")
else:
    print("Puoi vedere questo film.")


# --- Esercizio 2: Mini calcolatrice con if / elif ---

# inserimento dei due numeri
n1_input = input("Inserisci il primo numero: ")
n2_input = input("Inserisci il secondo numero: ")

n1 = float(n1_input)
n2 = float(n2_input)

# inserimento operazione
op = input("Scegli l'operazione (+, -, *, /): ")

if op == "+":
    risultato = n1 + n2
    print("Risultato:", risultato)

elif op == "-":
    risultato = n1 - n2
    print("Risultato:", risultato)

elif op == "*":
    risultato = n1 * n2
    print("Risultato:", risultato)

elif op == "/":
    # controllo divisione per zero
    if n2 == 0:
        print("Errore: Divisione per zero")
    else:
        risultato = n1 / n2
        print("Risultato:", risultato)

else:
    print("Operazione non valida.")

