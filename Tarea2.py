#No se necesita librerías extras, solo ejecutar el codigo

def binario(n):
    if(n==0):
        return ""
    else:
        return binario(n//2)+str(n%2)
    
def ContarDigitos(n):
    x = 0
    if(n>0):
        x = 1 + ContarDigitos(n//10)
        return x
    else:
        return 0
    
romanos = {'I': 1, 'V': 5, 'X': 10,'L': 50, 'C': 100, 'D': 500, 'M': 1000}
      
def ConvertirDecimales(n,x,total):
    if(len(n)==0):
        return 0
    else:
        alterno = n[0:len(n)-1]
        letra = n[len(n)-1:len(n)]
        valor = romanos[letra]
        if(x<=valor):
            x = valor
            total += ConvertirDecimales(alterno,x,total)+valor    
        else:
            x = valor
            total += ConvertirDecimales(alterno,x,total) -valor
    return total

def calcular_raiz(valor,aux):

    if(aux*aux==valor): 
        return aux
    elif(aux*aux>valor):
        return calcular_raiz_non(valor,aux-1)
    else:
        return calcular_raiz(valor,aux+1)
    
def calcular_raiz_non(valor,aux):
    multi = aux*aux
    resta = valor - multi
    return aux + (resta/(aux*2))
    
def suma_numeros_enteros(numero):
    if numero == 0:
        return 0
    else:
        return numero + suma_numeros_enteros(numero - 1)


while True:
    try:
        print("------------------------Menu------------------------")
        print("1) Convertir a binario")
        print("2) Contar digitos")
        print("3) Raíz cuadrada entera")
        print("4) Convertir a Decimal desde romano")
        print("5) Suma de numeros enteros")
        print("6) Salir")
  
        opcion = int(input("Escoja una opcion: "))
        if opcion ==1:
            print("Ha escogido convertir un numero a binario")
            n = int(input("Ingrese el numero a convertir: "))
            print()
            print("El numero ",n," en binario es: ",binario(n))
            print()
        elif opcion ==2:
            print("Ha escogido opcion 2")
            x = int(input("Ingrese el numero a contar: "))
            if(x==0):
                print()
                print("El numero ",x," tiene 1 digito")
                print()
            else:
                print()
                print("El numero ",x," tiene ",ContarDigitos(x)," digitos")
                print()
        elif opcion ==3:
            print("Ha escogido opcion 3")
            x = int(input("Ingrese el numero de la raiz que desea calcular: "))
            print()
            print("La raiz de ",x," es: ",calcular_raiz(x,1))
            print()
        elif opcion ==4:
            print("Ha escogido opcion 4")
            x = input("Ingrese el numero romano que desea convertir: ")
            if(len(x)==0):
                print("Ningun valor ingresado")
                print()
            else:
                print("El numero romano ",x," en decimales es: ",ConvertirDecimales(x,0,0))
                print()
        elif opcion ==5:
            print("Ha escogido opcion 5")
            x = int(input("Ingrese un numero entero que desea sumar desde 0: "))
            sum = suma_numeros_enteros(x)
            print("la suma de de los numeros enteros desde 0 a {} es {}".format(x,sum))
        elif opcion ==6:
            print("Hasta pronto")
            break
        else:
            print("opcion invalida")
    except ValueError as ve:
        print("Ingrese Valores Validos")