def suma(a,b):
    return a + b


def resta(a,b):
    return a - b


def multiplicacion(a,b):
    return a * b


def division(a,b):
    if b != 0:
        return a / b
    else:
        return "error : division por cero"
    
    
def mostrar_menu():
    print("calculadora basica")
    print("1, suma")
    print("2, resta")
    print("3, multiplicacion")
    print("4, division")
    print("salir")


while True:
    mostrar_menu()
    opcion = input("elige una opcion: ")
    if opcion == "5":
        print("saliendo del programa")
        break


    if opcion in ["1", "2", "3", "4"]:
        num1 = float(input("ingresa el primer numero"))
        num2 = float(input("ingresa el segundo numero"))

        if opcion == "1":
            print(f"Resultado: {suma(num1, num2)}")
        elif opcion == "2":
            print(f"Resultado: {resta(num1, num2)}")
        elif opcion == "3":
            print(f"Resultado: {multiplicacion(num1, num2)}") 
        elif opcion == "4":
            print(f"Resultado: {division(num1, num2)}") 

    else:
        print("opvion no valida, intentar nuevamente")




































































