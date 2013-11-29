
############################
# Practicando en Python
# Calcula area de figuras geometricas
############################


def area_rectangulo(b,h):
        """Funcion que hace operacion para calcular area de rectangulo"""
        area = b*h
        print "El area es: ",area

def area_cuadrado(lado):
        """Funcion que hace operacion para calcula el area de un cuadrado"""
        area = lado**2
        print "El area es: ",area


def area_radio(radio):
        """Funcion que hace operacion para calcular area de circulo, en base al radio"""
        pi = 3.1416
        area = radio**2*pi
        print "El area es: ",area

def area_diametro(diametro):
        """Funcion que hace operacion para calcular area de circulo, en base al diametro"""
        pi = 3.1416
        radio = diametro / 2
        area = radio**2*pi
        print "El area es: ",area

def area_figura():
        """En esta funcion decides de que figura deseas obtener el area"""
        print "Este programa de calcula area de 'circulo', 'cuadrado' y 'rectangulo'"
        figura = raw_input("De que figura deseas obtener area?: ")
        if figura == "circulo":
                area_circulo()
        elif figura == "cuadrado":
                lado = int(raw_input("introduce el valor de un lado: "))
                area_cuadrado(lado)
        elif figura == "rectangulo":
                b = int(raw_input("introduce el valor de la base: "))
                h = int(raw_input("introduce el valor de la altura: "))
                area_rectangulo(b,h)
        else:
                print "Introduzca un valor correcto, 'circulo', 'cuadrado' o rectangulo'"

def area_circulo():
        """Si elegiste en la funcion area_figura() 'circulo', se pasara a esta opcion, aqui
decides si usar diametro o radio para obtener el area"""
        diametro_o_radio = raw_input("Desea obtener area de circulo con 'radio' o 'diametro?: ")
        if diametro_o_radio == "radio":
                radio_1 = int(raw_input("introduce el valor del radio: "))
                area_radio(radio_1)
        elif diametro_o_radio == "diametro":
                diametro_1 = int(raw_input("introduce el valor del diametro: "))
                area_diametro(diametro_1)
        else:
                print "introduzca un valor correcto, 'radio' o 'diametro'"

while True:
        """bucle principal del programa"""
        print "Programa que calcula el area de figuras Geometrias"
        area_figura()
