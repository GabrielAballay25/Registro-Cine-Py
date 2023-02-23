import os.path
import pickle
import random


# ----------------------------------------------------------------------------------------------------------------------
# Definicion de registro
class Videoteca:
    def __init__(self, titulo, genero, idioma):
        self.titulo = titulo
        self.genero = genero
        self.idioma = idioma


def to_string(videoteca):
    res = "\n"
    res += "_Titulo de la pelicula: " + videoteca.titulo + "   _"
    res += "Genero: " + generos_cadena(videoteca.genero) + "   _"
    res += "Idioma: " + idioma_cadena(videoteca.idioma) + ""
    return res


# ----------------------------------------------------------------------------------------------------------------------
# Validacion
def validar_rango(mensaje, maximo, minimo):
    numero = int(input(mensaje))
    while numero < minimo or numero > maximo:
        print("El numero ingresado es invalido")
        numero = int(input(mensaje))
    return numero


# ----------------------------------------------------------------------------------------------------------------------
# Mostrar por genero/idioma y no por codigo
def generos_cadena(genero):
    res = ""
    generos = ["Infantil", "Comedia", "Romantico", "Drama", "Ciencia Ficcion", "Otros"]
    res += generos[genero]
    return res


def idioma_cadena(idioma):
    res = ""
    idiomas = ["Español", "Ingles", "Francés", "Portugues", "Otros"]
    res += idiomas[idioma]
    return res


# ----------------------------------------------------------------------------------------------------------------------
# Punto 1
def cargar_archivo(numero, fd):
    m = open(fd, "wb")
    peliculas = ("Avatar", "Titanic", "Armagedon", "Hannibal", "Tiburón", "It", "Gladiator", "Frankenstein", "Dracula",
                 "Machete", "Candyman", "REC", "Matilda", "Carrie", "Saw", "Cars", "Zoolander", "Amadeus", "Shrek",
                 "Cleopatra", "Chucky", "Contratiempo", "Nerve", "Enredados", "Up", "Malefica", "Dumbo", "Metegol",
                 "Crepusculo", "Interestelar", "Anabelle", "Gost")

    for i in range(numero):
        titulo = random.choice(peliculas)
        genero = random.randint(0, 5)
        idiomas = random.randint(0, 4)

        pelis = Videoteca(titulo, genero, idiomas)
        pickle.dump(pelis, m)
        m.flush()

    m.close()


def generar_vector(fd):
    vec = []
    if not os.path.exists(fd):
        print("El archivo no existe")
        return

    m = open(fd, "rb")
    taman = os.path.getsize(fd)

    while m.tell() < taman:
        peliculas = pickle.load(m)
        add_in_order(vec, peliculas)

    m.close()
    return vec


def mostrar_vector(vector):
    for i in range(len(vector)):
        print(to_string(vector[i]))


def add_in_order(vector, peliculas):
    n = len(vector)
    pos = n
    izq, der = 0, n-1
    while izq <= der:
        centro = (izq + der) // 2
        if vector[centro].titulo == peliculas.titulo:
            pos = centro
            break
        if peliculas.titulo < vector[centro].titulo:
            der = centro - 1
        else:
            izq = centro + 1

    if izq > der:
        pos = izq

    vector[pos:pos] = [peliculas]


# ----------------------------------------------------------------------------------------------------------------------
# Punto 2
def generar_lista(vector, numero, genero):
    lista = []
    for i in range(len(vector)):
        if vector[i].genero == genero:
            lista.append(vector[i])
        if len(lista) == numero:
            return lista

    return lista


# ----------------------------------------------------------------------------------------------------------------------
# Punto 3
def generar_matriz(vector):
    matriz = [[0] * 5 for f in range(6)]
    for i in range(len(vector)):
        fila = vector[i].genero
        colum = vector[i].idioma
        matriz[fila][colum] += 1
    return matriz


def mostrar_matriz(matriz):
    genero = ["Infantil", "Comedia", "Romantico", "Drama", "Ciencia Ficcion", "Otros"]
    print("{:^24}".format("                ") + "|"  
          "{:^24}".format("Español") + "|"
          "{:^24}".format("Ingles") + "|"
          "{:^24}".format("Frances") + "|"
          "{:^24}".format("Portuges") + "|"
          "{:^24}".format("Otros") + "|")

    for f in range(len(matriz)):
        print("{:<23}".format(genero[f]),  "|", end="")
        for c in range(len(matriz[f])):
            if matriz[f][c] > 0:
                print("{:^23}".format(matriz[f][c]), "|", end="")
            else:
                print("{:^23}".format("X"), "|", end="")
            if c == (len(matriz[f])-1):
                print()


# ----------------------------------------------------------------------------------------------------------------------
# Punto 4
def determinar_cantidad(matriz, idioma):
    cantidad = 0
    for i in range(len(matriz)):
        cantidad += matriz[i][idioma]
    return cantidad


# ----------------------------------------------------------------------------------------------------------------------
# Punto 5
def buscar_en_arreglo(vector, titulo):
    pos = None
    izq, der = 0, len(vector) - 1
    while izq <= der:
        cen = (izq + der) // 2
        if titulo == vector[cen].titulo:
            pos = cen
            break
        if titulo < vector[cen].titulo:
            der = cen - 1
        else:
            izq = cen + 1

    return pos


# ----------------------------------------------------------------------------------------------------------------------
# Punto 6
def generar_archivo_texto(idioma, vector):
    arc_tex = "PeliculasIdioma"+str(idioma)+".txt"
    m = open(arc_tex, "wt")
    for i in range(len(vector)):
        if vector[i].idioma == idioma:
            m.write(to_string(vector[i]))
            m.flush()
    m.close()


# ----------------------------------------------------------------------------------------------------------------------
# Principal
def test():
    opcion = -1
    fd = "peliculas.dat"
    vector = None
    matriz = None
    while opcion != 7:
        print('\n'"Bienvenido al menu de videoteca")
        print()
        print("╔═══════════════════════════════════════════════════════════╗")
        print("║ 1- Generar y mostrar vector.                     ║")
        print("║ 2- Generar lista de peliculas.                   ║")
        print("║ 3- Determinar peliculas por idioma y genero.     ║")
        print("║ 4- Determinar peliculas para determinado idioma. ║")
        print("║ 5- Buscar pelicula por determinado titulo.       ║")
        print("║ 6- Generar archivo por determinado idioma.       ║")
        print("║ 7- Salir.                                        ║")
        print("╚═══════════════════════════════════════════════════════════╝")
        print()

        opcion = int(input("Ingrese una opcion: "))
        print("-" * 300)

        if opcion == 1:
            numero = int(input("Ingrese la cantidad de peliculas que desea registrar: "))
            cargar_archivo(numero, fd)
            vector = generar_vector(fd)
            print("\nEl vector generado es: ")
            mostrar_vector(vector)
            print("-" * 300)

        elif opcion == 2:
            if vector:
                tamanio = int(input("Ingrese la cantidad de peliculas que quiere agregar a la lista: "))
                genero = int(input("Ingrese el genero de las peliculas a listar: "))
                lista = generar_lista(vector, tamanio, genero)
                if len(lista) < tamanio:
                    print("\nNo hay suficientes peliculas del genero")
                mostrar_vector(lista)
            else:
                print("El vector esta vacio, debe cargarlo para generar la lista!!!!!")
            print("-" * 300)

        elif opcion == 3:
            if vector:
                matriz = generar_matriz(vector)
                mostrar_matriz(matriz)
            else:
                print("El vector esta vacio, debe cargarlo para generar la matriz!!!!!")
            print("-" * 300)

        elif opcion == 4:
            if matriz:
                idiom = validar_rango("Ingrese el idioma(0-Español, 1-Inglés, 2-Francés, 3-Portugués, 4-Otros): ", 4, 0)
                cantidad = determinar_cantidad(matriz, idiom)
                print("La cantidad de peliculas para el idioma es: ", cantidad)
            else:
                print("La matriz no ha sido cargada")
            print("-" * 300)

        elif opcion == 5:
            if vector:
                titulo = input("Ingrese el titulo de la pelicula que desea buscar: ")
                posicion = buscar_en_arreglo(vector, titulo)
                if posicion:
                    print(to_string(vector[posicion]))
                else:
                    print("El titulo no fue encontrado")
            else:
                print("El vector no esta cargado!")
            print("-" * 300)

        elif opcion == 6:
            if vector:
                idioma = validar_rango("Ingrese el idioma(0-Español, 1-Inglés, 2-Francés, 3-Portugués, 4-Otros): ", 4, 0)
                generar_archivo_texto(idioma, vector)
            else:
                print("El vector no fue cargado!!")
            print("-" * 300)

        elif opcion == 7:
            print("---Fin del programa---")


test()
