import time
import os, re, statistics, json
from collections import Counter
#intenta importar modulos externos a pip si no los encuentra, los instala mediante el requeriments.txt
try:
  import requests, matplotlib.pyplot as plt, numpy as np
  from openpyxl import Workbook
  from openpyxl import load_workbook
except ImportError as e:
  print("El programa necesita módulos externos, instalando...")
  os.system("pip install -r Documentacion/requirements.txt")
  print("Reinicie el programa")
  os.system("pause")
  exit()
try:
  import funciones2
except ModuleNotFoundError:
  print("Debe tener el programa 'Funciones2.py' para que pueda funcionar")
  input("Enter para continuar")
  exit()
tiempo_actual = time.time()
# Formatear el timestamp como una cadena sin dos puntos
tiempo = time.strftime("_[%Y-%m-%d_%H-%M-%S]", time.localtime(tiempo_actual))


def clean():
  #Realiza la limpieza de pantalla, ya sea windows o linux
  if os.name == "posix":
    os.system("clear")
  elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    os.system("cls")


def consulta():
  #Realiza la consulta de id al form
  print("Consulta de pokemón\n")
  print("Ingrese el número de un pokemón a continuación:\n")
  i = exc_int()
  url = "https://pokeapi.co/api/v2/pokemon-form/" + str(i)
  try:
    r = requests.get(url)

  except (ConnectionError, Exception) as Cs:
    #si el programa no esta conectado a internet, se cierra
    print("Error de conexiÓn, debe conectarse a internet..")
    time.sleep(6)
    exit()
  except:
    print("Error desconocido..")
    time.sleep(6)
    exit()

  if r.status_code == 200:
    datos = json.loads(r.text)
    if datos:
      print("La conexión ha sido exitosa!\n")
    else:
      #Extrae los datos de json y se empieza a estructurar el diccionario
      print("La informaciÓn no pudo ser extraida")
    pokemon = datos.get("pokemon", [])
    generation = datos.get("version_group", [])
    elementos = list()
    for x, y in pokemon.items():
      if "http" in y and x == "url":
        r2 = requests.get(y)
        infoextra = json.loads(r2.text)
        for x, y in infoextra.items():
          #se empieza a estructurar los datos por listas y se extrea la informacion solicitada
          if x == "name":
            print(x + ": ", y)
            elementos.append(x + ":" + y)
          if x == "abilities":
            for habilidad in y:
              for x, y in habilidad.items():
                if x == "ability":
                  for Clave, valor in y.items():
                    if Clave != "url":
                      print("ability: ", valor)
                      elementos.append("ability: " + valor)
          if x == "height":
            y = y * .10
            y = str(round(y, 1)) + "m"
            print(x + ":", y)
            elementos.append(x + ":" + str(y))
          if x == "id":
            print(x + ": ", y)
            elementos.append(x + ":" + str(y))
            id = y
          if x == "base_experience":
            print(x + ": ", y)
            elementos.append(x + ":" + str(y))
          if x == "weight":
            y = y / 10
            y = str(y) + "kg"
            print(x + ":", y)
            elementos.append(x + ":" + str(y))
          if x == "types":
            for tipo in y:
              for x, y in tipo.items():
                if x == "type":
                  for Clave, valor in y.items():
                    if Clave != "url":
                      print("NameType: ", valor)
                      elementos.append("type: " + valor)
    #Se realiza la segunda estructura del diccionario
    for x, y in generation.items():
      if "http" in y and x == "url":
        r2 = requests.get(y)
        infoextra = json.loads(r2.text)
        for x, y in infoextra.items():
          #Se realiza la estructura mediante listas y se extrae lo solicitado
          if x == "generation":
            for Clave, Valor in y.items():
              if Clave == "name":
                print("Generation: ", Valor)
                elementos.append("Generation: " + Valor)
    dir = "pokemons/" + str(i) + ".txt"
    dir3 = str(i) + str(tiempo) + ".txt"
    comp = "pokemons/" + dir3
    file, dir2 = historial()

    if str(i) + ".txt" in file:
      #Si la busqueda concuerda con id ya creado, se cierra y no guarda
      input("Ya existe un registro con este ID, enter para continuar")
      clean()
    else:
      Cn = str(
          input("Desea agregar esta información a un archivo de texto(S/N): "))
      while True:
        #Estilo de ciclo para verificar que el usuario ingrese una opcion valida para
        #la impresion
        if Cn == "S" or Cn == "s":
          fo = open(comp, 'a')
          for elemento in elementos:
            fo.write(str(elemento) + "\n")
          fo.close()
          fo = open(dir, 'a')
          fo.write(str(dir3))
          fo.close()
          print("Información guardada correctamente, regreso al menú..")
          time.sleep(2)
          clean()
          break
        elif Cn == "N" or Cn == "n":
          print("Regresando al menu..")
          time.sleep(2)
          clean()
          break

        else:
          Cn = str(input("Ingrese una opcion valida(S/N): "))
  else:
    print("No se pudo comunicar con la API, el menu se cerrara")
    time.sleep(2)
    clean()


def impresion(lista, dir):
  i = 0
  # Itera sobre cada carácter en el elemento e imprime los digitos
  for elementos in lista:
    i = i + 1
    print(str(i) + ".- ", end="")
    for c in elementos:
      if "0" <= c <= "9":
        print(c, end="")
    print("")
  while True:
    #Estilo de ciclo para verificar que el usuario ingrese una opcion valida
    Cn = str(input("Desea realizar la impresión de los datos (S/N): "))
    if Cn == "S" or Cn == "s":
      a = exc_int()
      #print(dir)

      diccionario = dict()
      #Si existe el id ingresado, lo abre para la extraccion de datos
      if str(a) + ".txt" in lista:
        fo = open(dir + "/" + str(a) + ".txt", 'r')
        texto = fo.read()
        fo.close()
        with open(dir + "/" + texto, "r") as file:
          print("----------------------------------")
          for el in file:
            print(el, end="")
            partes = el.split(":")
            diccionario[partes[0]] = partes[1]
          funciones2.ImpExl(diccionario)
      else:
        print("No se pudo encontrar el archivo, saliendo...")
        time.sleep(4)
      clean()
      break
    elif Cn == "N" or Cn == "n":
      #regresa el menu, y no realiza nada
      print("Regresando al menú...")
      time.sleep(2)
      clean()
      break
    else:
      #Si no ingresa una opcion valida, vuelve a pedir al usuario
      print("Ingrese una opción válida..\n")
      time.sleep(1.5)


def historial():
  #Se abre la carpeta, y lee el nombre de todos los archivos que existen
  dir = os.path.abspath(".")
  dir2 = os.path.join(dir, "pokemons")
  try:
    patron = r"(\d+)_\["
    archivos = os.listdir(dir2)
    lista = list()
    arch = list()
    for doc in archivos:
      #print(doc)
      coincidencias = re.findall(patron, doc)
      lista.append(coincidencias)
    for el in lista:
      for x in el:
        arch.append(str(x) + ".txt")

  except FileNotFoundError:
    #Si no se encuentra la carpeta, se crea

    print("Carpeta no existente, creando..")
    time.sleep(2)
    os.mkdir(dir2)
    print("Aplicado, reinice el programa")
    exit()

  return arch, dir2


#excepciones
def exc_int():
  try:
    #Intenta convertir el input en int
    var = int(input("Ingrese una opción: "))
  except (ValueError, Exception) as el:
    #genera la excepcion si ingresa otro tipo de dato
    print("Debes capturar números enteros: ")
    var = exc_int()
  except:
    print("Error desconocido.")
    var = exc_int()
  return var
