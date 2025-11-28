import sqlite3
import csv
import os

# Nomi dei file
DB_NAME = 'magazzino.db'
CSV_FILE = 'prodotti_import.csv'

# --- 0. PREPARAZIONE: Creiamo un file CSV finto per l'esempio ---
# In un caso reale, questo file lo avresti già.
def crea_csv_finto():
    dati = [
        ["Nome Prodotto", "Categoria", "Prezzo", "Quantità"], # Header
        ["Laptop Gaming", "Elettronica", "1200.50", "5"],
        ["Mouse Wireless", "Elettronica", "25.99", "50"],
        ["Sedia Ufficio", "Arredamento", "150.00", "12"],
        ["Caffè in Grani", "Alimentari", "18.90", "100"],
        ["Monitor 4K", "Elettronica", "399.99", "7"]
    ]
    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(dati)
    print(f"File '{CSV_FILE}' creato per il test.")

# --- 1. FUNZIONE PER IMPORTARE CSV NEL DB ---
def importa_csv_in_db():
    print("\n--- Inizio Importazione CSV -> SQLite ---")
    
    # Connessione al DB
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # 1. Creiamo la tabella (se non esiste)
    # Nota: Definiamo i tipi corretti (REAL per prezzi, INTEGER per quantità)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS prodotti (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        categoria TEXT,
        prezzo REAL,
        quantita INTEGER
    );
    """)

    # 2. Apertura e Lettura del CSV
    with open(CSV_FILE, mode='r', encoding='utf-8') as f:
        csv_reader = csv.reader(f)
        
        # IMPORTANTE: Saltiamo l'intestazione (header) del CSV
        # next() legge la prima riga e sposta il cursore alla seconda
        header = next(csv_reader) 
        print(f"Header rilevato: {header}")

        # 3. Preparazione dei dati (TRANSFORM)
        # Il CSV legge tutto come stringhe. Dobbiamo convertire i numeri.
        dati_da_inserire = []
        for riga in csv_reader:
            # riga è tipo ['Laptop', 'Elettronica', '1200.50', '5']
            nome = riga[0]
            categoria = riga[1]
            try:
                # Convertiamo stringa '1200.50' -> float 1200.50
                prezzo = float(riga[2]) 
                # Convertiamo stringa '5' -> int 5
                quantita = int(riga[3]) 
                
                # Aggiungiamo la tupla pulita alla lista
                dati_da_inserire.append((nome, categoria, prezzo, quantita))
            except ValueError:
                print(f"Saltata riga corrotta: {riga}")

        # 4. Inserimento di massa (LOAD)
        # Usiamo executemany per la massima velocità
        sql = "INSERT INTO prodotti (nome, categoria, prezzo, quantita) VALUES (?, ?, ?, ?)"
        cursor.executemany(sql, dati_da_inserire)
        
        conn.commit()
        print(f"Importati con successo {cursor.rowcount} prodotti.")

    conn.close()

# --- 2. FUNZIONE PER RILEGGERE DAL DB ---
def leggi_dal_db():
    print("\n--- Lettura dati da SQLite ---")
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row # Per accedere ai dati col nome colonna
    cursor = conn.cursor()

    # Esempio: Selezioniamo solo elettronica sopra i 300 euro
    print("Query: Cerco Elettronica > 300€")
    cursor.execute("""
        SELECT nome, prezzo, quantita 
        FROM prodotti 
        WHERE categoria = 'Elettronica' AND prezzo > ?
    """, (300,))

    rows = cursor.fetchall()
    
    if not rows:
        print("Nessun prodotto trovato.")
    else:
        print(f"{'PRODOTTO':<20} | {'PREZZO':<10} | {'DISPONIBILI':<10}")
        print("-" * 45)
        for row in rows:
            # Qui i dati sono già nel tipo corretto (float/int), non stringhe!
            print(f"{row['nome']:<20} | {row['prezzo']:<10.2f} | {row['quantita']:<10}")

    conn.close()

# --- ESECUZIONE ---
if __name__ == "__main__":
    crea_csv_finto()      # Genera il file
    importa_csv_in_db()   # Scrive nel DB
    leggi_dal_db()        # Legge dal DB