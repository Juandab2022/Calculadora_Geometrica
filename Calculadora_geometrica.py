print("========================")
print("CALCULADORA GEOMETRICA")
print("========================")

pi = 3.14159265359
option = "si"

while option == "si":
    
    figura = input("\nPor favor escriba el nombre de la figura Geometrica que deseas calcular:\n"
    "FIGURAS 2D:\n"
    "Circulo\n"
    "Triangulo\n"
    "Rectangulo\n"
    "Pentagono\n"
    "Triangulo Rectangulo\n"
    "\nFIGURAS 3D:\n"
    "Esfera\n"
    "Cono\n"
    "Cilindro\n"
    "Prisma Rectangular\n"
    "SALIR\n").lower()



    if figura == "circulo":
        calculo = int(input("\nQue desea calcular exactamente del circulo, por favor escoja entre la opción: (1,2,3) \n1.Area\n2.Radio\n3.Circunferencia\n"))

        if calculo == 1:
            radio = float(input("Por favor ingrese el radio en número decimal: "))
            print("El Área del circulo es:", pi * radio * radio)

        elif calculo == 2:
            area = float(input("Por favor ingresa el área en número decimal: "))
            print("El Radio del circulo es:", (area / pi) ** 0.5)

        elif calculo == 3:
            radio = float(input("Por favor ingrese el radio en número decimal: "))
            print("La Circunferencia del circulo es:", 2  * pi * radio)

        else:
            print("Opción inválida")



    elif figura == "triangulo":
        calculo = int(input("\nQue desea calcular exactamente del triangulo, por favor escoja entre la opción: (1,2,3,4) \n1.Area\n2.Perimetro\n3.Altura\n4.Base\n"))

        if calculo == 1:
            base = float(input("Por favor ingrese la base en número decimal: "))
            altura = float(input("Por favor ingrese la altura en número decimal: "))
            area = (base * altura) / 2
            print("El Área del triangulo es:", (base * altura) / 2)

        elif calculo == 2:
            a = float(input("Por favor ingrese el valor del primer lado(a) en número decimal: "))
            b = float(input("Por favor ingrese el valor del segundo lado(b) en número decimal: "))
            c = float(input("Por favor ingrese el valor del tecer lado(c) en número decimal: "))
            print("El Perímetro del triangulo es:", a + b + c)

        elif calculo == 3:
            area = float(input("Por favor ingresa el área en número decimal: "))
            base = float(input("Por favor ingrese la base en número decimal: "))
            print("La Altura del triangulo es:", (2 * area) / base)

        elif calculo == 4:
            area = float(input("Por favor ingresa el área en número decimal: "))
            altura = float(input("Por favor ingrese la altura en número decimal: "))
            print("La Base del triangulo:", (2 * area) / altura)

        else:
            print(" Opción inválida")


    elif figura == "rectangulo":
        calculo = int(input("\nQue desea calcular exactamente del rectangulo, por favor escoja entre la opción: (1,2,3,4,5) \n1.Area\n2.Perimetro\n3.Diagonal\n4.Base\n5.Altura\n"))

        if calculo == 1:
            base = float(input("Por favor ingrese la base en número decimal: "))
            altura = float(input("Por favor ingrese la altura en número decimal: "))
            print("El Área del rectangulo es:", base * altura)

        elif calculo == 2:
            base = float(input("Por favor ingrese la base en número decimal: "))
            altura = float(input("Por favor ingrese la altura en número decimal: "))
            print("El Perímetro del rectangulo es:", 2 * (base + altura))

        elif calculo == 3:
            base = float(input("Por favor ingrese la base en número decimal: "))
            altura = float(input("Por favor ingrese la altura en número decimal: "))
            print("La Diagonal del rectangulo es:", (base**2 + altura**2) ** 0.5)

        elif calculo == 4:
            area = float(input("Por favor ingresa el área en número decimal: "))
            altura = float(input("Por favor ingrese la altura en número decimal: "))
            print("La Base del rectangulo es:", area / altura)

        elif calculo == 5:
            area = float(input("Por favor ingresa el área en número decimal: "))
            base = float(input("Por favor ingrese la base en número decimal: "))
            print("La Altura del rectangulo es:", area / base)

        else:
            print(" Opción inválida")



    elif figura == "pentagono":
        calculo = int(input("\n1.Perimetro\n2.Area\n3.Lado\n"))

        if calculo == 1:
            lado = float(input("Ingrese el lado del pentagono en número decimal: "))
            print("El Perímetro del pentagono es:", 5 * lado)

        elif calculo == 2:
            perimetro = float(input("Por favor ingrese el perimetro en número decimal: "))
            apotema = float(input("Por favor ingrese la apotema: "))
            print("El Área del pentagono es:", (perimetro * apotema) / 2)

        elif calculo == 3:
            perimetro = float(input("Por favor ingrese el perimetro en número decimal: "))
            print("El Lado del pentagono es:", perimetro / 5)

        else:
            print(" Opción inválida")


    elif figura == "triangulo rectangulo":
        calculo = int(input("\n1.Hipotenusa\n2.Area\n3.Perimetro\n"))

        if calculo == 1:
            a = float(input("Por favor ingrese el valor del cateto 1(NÚMERO DECIMAL): "))
            b = float(input("Por favor ingrese el valor del cateto 2(NÚMERO DECIMAL): "))
            print("La Hipotenusa del triangulo rectangulo es:", (a**2 + b**2) ** 0.5)

        elif calculo == 2:
            base = float(input("Por favor ingrese la base en número decimal: "))
            altura = float(input("Por favor ingrese la altura en número decimal: "))
            print("El Área del triangulo rectangulo es:", (base * altura) / 2)

        elif calculo == 3:
            a = float(input("Por favor ingrese el valor del cateto 1(NÚMERO DECIMAL): "))
            b = float(input("Por favor ingrese el valor del cateto 2(NÚMERO DECIMAL): "))
            c = float(input("Por favor ingrese el valor de la hipotenusa(NÚMERO DECIMAL): "))
            print("El Perímetro del triangulo rectangulo es:", a + b + c)

        else:
            print(" Opción inválida")



    elif figura == "esfera":
        calculo = int(input("\nQue deseas calcular exactamente de la esfera, por favor escoja entre la opcíon: (1,2,3) \n1.Volumen\n2.Area\n3.Diametro\n"))

        if calculo == 1:
            r = float(input("Por favor ingrese el radio en número decimal: "))
            print("El Volumen de la esfera es:", (4/3) * pi * r**3)

        elif calculo == 2:
            r = float(input("Por favor ingrese el radio en número decimal: "))
            print("El Área de la esfera es:", 4 * pi * r**2)

        elif calculo == 3:
            r = float(input("Por favor ingrese el radio en número decimal: "))
            print("El Diámetro de la esfera es:", 2 * r)

        else:
            print(" Opción inválida")



    elif figura == "cono":
        calculo = int(input("\nQue deseas calcular exactamente del cono, por favor escoja entre la opcíon: (1,2,3,4) \n1.Volumen:\n2.Área lateral:\n3.Área total:\n4.Generatriz:\n"))

        if calculo == 1:
            r = float(input("Por favor ingrese el radio en número decimal: "))
            altura = float(input("Por favor ingrese la altura en número decimal: "))
            print("El Volumen del cono es:", (1/3) * pi * r**2 * altura)

        elif calculo == 2:
            r = float(input("Por favor ingrese el radio en número decimal: "))
            generatriz = float(input("Por favor ingrese la generatriz en número decimal: "))
            print("El Área lateral del cono es:", pi * r * generatriz)

        elif calculo== 3:
            r = float(input("Por favor ingrese el radio en número decimal: "))
            generatriz = float(input("Por favor ingrese la generatriz en número decimal: "))
            print("El área total del cono es:", pi * r * (r + generatriz))
            
        elif calculo== 4:
            r = float(input("Por favor ingrese el radio en número decimal: "))
            altura = float(input("Por favor ingrese la altura en número decimal: "))
            print("La generatriz del cono es:", (r**2 + altura**2) **0.5)

        else:
            print(" Opción inválida")



    elif figura == "cilindro":
        calculo = int(input("\nQue deseas calcular exactamente del cilindro, por favor escoja entre la opcíon: (1,2,3) \n1.Volumen\n2.Area lateral\n3.Area total\n"))

        if calculo == 1:
            r = float(input("Por favor ingrese el radio en número decimal: "))
            altura = float(input("Por favor ingrese la altura en número decimal: "))
            print("El Volumen del cilindro es:", pi * r**2 * altura)

        elif calculo == 2:
            r = float(input("Por favor ingrese el radio en número decimal: "))
            altura = float(input("Por favor ingrese la altura en número decimal: "))
            print("El Área lateral del cilindro es:", 2 * pi * r * altura)

        elif calculo == 3:
            r = float(input("Por favor ingrese el radio en número decimal: "))
            altura = float(input("Por favor ingrese la altura en número decimal: "))
            print("El Área total del cilindro es:", 2 * pi * r * (altura + r))

        else:
            print(" Opción inválida")



    elif figura == "prisma rectangular":
        calculo=int(input("\nQue deseas calcular exactamente del prisma rectangular, por favor escoja entre la opcíon: (1,2,3,4) \n1.Volumen:\n2.Área lateral:\n3.Área total:\n4.Diagonal del prisma:\n"))

        if calculo == 1:
            largo=float(input("Por favor ingrese el largo en número decimal: "))
            ancho=float(input("Por favor ingrese el ancho en número decimal: "))
            altura=float(input("Por favor ingrese la altura en número decimal: "))
            print("El Volumen del prisma rectangular es:", largo * ancho * altura)

        elif calculo== 2:
            altura=float(input("Por favor ingrese la altura en número decimal: "))
            largo=float(input("Por favor ingrese el largo en número decimal: "))
            ancho=float(input("Por favor ingrese el ancho en número decimal: "))
            print("El área lateral del prisma rectangular es de:", 2* altura * (largo + ancho))

        elif calculo== 3:
            largo=float(input("Por favor ingrese el largo en número decimal: "))
            ancho=float(input("Por favor ingrese el ancho en número decimal: "))
            altura=float(input("Por favor ingrese la altura en número decimal: "))
            print("El área total del prisma rectangular es:", 2 * (largo*ancho + largo*altura + ancho*altura))

        elif calculo== 4:
            largo=float(input("Por favor ingrese el largo en número decimal: "))
            ancho=float(input("Por favor ingrese el ancho en número decimal: "))
            altura=float(input("Por favor ingrese la altura en número decimal: "))
            print("El diagonal del prisma es de:", (largo**2 +  ancho**2 + altura**2) ** 0.5)

        else:
            print(" Opción inválida")



    elif figura == "salir":
        print("\nGRACIAS POR USAR LA CALCULADORA")
        option = "no"



    else:
        print(" Opción inválida, intenta nuevamente")
        continue
    

    if figura != "salir":
        option = input("\nDeseas calcular otra figura? (si/no): ").lower()


print("\nPrograma finalizado")
