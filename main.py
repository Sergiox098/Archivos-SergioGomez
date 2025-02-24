varpais = input("Ingrese el país que desee consultar la cantidad de compras: ")
import csv
with open("C:/Users/sergio gomez/Documents/Programación 2024/Archivos/files/files/SalesJan2009.csv",newline="") as f:
    a=list((csv.DictReader(f)))
    pais = [col8["Country"] for col8 in a]
    producto = [col8["Country"] for col8 in a]
    lista = []
    ilista = []
    b = []
    for i in pais:
        if i == varpais:
            lista.append(i)
            ilista.append(pais.index(i))
            pais.remove(i)
    for i in ilista:
        b.append(producto[i-1])
sumproduct = len(b)   
print("El país \"",varpais,"\" en el 2009 tuvo un total de",sumproduct,"compras realizadas")
