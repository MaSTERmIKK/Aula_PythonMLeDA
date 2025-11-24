numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# funzione di filtro: prende un indice x
def somma_due_maggiore_del_terzo(x):
    return numbers[x] + numbers[x + 1] > numbers[x + 2]

# così x+1 e x+2 esisttono sempre
indici = range(len(numbers) - 2)

indici_validi = list(filter(somma_due_maggiore_del_terzo, indici))

gruppi_validi = [
    (numbers[i], numbers[i + 1], numbers[i + 2])
    for i in indici_validi
]

print("Indici che rispettano la condizione:", indici_validi)
print("Gruppi (x, x+1, x+2) validi:", gruppi_validi)
