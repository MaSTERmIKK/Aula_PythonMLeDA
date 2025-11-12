# Esercizio 1: if annidati con confronto
# L'utente deve superare tre livelli di verifica per "passare"

print("Benvenuto al test a 3 livelli!")

# Primo livello
livello1 = input("Scrivi 'via' per iniziare: ")
if livello1 == "via":
    # Secondo livello
    livello2 = input("Scrivi 'python' per continuare: ")
    if livello2 == "python":
        # Terzo livello
        livello3 = input("Scrivi 'ok' per vincere: ")
        if livello3 == "ok":
            print("Complimenti! Hai superato tutti e 3 i livelli!")
        else:
            print("Errore al terzo livello!")
    else:
        print("Errore al secondo livello!")
else:
    print("Errore al primo livello!")


# Esercizio 2: menu CRUD semplificato

print("\nMenu CRUD:")
print("1 - Aggiungi elemento")
print("2 - Rimuovi elemento")
print("3 - Visualizza elenco")
print("4 - Esci")

scelta = input("Scegli un'opzione (1-4): ")

if scelta == "1":
    print("Hai scelto: Aggiungi elemento")
elif scelta == "2":
    print("Hai scelto: Rimuovi elemento")
elif scelta == "3":
    print("Hai scelto: Visualizza elenco")
elif scelta == "4":
    print("Uscita dal programma...")
else:
    print("Scelta non valida. Riprova.")

