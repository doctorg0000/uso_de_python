'''
Teniendo en cuenta el ejercicio anterior calcule el
residuo con el símbolo de módulo % y entregue la
comprobación con los valores resultantes de dividir
dos números entregados por el usuario del
programa 

'''

dividendo=int(input('ingrese el valor que desea dividir '))
divisor=int(input('ingrese el valor por el que desea dividir '))

cociente=dividendo//divisor
residuo=dividendo%divisor

print(divisor,' * ',cociente,' + ',residuo,' = ', dividendo)











