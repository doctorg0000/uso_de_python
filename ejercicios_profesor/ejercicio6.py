'''
Problema: Solicitar al usuario 5 números enteros, almacenarlos en una lista y luego mostrar:

    La lista original.

    La lista en orden inverso.

    La suma de los números.
'''

x=int(input("ingresa un numero "))
a=int(input("ingresa un numero "))
s=int(input("ingresa un numero "))
d=int(input("ingresa un numero "))
f=int(input("ingresa un numero "))

lista_1=[x,a,s,d,f]

print(lista_1)

print(lista_1[::-1])

print("la suma de la lista es = ", x+a+s+d+f)





