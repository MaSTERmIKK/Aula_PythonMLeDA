import pandas as pd  # type: ignore

try:
    # Creazione di un DataFrame da un dizionario
    data = {
        'Nome': ['Alice', 'Bob', 'Charlie'],
        'Età': [24, 27, 22],
        'Città': ['Milano', 'Roma', 'Torino']
    }
    
    df = pd.DataFrame(data)
    
    # Selezione di una singola colonna
    nomi = df['Nome']
    eta_media = df['Età'].mean()
    
    # Aggiunta di una nuova colonna calcolata
    df['Anni Fino a 30'] = 30 - df['Età']
    
    # Filtraggio delle righe dove l'età è maggiore di 23
    filtrato = df[df['Età'] > 23]
    filtrato_nome = df[df['Nome'] == "Bob"]
    
    print(df)
    print(filtrato)
except Exception as e:
    print(f"Si è verificato un errore: {e}")
except ImportError as e:
    print(f"Errore durante l'importazione: {e}")
except KeyError as e:
    print(f"Errore di chiave: {e}")
except TypeError as e:
    print(f"Errore di tipo: {e}")
except ValueError as e:
    print(f"Errore di valore: {e}")


