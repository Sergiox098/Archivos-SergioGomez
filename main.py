varpais = input("Ingrese el país que desee consultar la cantidad de compras: ")
import csv
with open("C:/Users/sergio gomez/Documents/Programación 2024/Archivos/files/files/SalesJan2009.csv",newline="") as f:
    a=list((csv.DictReader(f)))
    pais = [col["Country"] for col in a]
    producto = [col["Product"] for col in a]
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
    valorproducto = []
    for i in b:
        x = i.replace("Product","")
        valorproducto.append(x)   
print(valorproducto)
sumproduct =sum(map(int,valorproducto))
print("El país \"",varpais,"\" en el 2009 tuvo un total de",sumproduct,"compras realizadas")
