'''Problema: Solicitar al usuario dos conjuntos de números y luego mostrar:

    La unión de ambos conjuntos.

    La intersección de ambos conjuntos'''

conjunto1=set(map(int,input("ingresa los numeros del primer conjunto").split()))
conjunto2=set(map(int,input("ingresa los numeros del primer conjunto").split()))
union=conjunto1 | conjunto2
interseccion= conjunto1 & conjunto2

print(union)
print(interseccion)







    
    