listaSpesa = []

def aggiunta(listaSpesa):
    listaSpesa.append(input("aggiungi valore"))
def visualizza(listaSpesa):
    for i in range(len(listaSpesa)):
        print(f"{i + 1}. {listaSpesa[i]}")
def rimuovere(listaSpesa):
    listaSpesa.pop(input("metti indice del elemento da rimuovere"))
    