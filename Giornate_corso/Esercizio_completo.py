# ---------------------------------------------------------
# ESERCITAZIONE COMPLETA - Soluzione Base
# ---------------------------------------------------------

# 1. WHILE per garantire numero positivo
n = int(input("Inserisci un numero intero positivo: "))

while n <= 0:
    print("Il numero deve essere positivo!")
    n = int(input("Reinserisci un numero intero positivo: "))

print("\nHai inserito:", n)

# ---------------------------------------------------------
# 2. FOR + RANGE per somma dei numeri PARI da 1 a n
somma_pari = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        somma_pari += i

print("Somma dei numeri pari da 1 a", n, "=", somma_pari)

# ---------------------------------------------------------
# 3. FOR per stampare tutti i numeri DISPARI da 1 a n
print("\nNumeri dispari da 1 a", n, ":")

for i in range(1, n + 1):
    if i % 2 == 1:
        print(i)

# ---------------------------------------------------------
# 4. IF per determinare se n è primo
# Un numero è primo se è divisibile solo per 1 e per se stesso

if n == 1:
    print("\n1 NON è un numero primo.")
else:
    primo = True  # assumiamo che sia primo

    for i in range(2, n):
        if n % i == 0:
            primo = False
            break

    if primo:
        print("\n", n, "è un numero primo.", sep="")
    else:
        print("\n", n, "NON è un numero primo.", sep="")
