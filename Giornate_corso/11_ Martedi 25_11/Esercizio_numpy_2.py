import numpy as np
import os

FILE_NAME = "es2_linspace_random_sum.txt"

def salva_su_file(contenuto, mode):
    """Scrive il testo nel file con il mode passato ('w' o 'a')."""
    with open(FILE_NAME, mode, encoding="utf-8") as f:
        f.write(contenuto + "\n")


def esecuzione_singolo_giro(giro_n):
    # 1. Array di 50 numeri equidistanti tra 0 e 10
    arr_lin = np.linspace(0, 10, 50)

    # 2. Array di 50 numeri casuali tra 0 e 1
    arr_rand = np.random.random(50)

    # 3. Somma elemento per elemento
    arr_sum = arr_lin + arr_rand

    # 4. Somma totale degli elementi del nuovo array
    somma_totale = arr_sum.sum()

    # 5. Somma degli elementi del nuovo array > 5
    somma_maggiori_5 = arr_sum[arr_sum > 5].sum()

    # 6. Stampa a video
    print(f"\n=== GIRO {giro_n} ===")
    print("Array linspace (0→10):")
    print(arr_lin)
    print("\nArray random (0→1):")
    print(arr_rand)
    print("\nNuovo array (somma elemento per elemento):")
    print(arr_sum)
    print("\nSomma totale elementi nuovo array:", somma_totale)
    print("Somma elementi > 5:", somma_maggiori_5)

    # Prepariamo testo per il file
    testo = []
    testo.append(f"=== GIRO {giro_n} ===")
    testo.append("Array linspace (0→10):")
    testo.append(str(arr_lin))
    testo.append("Array random (0→1):")
    testo.append(str(arr_rand))
    testo.append("Nuovo array (somma):")
    testo.append(str(arr_sum))
    testo.append(f"Somma totale: {somma_totale}")
    testo.append(f"Somma elementi > 5: {somma_maggiori_5}")
    testo.append("")  # riga vuota

    return "\n".join(testo)


def main():
    # 9. Chiedi se si vuole sovrascrivere il TXT o no
    sovrascrivi = input(
        f"Vuoi sovrascrivere il file '{FILE_NAME}' se esiste? (s/n): "
    ).strip().lower()

    if sovrascrivi == "s":
        mode_primo_giro = "w"   # sovrascrive
    else:
        mode_primo_giro = "a"   # appende

    giro = 1
    primo_giro = True

    while True:
        # 7. Salva i dati su un file TXT a ogni giro
        contenuto = esecuzione_singolo_giro(giro)

        if primo_giro:
            salva_su_file(contenuto, mode_primo_giro)
            primo_giro = False
        else:
            # dai giri successivi appendo sempre
            salva_su_file(contenuto, "a")

        # 8. Rendi ripetibile il processo complessivo
        scelta = input("\nVuoi eseguire un altro giro? (s/n): ").strip().lower()
        if scelta != "s":
            print("Fine programma.")
            break

        giro += 1


if __name__ == "__main__":
    main()
