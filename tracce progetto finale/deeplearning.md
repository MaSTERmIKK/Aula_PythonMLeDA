# Traccia Progetto: "Sfida all'Ultimo Gesto: Sasso, Carta, Forbice vs PC"

### L'Obiettivo
Il tuo obiettivo è costruire un gioco interattivo. Il giocatore farà un gesto (Sasso, Carta o Forbice) davanti alla webcam del computer. Un modello di Intelligenza Artificiale (Deep Learning) dovrà "guardare" l'immagine dalla webcam e capire che mossa ha fatto il giocatore. Il computer poi sceglierà una mossa a caso e il programma decreterà il vincitore della mano.

### Cosa ti serve (Ingredienti)
* Python
* Librerie per il Deep Learning (es. Keras/TensorFlow o PyTorch)
* Libreria per gestire la webcam (es. OpenCV, che si installa con `pip install opencv-python`)

---

### Le 3 Fasi del Progetto

Il progetto si divide in tre passaggi fondamentali. Non cercare di fare tutto subito! Affronta una fase alla volta.

#### FASE 1: I Dati (Insegnare con l'esempio)
Un modello di Deep Learning non sa cos'è un "Sasso" se non glielo mostri prima.

* **Il compito:** Ti servono centinaia di immagini di mani che fanno "Sasso", centinaia di "Carta" e centinaia di "Forbice".
* **Come fare (scegli una via):**
    * **Via Facile:** Cerca online un dataset già pronto (su siti come Kaggle ce ne sono molti cercando "Rock Paper Scissors dataset"). Scaricalo e organizzalo in tre cartelle separate.
    * **Via "Fai da te" (Più istruttiva):** Scrivi un piccolo script con OpenCV che accende la tua webcam e scatta una foto ogni volta che premi un tasto. Passa 5 minuti a fotografare la tua mano in posizioni diverse per ogni gesto.

#### FASE 2: Il "Cervello" (Il modello di Deep Learning)
Ora devi creare e addestrare la rete neurale che imparerà a distinguere le tre cartelle di immagini.

* **Il compito:** Costruire una rete neurale per la classificazione di immagini.
* **Il consiglio:** Se avete visto le **CNN (Reti Neurali Convoluzionali)**, questo è il momento di usarle: sono fatte apposta per le immagini! Se avete visto solo reti dense (MLP), dovrete prima "appiattire" le immagini in un lungo vettore di pixel, ma funzionerà un po' peggio.
* **L'output:** La tua rete neurale dovrà avere **3 neuroni finali** (uno per Sasso, uno per Carta, uno per Forbice).

#### FASE 3: L'Arena (Il Gioco vero e proprio)
È il momento di mettere tutto insieme in uno script finale che gira in tempo reale.

* **Il loop del gioco:** Dovrai creare un programma che fa queste cose all'infinito (finché non lo fermi):
    1.  Accende la webcam e cattura un singolo fotogramma (un'immagine).
    2.  Prepara l'immagine per il modello (magari riducendola di dimensione o convertendola in bianco e nero, a seconda di come hai allenato il modello).
    3.  Passa l'immagine al modello ("Cervello") e ottiene la predizione (es. "L'utente ha fatto: Forbice").
    4.  Il PC sceglie una mossa a caso (usando `random.choice(['sasso', 'carta', 'forbice'])`).
    5.  Il programma confronta le due mosse (con dei semplici `if/else`) e stampa a schermo chi ha vinto.

---

### Livelli di difficoltà 

* ⭐ **Livello Base:** Il gioco funziona. Carichi un dataset da internet, addestri un modello semplice, e lo script finale stampa nella console del terminale le mosse e chi ha vinto.
* ⭐⭐ **Livello Intermedio:** Usi una rete CNN per migliorare la precisione. Nello script finale, invece di stampare sulla console, usi OpenCV per scrivere il risultato direttamente sopra il video della webcam (es. testo rosso "HAI PERSO!" in sovraimpressione).
* ⭐⭐⭐ **Livello Avanzato:** Raccogli tu stesso le immagini con la tua webcam per l'addestramento, così il modello è specializzato sulla tua mano e il tuo sfondo. Riesci a far funzionare il gioco in modo fluido senza che si blocchi tra un frame e l'altro.