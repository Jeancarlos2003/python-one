'''def nombre_de_la_funcion(valores):
    #acciones
    return valores

#funcion con parametro
def Hola(nombre):
    print(f"Hola{nombre}")
Hola(" jose")

def suma(n1,n2):
    print(n1 + n2)
suma(3,4)

def resta(a,b=4):
    return a - b
resultR = resta(5)
print(resultR)


def mul_por_5(num):
    print(f'{num} * 5 ={num * 5}')
    print("inicio de la multiplicacion por 5")
mul_por_5(1)
print("siguiente")
mul_por_5(2)
print("fin")
  

def suma( a=3, b=4):
    return a + b
#llamar a la funcion sin argumentos para usar los valores por defecto
resultS = suma()
print(resultS)

#sumar otros vallores
resultS_con_parametro = suma(5,6)
print(resultS_con_parametros)


def nummayor(n1,n2):
   return max (n1,n2)
print("realizar el calculo para determinar cual es el numero mayor")


n1 = int(input("dijitar numero 1: "))
n2 = int(input("dijitar numero 2: "))

mayor = nummayor(n1,n2)
print(f'el numero mayor es : {mayor}')



#clases y objetos

#____init___ es un metodo que permite inicializar atributos de un objeto
# tener en cuenta Def, de las funciones

class nombredelaclase(object): #viene heredado del objeto
    def __init__ (self, parametros):
        self.nombre = nombredelaclase
'''
class Persona(object):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def presentarse(self):
        print(f'Hola, soy {self.nombre} y tengo {self.edad} años')

#crear objeto de la clase persona 
Persona1 = Persona("juan", 30)#crear un objeto con n ombre y edad
Persona1.presentarse()   #llamar al metodo presentarse        
       
        















