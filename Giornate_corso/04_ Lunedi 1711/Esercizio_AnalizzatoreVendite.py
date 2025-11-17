# ---------------------------------------------------------
# Esercizio: Analizzatore di Dati di Vendita
# ---------------------------------------------------------
# NOTA (per spiegare i moduli):
# Se questa classe fosse in un altro file (es. analizzatore.py),
# qui sopra scriveremmo:
# from analizzatore import Esercizio_AnalizzatoreVendite
# ---------------------------------------------------------


class AnalizzatoreVendite:
    # Classe semplice per gestire i dati di vendita
    def __init__(self, vendite):
        self.vendite = vendite  # lista di interi

    def calcola_totale(self):
        return sum(self.vendite)

    def calcola_media(self):
        if len(self.vendite) == 0:
            return 0
        return self.calcola_totale() / len(self.vendite)

    def vendite_sopra_media(self):
        risultato = []
        media = self.calcola_media()

        for indice, valore in enumerate(self.vendite):
            if valore > media:
                # indice + 1 per avere il "giorno" umano (parte da 1, non da 0)
                risultato.append((indice + 1, valore))

        return risultato


# ---------------------------------------------------------
# Parte "main" del programma
# ---------------------------------------------------------

# 1. Inserimento dei dati con gestione eccezioni
while True:
    testo = input("Inserisci gli importi di vendita separati da spazio: ")

    # Se l'utente non inserisce niente
    if testo.strip() == "":
        print("Non sono stati inseriti dati. Riprova.")
        continue

    parti = testo.split()
    vendite = []

    try:
        for p in parti:
            numero = int(p)
            vendite.append(numero)
        # se tutto va bene si esce dal while
        break
    except ValueError:
        print("Errore: hai inserito qualcosa che non è un numero.")
        print("Riprova inserendo solo numeri interi, separati da spazi.\n")

# 2. Creiamo l'oggetto analizzatore
analizzatore = AnalizzatoreVendite(vendite)

# 3. Calcolo totale e media
totale = analizzatore.calcola_totale()
media = analizzatore.calcola_media()

print("\n--- Risultati Generali ---")
print("Dati di vendita inseriti:", vendite)
print("Totale vendite:", totale)
print("Media vendite:", media)

# 4. Vendite sopra la media
sopra_media = analizzatore.vendite_sopra_media()

print("\n--- Giorni con vendite sopra la media ---")
if len(sopra_media) == 0:
    print("Non ci sono giorni con vendite sopra la media.")
else:
    for giorno, valore in sopra_media:
        print(f"Giorno {giorno}: vendita = {valore}")

print("\nFine analisi dati.")
