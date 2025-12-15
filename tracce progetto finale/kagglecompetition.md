# Traccia "The Kaggle Challenger": Diario di un Data Scientist

### Per chi è questa traccia?
Questa traccia è pensata per chi vuole misurarsi con il mondo reale. I dataset didattici sono puliti e "facili". Le competizioni Kaggle sono imprevedibili, sporche e competitive.
**Attenzione:** Qui non conta solo il voto finale del modello, ma la qualità del percorso che hai fatto per arrivarci.

### L'Obiettivo
Partecipare a una competizione **attiva** (o appena conclusa) sulla piattaforma [Kaggle](https://www.kaggle.com/).
Il tuo scopo non è necessariamente vincere la competizione, ma documentare ogni tentativo fatto per migliorare il tuo punteggio, creando un vero e proprio **"Diario di Laboratorio"**.

---

### Cosa devi fare (Step by Step)

#### 1. Scegli la tua Arena
Vai su Kaggle nella sezione "Competitions".
* Ti consiglio vivamente la **"Tabular Playground Series"** del mese corrente (sono competizioni mensili pensate per l'apprendimento, con dataset gestibili).
* In alternativa, scegli una competizione "Featured" o "Getting Started" (come *Titanic* o *House Prices* se vuoi andare sul classico, ma le competizioni attive sono più stimolanti).

#### 2. Il "Diario degli Esperimenti" (Il cuore del progetto)
Invece della classica relazione, devi consegnare un report strutturato in **ordine cronologico**. Immagina di essere uno scienziato che annota i progressi giorno per giorno.

Il report deve contenere una tabella o una lista di "Iterazioni". Per ogni tentativo (sottomissione a Kaggle), devi compilare questa scheda:

> **ESPERIMENTO #N**
> * **L'Idea/Ipotesi:** *Cosa voglio testare?* (Es. "Credo che il modello stia facendo overfitting, quindi provo a ridurre la profondità degli alberi").
> * **L'Azione:** *Cosa ho cambiato nel codice?* (Es. "RandomForest `max_depth` impostato a 5 invece che None. Rimossa la feature 'Nome Passeggero'").
> * **Il Risultato (Score):** *Il punteggio ottenuto sulla Public Leaderboard.*
> * **Analisi:** *È migliorato o peggiorato? Perché?* (Es. "Peggiorato. Probabilmente `max_depth=5` è troppo basso e il modello non impara abbastanza (Underfitting)").

#### 3. I Requisiti Minimi
Per considerare il progetto completo, il tuo diario deve contenere almeno **5 iterazioni significative** che mostrino l'uso di diverse tecniche:

1.  **Baseline:** Un modello semplice (es. Regressione Logistica o un albero decisionale base) senza preprocessing avanzato. Serve come punto di partenza.
2.  **Feature Engineering:** Un tentativo in cui crei nuove feature o pulisci i dati in modo diverso (es. gestione dei missing values, encoding, scaling).
3.  **Ensemble Learning:** Un tentativo usando Random Forest, XGBoost o simili.
4.  **Deep Learning (La sfida):** Un tentativo usando una Rete Neurale (MLP). **Nota:** Sui dati tabellari è difficile battere XGBoost. La sfida è: *quanto riesci ad avvicinarti alle performance dell'Ensemble usando una Rete Neurale?*
5.  **Tuning:** Un tentativo di ottimizzazione degli iperparametri (Grid Search o tentativi manuali ragionati).

### Struttura della Consegna

Il tuo output finale sarà un **Notebook Jupyter** ben commentato o un **PDF** che includa:

1.  **Descrizione del problema:** Di cosa tratta la competizione?
2.  **Analisi Esplorativa (EDA):** Cosa hai scoperto guardando i grafici dei dati?
3.  **Il Diario degli Esperimenti:** La lista cronologica dei tentativi (come descritto sopra).
    * *Esempio: "Tentativo 3: Ho provato a normalizzare i dati per la rete neurale, il punteggio è salito da 0.60 a 0.75".*
    * *Esempio: "Tentativo 4: Ho aggiunto più layer alla rete, ma il punteggio è sceso. Probabile overfitting."*
4.  **Conclusione "Post-Mortem":**
    * Qual è stato il modello vincitore tra i tuoi tentativi?
    * Cosa hai imparato che non ti aspettavi?
    * Se avessi avuto un'altra settimana di tempo, cosa avresti provato?

---

### Criteri di Valutazione 
* **Non valuto il punteggio assoluto:** Non mi importa se sei 1° o 1000° in classifica mondiale.
* **Valuto il ragionamento:** Un esperimento fallito (che peggiora il punteggio) vale quanto uno riuscito, **SE** sai spiegare *perché* è fallito.
* **Valuto la varietà:** Aver provato sia approcci classici (Ensemble) che Deep Learning.
