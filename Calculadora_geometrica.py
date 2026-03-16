
print("CALCULADORA GEOMETRICA")
print("========================")

pi = 3.14159265359
option = "si"

while option == "si":
    figura = input("\nPor favor escriba el nombre de la figura Geometrica deseas calcular:\n"
    "FIGURAS 2D:\n"
    "1.Circulo\n"
    "2.Triangulo\n"
    "3.Rectangulo\n"
    "4.Pentagono\n"
    "5.Triangulo Rectangulo\n"
    "\nFIGURAS 3D:\n"
    "1.Esfera\n"
    "2.Cono\n"
    "3.Cilindro\n"
    "4.Prisma Rectangular\n""SALIR\n").lower()

if figura == "circulo":
    circulo=calculo=int(input("\nQue desea calcular exactamente del circulo, por favor escoja entre la opción: (1,2,3) \n1.Área:\n2.Radio:\n3.Circunferencia:\n"))
    if calculo== 1:
        radio=float(input("Por favor ingrese el radio en número decimal: "))
        area= pi * radio * radio
        print("El Área del circulo es:", area)
    elif calculo== 2:
            area=float(input("Por favor ingresa el área en número decimal: "))
            radio=(area / pi) ** 0.5
            print("El Radio  del circulo es:", radio)
    
    elif calculo== 3:
            radio=float(input("Por favor ingrese el radio en número decimal: "))
            circunferencia= 2 * pi * radio
            print("La Circunferencia del circulo es:", circunferencia)
    
if figura == "triangulo":
    triangulo=calculo=int(input("\nQue desea calcular exactamente del triangulo, por favor escoja entre la opción: (1,2,3,4) \n1.Área:\n2.Perímetro:\n3.Altura:\n4.Base:\n"))
    if calculo== 1:
        base=float(input("Por favor ingrese la base en número decimal: "))
        altura=float(input("Por favor ingrese la altura en número decimal: "))
        area= (base * altura) / 2
        print("El Área del triangulo es:", area)
    
    elif calculo== 2:
        a=float(input("Por favor ingrese el valor del primer lado(a) en número decimal: "))
        b=float(input("Por favor ingrese el valor del segundo lado(b) en número decimal: "))
        c=float(input("Por favor ingrese el valor del tercer lado(c) en número decimal: "))
        perimetro= a + b + c
        print("El Perimetro del triangulo es:", perimetro)
    
    elif calculo== 3:
        area=float(input("Por favor ingresa el área en número decimal: "))
        base=float(input("Por favor ingrese la base en número decimal: "))
        altura=(2 * area) / base
        print("La Altura del triangulo es de:", altura)
    
    elif calculo== 4:
        area=float(input("Por favor ingresa el área en número decimal: "))
        altura=float(input("Por favor ingrese la altura en número decimal: "))
        base= (2 * area) / altura
        print("La Base del triangulo es de:", base)

if figura== "rectangulo":
    rectangulo=calculo=int(input("\nQue desea calcular exactamente del rectangulo, por favor escoja entre la opción: (1,2,3,4,5) \n1.Área:\n2.Perímetro:\n3.Diagonal:\n4.Base:\n5.Altura:\n"))
    if calculo== 1:
        base=float(input("Por favor ingrese la base en número decimal: "))
        altura=float(input("Por favor ingrese la altura en número decimal: "))
        area= base * altura
        print("El Área del rectangulo es de:", area)
    elif calculo== 2:
        base=float(input("Por favor ingrese la base en número decimal: "))
        altura=float(input("Por favor ingrese la altura en número decimal: "))
        perimetro= 2 * (base + altura)
        print("El Perimetro del rectangulo es:", perimetro)
        
    elif calculo== 3:
        base=float(input("Por favor ingrese la base en número decimal: "))
        altura=float(input("Por favor ingrese la altura en número decimal: "))
        diagonal= (base**2 + altura**2) **0.5
        print("La Diagonal del rectangulo es:", diagonal)
    
    elif calculo== 4:
        area=float(input("Por favor ingresa el área en número decimal: "))
        altura=float(input("Por favor ingrese la altura en número decimal: "))
        base= area / altura
        print("La Base del rectangulo es:", base)
    
    elif calculo== 5:
        area=float(input("Por favor ingresa el área en número decimal: "))
        base=float(input("Por favor ingrese la base en número decimal: "))
        altura= area / base
        print("La Altura del rectangulo es:", altura)
        
if figura== "pentagono":
    pentagono=calculo=int(input("\nQue desea calcular exactamente del pentagono, por favor escoja entre la opcíon: (1,2,3) \n1.Perímetro:\n2.Área:\n3.Lado:\n"))
    if calculo== 1:
        lado=float(input("Ingrese el lado del pentagono en número decimal: "))
        perimetro= 5 * lado
        
    elif calculo== 2:
        perimetro=float(input("Por favor ingrese el perimetro en número decimal: "))
        apotema=float(input("Por favor ingrese la apotema: "))
        area= (perimetro * apotema) / 2
        print("El Área del pentagono es:", area)
        
    elif calculo== 3:
        perimetro=float(input("Por favor ingrese el perimetro en número decimal: "))
        lado= perimetro / 5
        print("El lado del pentagono es de:", lado)

if figura== "triangulo_rectangulo":
    triangulo_rectangulo=calculo=int(input("\nQue deseas calcular exactamente del tr"))
        
        
        
        
        
        
        
        
        
            

     option = input("\nDeseas calcular otra figura? (si/no): \n").lower()
print("\nGRACIAS POR USAR NUESTRA CALCULADORA GEOMETRICA!!")