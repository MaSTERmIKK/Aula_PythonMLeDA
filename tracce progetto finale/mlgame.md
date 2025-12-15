# Progetto Finale: "The AI DJ" – Costruisci il tuo Spotify Personale

### 1\. Scenario e Obiettivo

Hai mai notato come Spotify o YouTube sembrino "leggerti nel pensiero" dopo un po' che li usi? Questo progetto ti porta dietro le quinte di quella magia.
Il tuo obiettivo è creare un'applicazione interattiva da terminale che simula un **Recommender System**.
Il programma partirà da zero (non sa nulla dei tuoi gusti) e dovrà imparare in *tempo reale* quali canzoni ti piacciono, proponendoti brani sempre più affini ai tuoi gusti man mano che interagisci.

**La Sfida tecnica:** Implementare un ciclo di **Active Learning** (Apprendimento Attivo) dove il dataset di training si costruisce dinamicamente durante l'uso del software.

### 2\. Il Dataset

Utilizzeremo un dataset contenente le **audio features** (caratteristiche numeriche) delle canzoni.

  * **Fonte Consigliata:** [Spotify Tracks Dataset su Kaggle](https://www.google.com/search?q=https://www.kaggle.com/datasets/maharshipandya/thompson-sampling-spotify-dataset) (o simili che contengono colonne come `danceability`, `energy`, `valence`, `tempo`, `acousticness`).
  * **Perché questo dataset?** Perché trasforma la musica in numeri. Ad esempio:
      * `Energy` (0.0 - 1.0): Quanto è intensa la canzone.
      * `Valence` (0.0 - 1.0): Quanto è "felice" (1.0) o "triste" (0.0) la canzone.

### 3\. Architettura del Software

Il tuo programma Python dovrà funzionare secondo questo flusso logico continuo:

#### Fase A: Il "Cold Start" (Avvio a Freddo)

All'inizio il modello è "vuoto". Non può fare predizioni.

1.  Il programma pesca 5-10 canzoni **totalmente a caso** dal database.
2.  Le mostra all'utente (Titolo + Artista).
3.  L'utente vota: `1` (Mi piace) o `0` (Non mi piace / Skip).
4.  Questi primi dati vengono salvati in un nuovo DataFrame: `user_history`.

#### Fase B: Il Training (Il Cervello)

Una volta raccolti i primi voti, entra in gioco il Machine Learning.

1.  **Input (X):** Le features audio delle canzoni votate (`energy`, `danceability`, ecc. - *Escludendo Titolo e Artista\!*).
2.  **Target (y):** I voti dell'utente (0 o 1).
3.  **Addestramento:** Il programma addestra al volo un classificatore.
      * *Opzione ML Classico:* Random Forest o XGBoost.
      * *Opzione Deep Learning:* Un semplice **MLP (Multi-Layer Perceptron)** con Keras/PyTorch (es. 2 layer densi).

#### Fase C: La Predizione (L'Inference)

1.  Il modello prende **tutte le canzoni rimanenti** nel database (quelle non ancora ascoltate).
2.  Calcola per ognuna la **probabilità** che all'utente piaccia (usando `model.predict_proba()`).
3.  Ordina le canzoni e seleziona quella con la probabilità più alta.

#### Fase D: L'Interazione

1.  Il programma stampa: *"Secondo i miei calcoli, questa ti piacerà al 94%: [Titolo - Artista]"*.
2.  Chiede all'utente il verdetto reale (1 o 0).
3.  **Feedback Loop:** La nuova coppia (Canzone + Voto) viene aggiunta alla `user_history`, il modello viene ri-addestrato (o aggiornato) e si torna alla Fase C.

-----

### 4\. Requisiti della Consegna

Il progetto si considera completo se include:

1.  **Preprocessing dei dati:**
      * Pulizia del dataset (gestione valori nulli).
      * Scaling delle features (fondamentale se usate una Rete Neurale, es. `MinMaxScaler` per portare tutto tra 0 e 1).
2.  **Il Codice Interattivo:** Uno script `.py` o un Notebook che permette di giocare senza crashare.
3.  **Analisi delle Feature (L'interpretabilità):**
      * Se usi **Random Forest/XGBoost**: Stampa a schermo ogni 10 turni quali sono le caratteristiche che il modello sta "guardando" di più.
          * *Esempio output:* "Ho capito che ti piacciono canzoni con alta `Energy` e bassa `Acousticness`".
      * Se usi **Deep Learning**: Prova a spiegare come cambia la *loss* durante i vari step di ri-addestramento.
4.  **Grafico Finale (Bonus Visivo):**
      * Quando l'utente decide di uscire dal gioco, mostra un grafico a dispersione (Scatter Plot) con assi `Valence` vs `Energy`. Colora i punti in **Verde** (Like) e **Rosso** (Dislike) e mostra come il modello ha provato a tracciare una linea di separazione.

### 5\. Esempio di funzionamento (Terminale)

```text
--- BENVENUTO NEL TUO AI DJ ---
Sto caricando 5000 canzoni... Fatto.

[Fase di Riscaldamento - Voto 1/5]
Canzone: "Shape of You" - Ed Sheeran
Caratteristiche: Pop, Veloce.
Ti piace? (1=Sì, 0=No): 0

... (dopo 5 voti iniziali) ...

[AI attivata! Ora scelgo io]
Sto analizzando i tuoi gusti... Addestramento completato.

Ho scelto per te: "Bohemian Rhapsody" - Queen.
La mia confidenza è: 89%
Ti è piaciuta? (1=Sì, 0=No): 1

Fantastico! Ho imparato qualcosa di nuovo.
Sto ricalcolando il prossimo brano...
```

### 6\. Valutazione

  * **Livello Base:** implementa il ciclo usando un Decision Tree o KNN. Il gioco funziona.
  * **Livello Intermedio:**  usa una Random Forest o XGBoost e implementa un sistema per non ripetere mai le canzoni.
  * **Livello Avanzato (Deep Learning):**  usa una Rete Neurale. La sfida qui è gestire il training su pochissimi dati (i primi 5 voti) senza andare in *Overfitting* immediato. Spiegare come hai gestito questo problema (es. usando modelli molto semplici all'inizio o facendo data augmentation/noise).