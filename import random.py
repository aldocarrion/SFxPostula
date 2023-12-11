import random
num_sec = random.randint(1,100)
contador = 0
while True:
    entrada = input("Ingresa numero entre 1 y 100, 'Salir' para finalizar: ")
    if entrada == 'Salir':
        break
    if 1<= int(entrada) <= 100:

        
        print("Numero válido ingresado: "+entrada)
        #contador +=1
        if int(entrada) < num_sec:
            print("Numero ingresado es muy bajo")
            #contador +=1
        if int(entrada) > num_sec:
            print("Numero ingresado es muy alto")
            #contador +=1
        if int(entrada) == num_sec:
            print("Lo hiciste bien")
            print("Lo hiciste en "+str(contador)+" intentos")
            break
    else:
        print("Ingrese un numero válido")
        break

