# -----------------------------------------
# Classe base: Posto
# -----------------------------------------

class Posto:
    def __init__(self, numero, fila):
        self._numero = numero       # int
        self._fila = fila           # str
        self._occupato = False      # bool

    # getter
    def get_numero(self):
        return self._numero

    def get_fila(self):
        return self._fila

    def is_occupato(self):
        return self._occupato

    def prenota(self):
        if not self._occupato:
            self._occupato = True
            print(f"Posto {self._fila}{self._numero} prenotato.")
        else:
            print(f"Posto {self._fila}{self._numero} è già occupato.")

    def libera(self):
        if self._occupato:
            self._occupato = False
            print(f"Posto {self._fila}{self._numero} liberato.")
        else:
            print(f"Posto {self._fila}{self._numero} non era prenotato.")

    def __str__(self):
        stato = "occupato" if self._occupato else "libero"
        return f"Posto {self._fila}{self._numero} - {stato}"


# -----------------------------------------
# Classe derivata: PostoVIP
# -----------------------------------------

class PostoVIP(Posto):
    def __init__(self, numero, fila, servizi_extra):
        super().__init__(numero, fila)
        self.servizi_extra = servizi_extra  # lista di stringhe

    def prenota(self):
        if not self._occupato:
            self._occupato = True
            servizi = ", ".join(self.servizi_extra)
            print(f"Posto VIP {self._fila}{self._numero} prenotato.")
            print(f"   Servizi extra attivati: {servizi}")
        else:
            print(f"Posto VIP {self._fila}{self._numero} è già occupato.")

    def __str__(self):
        stato = "occupato" if self._occupato else "libero"
        servizi = ", ".join(self.servizi_extra)
        return f"PostoVIP {self._fila}{self._numero} - {stato} (servizi: {servizi})"


# -----------------------------------------
# Classe derivata: PostoStandard
# -----------------------------------------

class PostoStandard(Posto):
    def __init__(self, numero, fila, costo):
        super().__init__(numero, fila)
        self.costo = costo  # costo prenotazione

    def prenota(self):
        if not self._occupato:
            self._occupato = True
            print(
                f"Posto Standard {self._fila}{self._numero} prenotato. "
                f"Costo: {self.costo}€"
            )
        else:
            print(f"Posto Standard {self._fila}{self._numero} è già occupato.")

    def __str__(self):
        stato = "occupato" if self._occupato else "libero"
        return f"PostoStandard {self._fila}{self._numero} - {stato} (costo: {self.costo}€)"


# -----------------------------------------
# Classe Teatro
# -----------------------------------------

class Teatro:
    def __init__(self):
        self._posti = []  # lista di Posto / PostoVIP / PostoStandard

    def aggiungi_posto(self, posto):
        self._posti.append(posto)

    def prenota_posto(self, numero, fila):
        for posto in self._posti:
            if posto.get_numero() == numero and posto.get_fila() == fila:
                posto.prenota()
                return
        print(f"Nessun posto trovato con numero {numero} in fila {fila}.")

    def stampa_posti_occupati(self):
        print("Posti occupati:")
        trovato = False
        for posto in self._posti:
            if posto.is_occupato():
                print(" -", posto)
                trovato = True
        if not trovato:
            print(" Nessun posto occupato.")

    def stampa_tutti_i_posti(self):
        print("Tutti i posti in teatro:")
        for posto in self._posti:
            print(" -", posto)


# -----------------------------------------
# Esempio d'uso
# -----------------------------------------

if __name__ == "__main__":
    teatro = Teatro()

    # creo alcuni posti
    p1 = PostoStandard(1, "A", 15.0)
    p2 = PostoStandard(2, "A", 15.0)
    vip1 = PostoVIP(1, "B", ["Accesso lounge", "Servizio al posto"])

    # aggiungo al teatro
    teatro.aggiungi_posto(p1)
    teatro.aggiungi_posto(p2)
    teatro.aggiungi_posto(vip1)

    # prenotazioni
    teatro.prenota_posto(1, "A")
    teatro.prenota_posto(1, "B")
    teatro.prenota_posto(1, "B")  # doppia prenotazione per test

    # stampa
    teatro.stampa_tutti_i_posti()
    teatro.stampa_posti_occupati()
