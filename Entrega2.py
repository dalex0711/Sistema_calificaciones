import sys
import os #Importando librerias que me serviran posteriormente para salir del programa y limpiar la terminal.


def limpiar ():
    os.system("cls" if os.name == "nt" else "clear") #Ejecutando comando para limpiar la terminal (dependiento del SO) con ayuda de la libreria os



def validar_nota():
    while True:
        try:
            nota = float(input(" - Ingresa una calificacion: "))
            if  0  <= nota <= 100:
                break
            else:
                print(" * Las notas deben ser entre (0-100)")
            
        except ValueError:
            print(" * Error: no es un número decimal válido")

    return nota

def estado(): # En está función encontraremos todo el proceso:

    limpiar()
    print("---------\n\033[1mOPCIÓN 1\033[0m  \n---------")
    print("Determinaremos el estado de aprobación: (Siendo 6.0 la nota aprobatoria)\n")
    
    calificacion = validar_nota()

    if calificacion <6.0:
      print(f" = Con la nota {calificacion} estás |reprobado| ¡Sigue intentando!\n")
    else:
      print(f" = Con la nota {calificacion} estás |aprobado| ¡Felicidades!\n")
    
def validar_lista():

    while True:
        notas = (input(" - Ingresa las notas seperadas por comas: ")).replace(" ","")
    
        if "," in notas:

            lista_final = []
            try:
                for lista_notas in notas.split(","): 
                    lista_notas = float(lista_notas)  

                    if lista_notas >= 0 and lista_notas <=100:
                        lista_final.append(lista_notas)  
                    else:
                        print(" * Las notas deben ser entre (0-100)")
                        break
                else: 
                 break
                
            except:
                    print(" * Debes ingresar las notas separadas por comas y no pueden ser caracteres. Ejemplo: (5.0, 4.0, 2.0)")   
        else:
            print(" * No puedes ingresar caracteres. Solo puedes ingresar notas, por ejemplo: (5.0, 4.0, 2.0)")

    return lista_final


def promedio(): # 2

    limpiar()
    print("---------\n\033[1mOPCIÓN 2\033[0m  \n---------")
    print("Calcularemos el promedio de la notas ingresadas.\n")
    
                 
    lista_calificacion = validar_lista()

    suma_notas = 0

    for lista_calificaciones in lista_calificacion:    
        suma_notas += lista_calificaciones
        promedio = suma_notas / len(lista_calificacion)

    print (f" = El promedio de las notas {lista_calificacion} es: {promedio:.2f} ")     
    return     

        
def comparar(): # 3
        
        limpiar()
        print("---------\n\033[1mOPCIÓN 3\033[0m  \n---------")
        print("Ingresaras un listado notas y contaremos cuántas calificaciones en la lista son mayores que este valor\n")

        lista = validar_lista()
        nota = validar_nota()
        
        lista_igual = []; i = 0; aprobados = 0

        while i < len(lista):
            if lista[i] == nota:
                  lista_igual.append(lista[i])
                  aprobados += 1
            i += 1
        print(f" = Cantidad de número mayores de {nota} de las calificaciones: {lista} fueron {aprobados}.")
        return


def verificar():
     
    limpiar()
    print("---------\n\033[1mOPCIÓN 4\033[0m  \n---------")
    print("Ingresaras un listado notas y verificaremos cuántas calificaciones en la lista son iguales que este valor\n")
    lista = validar_lista()
    nota = validar_nota()
    numero_de_veces = 0

    for x in lista:
        if x != nota:
            continue    
        else:
            numero_de_veces += 1
    print(f" = En las calificaciones: {lista} La nota: {nota} aparece {numero_de_veces} veces.")

    return

def salir():
    limpiar()
    print("\n----------------------------------")
    print("  Proceso finalizado.")
    print("¡Que tengas un excelente día!")
    print("----------------------------------\n")

    sys.exit()

def menu():
    
    while True:
        limpiar()

        print("\033[1m\nOPCIONES DE MENU \033[0m \n")
        print("\033[1m 1. \033[0m Resultado de evaluación [Aprobado o Reprobado]")
        print("\033[1m 2. \033[0m Calcular el promedio")
        print("\033[1m 3. \033[0m Comparar notas de una lista de notas")
        print("\033[1m 4. \033[0m Veces que aparece n notas de una lista de notas")
        print("\033[1m 5. \033[0m Salir")
        
        opcion = input("\033[1m\nIngrese la opción deseada:\033[0m ")
        
        if opcion == "1":
            estado()
        elif opcion == "2":
            promedio()
        
        elif opcion == "3":  
            comparar()  

        elif opcion == "4":  
            verificar()  

        elif opcion == "5":
            salir()
            break
            
        else:
            print("\033[1m Opción inválida. Intente nuevamente. \033[0m")

        continuar = input(" -- Si deseas regresar al menu presiona si, de lo contrario cualquier caracter: ")
        
        if continuar.lower() != "si":
           salir()

           
menu()