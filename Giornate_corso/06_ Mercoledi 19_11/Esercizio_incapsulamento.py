# ---------------------------------------------------------
# Classe base: Persona
# ---------------------------------------------------------

class Persona:
    def __init__(self, nome, eta):
        # Attributi privati (incapsulamento)
        self.__nome = nome
        self.__eta = eta

    # Getter e setter per nome
    def get_nome(self):
        return self.__nome

    def set_nome(self, nuovo_nome):
        self.__nome = nuovo_nome

    # Getter e setter per età
    def get_eta(self):
        return self.__eta

    def set_eta(self, nuova_eta):
        if nuova_eta >= 0:
            self.__eta = nuova_eta
        else:
            print("L'età non può essere negativa.")

    # Metodo di presentazione base
    def presentazione(self):
        testo = f"Mi chiamo {self.__nome} e ho {self.__eta} anni."
        print(testo)
        return testo


# ---------------------------------------------------------
# Sottoclasse: Studente (eredita da Persona)
# ---------------------------------------------------------

class Studente(Persona):
    def __init__(self, nome, eta, voti):
        # Richiamo il costruttore della superclasse
        super().__init__(nome, eta)
        # Lista di interi che rappresentano i voti
        self.voti = voti

    def calcola_media(self):
        if not self.voti:
            return 0
        return sum(self.voti) / len(self.voti)

    # Override del metodo presentazione (polimorfismo)
    def presentazione(self):
        media = self.calcola_media()
        testo_base = f"Mi chiamo {self.get_nome()} e ho {self.get_eta()} anni."
        testo = f"{testo_base} Sono uno studente e la mia media dei voti è {media:.2f}."
        print(testo)
        return testo


# ---------------------------------------------------------
# Sottoclasse: Professore (eredita da Persona)
# ---------------------------------------------------------

class Professore(Persona):
    def __init__(self, nome, eta, materia):
        # Richiamo il costruttore della superclasse
        super().__init__(nome, eta)
        # Materia insegnata
        self.materia = materia

    # Override del metodo presentazione (polimorfismo)
    def presentazione(self):
        testo = (
            f"Mi chiamo {self.get_nome()} e ho {self.get_eta()} anni. "
            f"Sono un professore di {self.materia}."
        )
        print(testo)
        return testo


# ---------------------------------------------------------
# Esempio di utilizzo e dimostrazione del polimorfismo
# ---------------------------------------------------------

if __name__ == "__main__":
    p1 = Persona("Mario Rossi", 40)
    s1 = Studente("Luca Bianchi", 17, [8, 7, 9, 10])
    prof1 = Professore("Anna Verdi", 35, "Matematica")

    elenco_persone = [p1, s1, prof1]

    # Polimorfismo: tutte hanno presentazione(), ma ognuna fa qualcosa di diverso
    for persona in elenco_persone:
        persona.presentazione()
