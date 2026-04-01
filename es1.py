# ## Esercizio 1
# Chiedi quanti numeri inserire (`n > 0`), leggi i numeri e salvali in una lista.

# Il programma deve:
# - creare una lista con i numeri positivi e pari;
# - contare i numeri dispari negativi;
# - calcolare la media assoluta dei numeri;
# - stampare lista inserita, lista filtrata, conteggio e media.

# ### Esempio
# Input: `2, -3, 4, -5, 6`

# Output:
# - `Lista inserita: [2, -3, 4, -5, 6]`
# - `Positivi pari: [2, 4, 6]`
# - `Conteggio dispari negativi: 2`
# - `Media assoluta: 4.0`

n = int(input("Quanti numeri vuoi inserire?: "))
lista = []

for i in range (n):
    numero = int(input(f"inserisci il numero {i+1}: "))
    lista.append(numero)
positivi_pari = []
            
for num in lista:
    if num > 0 and num %2 == 0:
        positivi_pari.append(num)
conteggio_dispari_negativi = 0

for num in lista:
    if num < 0 and num %2 != 0:
        conteggio_dispari_negativi += 1
somma_assoluti = 0

for num in lista:
    somma_assoluti += abs (num)
media_assoluta = somma_assoluti / n

print("Lista inserita: ", lista)
print("Positivi pari: ", positivi_pari)
print("Conteggio dispari negativi: ", conteggio_dispari_negativi)
print("Media assoluta: ", media_assoluta)
