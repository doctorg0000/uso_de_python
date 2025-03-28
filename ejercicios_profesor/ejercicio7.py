'''
Problema: Almacenar los nombres de 3 ciudades en una tupla y luego mostrar:

    La primera y la última ciudad.

    La cantidad de caracteres de cada ciudad.
'''


a=str(input("ingresa el nombre de la ciudad 1 "))
s=str(input("ingresa el nombre de la ciudad 2 "))
d=str(input("ingresa el nombre de la ciudad 3 "))
      
tupla_1=(a,s,d)
print(tupla_1[0],tupla_1[-1])
print(len(tupla_1[0]))
print(len(tupla_1[1]))
print(len(tupla_1[2]))


