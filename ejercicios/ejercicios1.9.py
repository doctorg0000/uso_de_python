'''
Compruebe mediante el operador de identidad
correspondiente si la letra w se encuentra en la
expresión “Python es un lenguaje de programación
muy popular”. Utilice un input para consultar lo
mismo y comprobar según la entrada que dé el
usuario. 

'''
w="w"
expresion = "Python es un lenguaje de programación muy popular"

print(w is expresion)

X=input('Introduce una letra ')

print(X is expresion)

# # Definir la letra 'w'
# w = "w"
# expresion = "Python es un lenguaje de programación muy popular"

# # Verificar si la letra 'w' está en la expresión usando el operador 'is'
# print(w is expresion[expresion.find(w)] if w in expresion else False)

# # Solicitar al usuario una letra
# X = input('Introduce una letra: ')

# # Verificar si la letra ingresada por el usuario está en la expresión utilizando el operador 'is'
# resultado = False
# for char in expresion:
#     if X is char:
#         resultado = True
#         break

# # Imprimir el resultado
# print(resultado)