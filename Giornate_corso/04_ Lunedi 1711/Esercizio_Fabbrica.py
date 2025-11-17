# ---------------------------------------------------------
# CLASSI BASE
# ---------------------------------------------------------

class Prodotto:
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita

    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione


# ---------------------------------------------------------
# CLASSI PARALLELE
# ---------------------------------------------------------

class Abbigliamento(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.materiale = materiale


class Elettronica(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia_anni):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.garanzia_anni = garanzia_anni


# ---------------------------------------------------------
# CLASSE FABBRICA
# ---------------------------------------------------------

class Fabbrica:
    def __init__(self):
        # inventario = { nome_prodotto : quantità }
        self.inventario = {}

    def aggiungi_prodotto(self, prodotto, quantita):
        if prodotto.nome in self.inventario:
            self.inventario[prodotto.nome] += quantita
        else:
            self.inventario[prodotto.nome] = quantita

    def vendi_prodotto(self, prodotto, quantita):
        nome = prodotto.nome

        if nome not in self.inventario:
            print("Prodotto non presente in inventario.")
            return

        if self.inventario[nome] < quantita:
            print("Quantità richiesta non disponibile.")
            return

        # diminuisce quantità
        self.inventario[nome] -= quantita

        # calcolo profitto
        profitto_totale = prodotto.calcola_profitto() * quantita

        print(f"Hai venduto {quantita} pezzi di {nome}.")
        print(f"Profitto totale: {profitto_totale} €")

    def stato_inventario(self):
        print("\n--- Inventario Attuale ---")
        for nome, qta in self.inventario.items():
            print(f"{nome}: {qta} pezzi")
        print("---------------------------")


# ---------------------------------------------------------
# BLOCCO DI TEST (CODICE ESEGUIBILE)
# ---------------------------------------------------------

if __name__ == "__main__":
    # Creo prodotti
    maglietta = Abbigliamento("Maglietta", 5, 15, "Cotone")
    smartphone = Elettronica("Smartphone", 120, 300, 2)

    # Creo la fabbrica
    fabbrica = Fabbrica()

    # Aggiungo prodotti
    fabbrica.aggiungi_prodotto(maglietta, 50)
    fabbrica.aggiungi_prodotto(smartphone, 20)

    # Mostro inventario iniziale
    fabbrica.stato_inventario()

    # Vendo alcuni prodotti
    fabbrica.vendi_prodotto(maglietta, 10)
    fabbrica.vendi_prodotto(smartphone, 5)

    # Mostro inventario finale
    fabbrica.stato_inventario()
