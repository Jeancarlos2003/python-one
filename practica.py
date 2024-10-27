#incremento de una variable

#print("incremento o aumento")
#x = 2
#print("el valor inicial de x es :", x)
#x += 1

#print("el valor final de x es:", x,"\n")

#mensaje = "hola"
#mensaje += " jose"
#numero = 3
#numero += 4

#print(mensaje, "el resultado de la suma es:", numero)


#nombre = "hola"
#nombre += input("escriba su nombre: ")
#print(nombre, ", esto es el incremento de una variable \n")

#print("concatenacion")
#mensaje = "Hola"
#espacio = " "
#nombre = "pedro"
#print(mensaje + espacio + nombre)

#num_1 = 2
#num_2 = 6
#result = num_1 + num_2
#result = str(result)
#print("el resultado de la suma es: " + result)

#print("busqueda")
#mensaje ="hola juan manuel"
#buscar=mensaje.find("juan manuel")
#print(buscar)

#print("Extraccion:")
#mensaje = ("Hola joseA")
#extraer=mensaje[1:6]
#print(extraer)


#print("comparacion:")
#mensaje1 = "hola"
#mensaje2 = "Hola"
#print(mensaje1 == mensaje2)

#formateo elegante de salida

#año = 2022
#evento = 'semana santa'
#print(f'lo mejor de las fiestas de {evento} del {año}')


#flor = 'rosas'
#print(f'el jardin de mi casa, esta llena de {flor!r}.')

#modelo = 'optimus tucan'
#precio = 1900000
#impuestos = precio * 19/100
#print(f'bicicleta {modelo}:${precio+impuestos} pesos')



#taller 
nombre_usuario = input("ingresa tu nombre \n")
print("¡Bienvenido, ", nombre_usuario, "!")
print(f"\n¡Bienvenido, {nombre_usuario}!\n")


#suma
#print("suma")
#num1 = float(input("ingresar el primer numero para la suma: "))
#num2 = float(input("ingresar el segundo numero para la suma: "))
#resultado = num1 + num2
#print(f'el resultado de la suma es: {resultado}\n')

#resta

#print("resta")
#num1 = float(input("ingresar el primer numero para la resta: "))
#num2 = float(input("ingresar el segundo numero para la resta: "))
#resultado = num1 - num2
#print(f'el resultado de la resta es: {resultado}\n')

# multiplicacion

#print("multiplicacion")
#num1 = float(input("ingresar el primer numero para la multiplicacion: "))
#num2 = float(input("ingresar el segundo numero para la multiplicacion: "))
#resultado = num1 * num2
#print(f'el resultado de la multiplicacion es: {resultado}\n')

#exponente

#print("exponente")
#num1 = float(input("ingresar la base del exponente: "))
#num2 = float(input("ingresar el exponente: "))
#resultado = num1 ** num2
#print(f'el resultado del exponente es: {resultado}\n')

#exponente 2

#print("exponente 2")
#num1 = float(input("ingresar el numero para elevarlo al cuadrado: "))
#resultado = num1 * num1 
#print(f'el resultado de la raiz cuadrada de {num1} es: {resultado}\n')

#division
#print("division")
#num1 = float(input("ingresar el primer numero para la division: "))
#num2 = float(input("ingresar el segundo numero para la division: "))
#if num2  != 0:
#resultado = num1 / num2
#print(f'el resultado de la division es: {resultado}\n')
#else
#print("error")
 
#modulo

#print("modulo")
#num1 = float(input("ingresar el primer numero: "))
#num2 = float(input("ingresar el segundo numero: "))
#resultado = (num1 + num2) * 100
#resta = num1 % num2
#print(f'El porcentaje de {num1} respecto a {num2} es: {porcentaje:}%')
#print(f'la resta de la división de {num1} entre {num2} es: {resta}')

#tipo de entero
#numero_entero = 15
#print(f'el numero {numero_entero} es de tipo: {type(numero_entero)}')

#tipo de dato flotante
#numero_float = 10.5
#print(f'el numero {numero_float} es de tipo: {type(numero_float)}')

#tipo de dato complejo

#numero_complejo = 5 + 6j
#print(f'el numero complejo {numero_complejo} es de tipo: {type(numero_complejo)}')

#tipo de dato cadena
#nombre ="jose"
#print(f'el texto "{nombre}" es de tipo: {type(nombre)}')



# taller
#numero entero
#numero_entero = input("ingresa un numero")
#print(f'el numero {numero_entero} es de tipo: {type(numero_entero)}')

#numero flotante
#numero_float = inpur("ingrese un numero decimal")
#print(f'el numero {numero_float} es de tipo: {type(numero_float)}')

#mumero complejo
#numero_complejo = input("ingresa un numero real y uno imaginario")
#print(f'el numero complejo {numero_complejo} es de tipo: {type(numero_complejo)}')

#cadena de texto
#cadena_texto = input("ingrese un nombre ")
#print(f'el texto "{cadena_texto}" es de tipo: {type(string)}')

#booleano
#num1 = input("ingrese un numero")
#num2 = input("ingrese un segundo numero")
#if num1 == 3 
#return True
#else num2 = 3
#return True
#else return False



#act 1

#if (True):
 #   print("se ha ingresado a la estructura de control condicional is")

#act 2
#num_1 == 6
#if num_1 == 5:
 #   print("el numero es 5")
#print("fin.")     



#print("sistema para calcular notas de un estudiante")
#name = input("dijitar el nombre del estudiante: ")
#nota_1 = int(input(name + "dijita nota 1: "))
#nota_2 = int(input(name + "dijita nota 2: "))
#nota_3 = int(input(name + "dijita nota 3: "))

#prom = (nota_1 + nota_2 + nota_3)/3
#if prom >= 3:
#    print("felicitaciones " + name + "aprovaste y tu promedio es: ", round( prom,2))
#else:
  #   print("lo sentimos " + name + "no aprovaste y tu promedio es: ", round( prom,2)
#print("fin.")


# uso de elif
#x = 5   
#if x == 5:
#    print("el numero es 5")
#elif x == 6:
#    print("el numero es 6 ")    
#elif x == 7:
#    print("el numero es 7")
#else:
#    print("numero no registrado")        


'''#print ("===========")
print("=conversor")
print("==============")
num_1 = int(input("¿cual es el numero que desea convertir?"))

if num_1 == 1:
    print("el numero es 'UNO'")
elif num_1 == 2:
    print("el numero es 'DOS'")
elif num_1 == 3:
    print("el numero es 'TRES'")
elif num_1 == 4:
    print("el numero es 'CUATRO'")
elif num_1 == 5:
    print("el numero es 'CINCO'")
elif num_1 == 6:
    print("el numero es 'SEIS'")
else:
    print("numero no registrado")
print("fin.")

'''


'''menu = """
bienvenidos al registro de usuarios, llene los campos que usted
prefiera a continuacion selecciona la opcion del 1 al 3:
(1) Dijitar nombre
(2) Dijitar edad
(3) Dijitar correo

"""
print(menu)
opcion = input("dijite opcion entre 1 y 3: ")
if opcion == "1":
    pass # comando de espera
elif opcion == "2":
    pass 
elif opcion == "3":
    pass 
else:
    print("debes dijitar un numero entre 1 y 3")
'''

'''#convertir una cadena a minusculas
cadena = "Hola jose"
print(cadena.lower())
'''

'''#convertir una cadena a mayusculas
cadena = "Hola jose"
print(cadena.upper())
'''

'''#convertir en viseversa
cadena = "Hola jose"
print(cadena.swapcase())
'''

'''#convertir una cadena aformato de titulo
cadena = "Hola jose"
print(cadena.title())
'''
'''
#Act 3.
print("=================")
print("=== Conversor ===")
print("=================\n")

print("Menú de opciones: \n")
menu = '''
#print("Presiona 1 para convertir de número a palabra.")
#print("Presiona 2 para convertir de palabra a número.")\n
'''
print(menu)
opcion = int(input("¿cuál es la opción deseada:  ?"))
if opcion == 1:
    print("\n Conversor de número a palabra. \n")
    opcion_uno = int(input("¿Cuál es el número que deseas convertir a palabra?: "))
    if opcion_uno == 1:
        print("El número es  'UNO' ")
    elif opcion_uno == 2:
        print("El número es  'DOS' ")
    elif opcion_uno == 3:
        print("El número es  'TRES' ")
    elif opcion_uno == 4:
        print("El número es  'CUATRO' ")
    elif opcion_uno == 5:
        print("El número es  'CINCO' ")
    else:
        print("El número seleccionado no está registrado.")

elif opcion == 2:
    print("\n Conversor de palabra a número. \n")
    opcion_dos = input("¿Cuál es la palabra que deseas convertir a número?:")
    opcion_dos = opcion_dos.lower() #Metodo .lower() convertir cadena de caracteres en minúsculas

    if opcion_dos == "uno":
        print ("El número es ' 1 '")
    elif opcion_dos == "dos":
        print ("El número es ' 2 '")
    elif opcion_dos == "tres":
        print ("El número es ' 3 '")
    elif opcion_dos == "cuatro":
        print ("El número es ' 4 '")
    elif opcion_dos == "cinco":
        print ("El número es ' 5 '")
    else:
        print("El número seleccionado no está registrado.")
else:
    print("\n Opción no valida")
print("fin.")
'''

# hacer esta catividad como tu gustes y simple
'''menu = """ 
Bienvenidos al registro de usuarios, llene los campos que usted 
prefiera a continuación seleccionando un número del 1 al 3: 
[1] Digitar su Nombre 
[2] Digitar su edad 
[3] Digitar su correo electrónico 
"""
print(menu)
opcion = input('Digita una opción entre 1 y 3: ')
if opcion == '1':
    nombre = input('Digita tu nombre: ')
    edad = input('digitar edad')
    print("tu nombre es:" + nombre)
    print("tu nombre es:", nombre)
    print('Tu nombre es {}'.format(nombre), 'tu edad es{}.'.format(edad))
elif opcion == '2':
    edad = input('Digita tu edad: ')
    print('Tu edad es:' + edad)
    print('Tu edad es:', edad)
    print('Tu edad es {}'.format(edad))
elif opcion == '3':
    email = input('Digita tu email: ')
    print('tu email es: ' + email)
    print('tu email es: ', email)
    print(f'tu email es: {email}')
else:
    print('Debes digitar un numero entre 1 y 3')
    print('=-='*20)
print("****** Gracias por usar nuestro servicio ******")
'''

#taller
'''menu = """ 
Bienvenidos al registro de usuarios, llene los campos que usted 
prefiera a continuación seleccionando un número del 1 al 3: 
[1] Digitar su Nombre 
[2] Digitar su edad 
[3] Digitar su correo electrónico 
"""
print(menu)
opcion = input('Digita una opción entre 1 y 3: ')
if opcion == '1':
    nombre = input('Digita tu nombre: ')
    if nombre.isalpha():
        print(f'tu nombre es: {nombre}')
    else:
        print("has dijitado un nombre no valido") 
elif opcion =='2':
    pass           
elif opcion =='3':
    pass 
else:
    print("debes dijitar un numero entre 1 y 3")


menu = """ Bienvenidos al registro de usuarios, llene los campos que usted
prefiera a continuación seleccionando un número del 1 al 3: 
[1] Digitar su Nombre 
[2] Digitar su edad 
[3] Digitar su correo electrónico 
"""
print(menu)
opcion = input('Digita una opción entre 1 y 3: ')
if opcion == '1':
    nombre = input('Digita tu nombre: ')
    if nombre.isalpha():#el metodo isalpha, es para str, y evalua si es una cadena de caracteres
        print('Tu nombre es {}'.format(nombre))
        print(f'Tu nombre es: {nombre}')
    else:
        print('Has digitado un nombre no valido...')
elif opcion == '2':
    edad = input('Digita tu edad: ')
    if edad.isnumeric(): #el metodo inumeric, es para datos numéricos,
        # y permite evaluar si edad es totalmente numérico
        edad = int(edad)  # Convierte la entrada a un entero
        if 0 <= edad <= 110:  # Verifica que la edad esté en el rango permitido
            print('Tu edad es {}'.format(edad))
            print(f'Tu edad es: {edad}')
        else:
            print('Has digitado una edad no valida...')
    else:
        print('Has digitado una edad no válida...')
elif opcion == '3':
    email = input('Digita tu email: ')
    if email.find('@')>=0 and email.find('.')>=0:#el metodo find que es buscar dentro de str 
        # una oracion o un caracter, y evalua si tiene caracteres especiales 
        print('Tu e-mail es {}'.format(email))
        print(f'tu email es: {email}')
    else:
        print('Has digitado un email no valido...')
else:
   print('Debes digitar un numero entre 1 y 3')
   print('=-='*20)
print('****'*10)



num1 = 20
num2 = 0

try:
    print("la division de {0} entre {1}".format(num1, num2(num1/num2)))
    result = num1 / num2
except ZeroDivisionError:
    print("error en la ejecucion del programa")

print("hasta aqui va  el programa")
'''







