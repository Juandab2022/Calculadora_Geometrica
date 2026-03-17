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
        calculo = int(input("\n1.Area\n2.Radio\n3.Circunferencia\n"))

        if calculo == 1:
            radio = float(input("Radio: "))
            area = pi * radio * radio
            print("Área:", area)

        elif calculo == 2:
            area = float(input("Área: "))
            radio = (area / pi) ** 0.5
            print("Radio:", radio)

        elif calculo == 3:
            radio = float(input("Radio: "))
            circunferencia = 2 * pi * radio
            print("Circunferencia:", circunferencia)

        else:
            print("Opción inválida")



    elif figura == "triangulo":
        calculo = int(input("\n1.Area\n2.Perimetro\n3.Altura\n4.Base\n"))

        if calculo == 1:
            base = float(input("Base: "))
            altura = float(input("Altura: "))
            area = (base * altura) / 2
            print("Área:", area)

        elif calculo == 2:
            a = float(input("Lado a: "))
            b = float(input("Lado b: "))
            c = float(input("Lado c: "))
            print("Perímetro:", a + b + c)

        elif calculo == 3:
            area = float(input("Área: "))
            base = float(input("Base: "))
            altura = (2 * area) / base
            print("Altura:", altura)

        elif calculo == 4:
            area = float(input("Área: "))
            altura = float(input("Altura: "))
            base = (2 * area) / altura
            print("Base:", base)

        else:
            print(" Opción inválida")


    elif figura == "rectangulo":
        calculo = int(input("\n1.Area\n2.Perimetro\n3.Diagonal\n4.Base\n5.Altura\n"))

        if calculo == 1:
            base = float(input("Base: "))
            altura = float(input("Altura: "))
            print("Área:", base * altura)

        elif calculo == 2:
            base = float(input("Base: "))
            altura = float(input("Altura: "))
            print("Perímetro:", 2 * (base + altura))

        elif calculo == 3:
            base = float(input("Base: "))
            altura = float(input("Altura: "))
            print("Diagonal:", (base**2 + altura**2) ** 0.5)

        elif calculo == 4:
            area = float(input("Área: "))
            altura = float(input("Altura: "))
            print("Base:", area / altura)

        elif calculo == 5:
            area = float(input("Área: "))
            base = float(input("Base: "))
            print("Altura:", area / base)

        else:
            print(" Opción inválida")



    elif figura == "pentagono":
        calculo = int(input("\n1.Perimetro\n2.Area\n3.Lado\n"))

        if calculo == 1:
            lado = float(input("Lado: "))
            print("Perímetro:", 5 * lado)

        elif calculo == 2:
            perimetro = float(input("Perímetro: "))
            apotema = float(input("Apotema: "))
            print("Área:", (perimetro * apotema) / 2)

        elif calculo == 3:
            perimetro = float(input("Perímetro: "))
            print("Lado:", perimetro / 5)

        else:
            print(" Opción inválida")


    elif figura == "triangulo rectangulo":
        calculo = int(input("\n1.Hipotenusa\n2.Area\n3.Perimetro\n"))

        if calculo == 1:
            a = float(input("Cateto 1: "))
            b = float(input("Cateto 2: "))
            print("Hipotenusa:", (a**2 + b**2) ** 0.5)

        elif calculo == 2:
            base = float(input("Base: "))
            altura = float(input("Altura: "))
            print("Área:", (base * altura) / 2)

        elif calculo == 3:
            a = float(input("Cateto 1: "))
            b = float(input("Cateto 2: "))
            c = float(input("Hipotenusa: "))
            print("Perímetro:", a + b + c)

        else:
            print(" Opción inválida")



    elif figura == "esfera":
        calculo = int(input("\n1.Volumen\n2.Area\n3.Diametro\n"))

        if calculo == 1:
            r = float(input("Radio: "))
            print("Volumen:", (4/3) * pi * r**3)

        elif calculo == 2:
            r = float(input("Radio: "))
            print("Área:", 4 * pi * r**2)

        elif calculo == 3:
            r = float(input("Radio: "))
            print("Diámetro:", 2 * r)

        else:
            print(" Opción inválida")



    elif figura == "cono":
        calculo = int(input("\n1.Volumen\n2.Area lateral\n"))

        if calculo == 1:
            r = float(input("Radio: "))
            h = float(input("Altura: "))
            print("Volumen:", (1/3) * pi * r**2 * h)

        elif calculo == 2:
            r = float(input("Radio: "))
            g = float(input("Generatriz: "))
            print("Área lateral:", pi * r * g)

        else:
            print(" Opción inválida")



    elif figura == "cilindro":
        calculo = int(input("\n1.Volumen\n2.Area lateral\n3.Area total\n"))

        if calculo == 1:
            r = float(input("Radio: "))
            h = float(input("Altura: "))
            print("Volumen:", pi * r**2 * h)

        elif calculo == 2:
            r = float(input("Radio: "))
            h = float(input("Altura: "))
            print("Área lateral:", 2 * pi * r * h)

        elif calculo == 3:
            r = float(input("Radio: "))
            h = float(input("Altura: "))
            print("Área total:", 2 * pi * r * (h + r))

        else:
            print(" Opción inválida")



    elif figura == "prisma rectangular":
        largo = float(input("Largo: "))
        ancho = float(input("Ancho: "))
        altura = float(input("Altura: "))
        print("Volumen:", largo * ancho * altura)



    elif figura == "salir":
        print("\nGRACIAS POR USAR LA CALCULADORA")
        break



    else:
        print(" Opción inválida, intenta nuevamente")
        continue



    option = input("\nDeseas calcular otra figura? (si/no): ").lower()

print("\nPrograma finalizado")
