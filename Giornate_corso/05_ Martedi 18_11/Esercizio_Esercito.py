# 1. Classe Base: UnitaMilitare
class UnitaMilitare:
    def __init__(self, nome, numero_soldati):
        self.nome = nome
        self.numero_soldati = numero_soldati

    def muovi(self):
        print(f"{self.nome}: Si sta muovendo verso l'obiettivo.")

    def attacca(self):
        print(f"{self.nome}: Sta attaccando il nemico!")

    def ritira(self):
        print(f"{self.nome}: Sta effettuando un ritiro strategico.")

# 2. Classi Derivate (Specializazioni)

class Fanteria(UnitaMilitare):
    def costruisci_trincea(self):
        print(f"{self.nome} (Fanteria): Costruisce difese temporanee.")

class Artiglieria(UnitaMilitare):
    def calibra_artiglieria(self):
        print(f"{self.nome} (Artiglieria): Calibra i pezzi per la precisione.")

class Cavalleria(UnitaMilitare):
    def esplora_terreno(self):
        print(f"{self.nome} (Cavalleria): Esplora l'area per info sul nemico.")

class SupportoLogistico(UnitaMilitare):
    def rifornisci_unita(self):
        print(f"{self.nome} (Logistica): Gestisce rifornimento e manutenzione.")

class Ricognizione(UnitaMilitare):
    def conduci_ricognizione(self):
        print(f"{self.nome} (Ricognizione): Conduce missione di sorveglianza.")

# 3. Classe ControlloMilitare
# NOTA: L'esercizio richiede che questa classe erediti da TUTTE le altre.
# In Python si usa l'ereditarietà multipla.
class ControlloMilitare(Fanteria, Artiglieria, Cavalleria, SupportoLogistico, Ricognizione):
    def __init__(self):
        # Inizializziamo il dizionario per tenere traccia delle unità
        self.unita_registrate = {}
        
    def registra_unita(self, unita):
        # Aggiunge un'istanza di unità al registro usando il nome come chiave
        if isinstance(unita, UnitaMilitare):
            self.unita_registrate[unita.nome] = unita
            print(f"[Sistema]: Unità '{unita.nome}' registrata con successo.")
        else:
            print("[Errore]: Oggetto non valido.")

    def mostra_unita(self):
        print("\n--- Elenco Unità Registrate ---")
        if not self.unita_registrate:
            print("Nessuna unità registrata.")
        for nome in self.unita_registrate:
            print(f"- {nome}")
        print("-------------------------------")

    def dettagli_unita(self, nome):
        if nome in self.unita_registrate:
            unita = self.unita_registrate[nome]
            print(f"\n--- Dettagli {unita.nome} ---")
            print(f"Tipo: {type(unita).__name__}")
            print(f"Numero Soldati: {unita.numero_soldati}")
            # Eseguiamo un metodo generico per dimostrazione
            unita.muovi()
        else:
            print(f"\n[Errore]: L'unità '{nome}' non è stata trovata.")

# --- ESEMPIO DI UTILIZZO (Main) ---

# Creazione del gestore (ControlloMilitare)
comando_centrale = ControlloMilitare()

# Creazione delle singole unità
alpha_team = Fanteria("Alpha Team", 150)
bravo_cannons = Artiglieria("Bravo Cannons", 50)
charlie_horses = Cavalleria("Charlie Horses", 80)
delta_supply = SupportoLogistico("Delta Supply", 20)
echo_scout = Ricognizione("Echo Scout", 10)

# Registrazione delle unità nel sistema di controllo
comando_centrale.registra_unita(alpha_team)
comando_centrale.registra_unita(bravo_cannons)
comando_centrale.registra_unita(charlie_horses)
comando_centrale.registra_unita(delta_supply)
comando_centrale.registra_unita(echo_scout)

# Mostrare l'elenco delle unità
comando_centrale.mostra_unita()

# Mostrare i detagli di una specifica unità e usare i suoi metodi speciali
comando_centrale.dettagli_unita("Bravo Cannons")
bravo_cannons.calibra_artiglieria() # Metodo specifico dell'Artiglieria

comando_centrale.dettagli_unita("Alpha Team")
alpha_team.costruisci_trincea() # Metodo specifico della Fanteria
