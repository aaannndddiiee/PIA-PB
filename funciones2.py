try:
  import funciones
except ModuleNotFoundError:
  print("Debe tener el programa 'Funciones.py' para que pueda funcionar")
  input("Enter para continuar")
  exit()


def ext_peso(lista, dir):
  tam = len(lista)
  flotantes = list()
  nombre = list()
  patron = r"[-+]?\d*\.\d+|\d"
  #patron que realiza la busqueda de numeros flotantes
  patron2 = r"name:(\w+(?:-\w+)?)\n"
  #patron que realiza la busqueda de nombres
  for i in range(0, tam + 1):
    if str(i) + ".txt" in lista:
      fo = open(dir + "/" + str(i) + ".txt", 'r')
      texto = fo.read()
      fo.close()
      with open(dir + "/" + texto, "r") as file:
        #Si existe el archivo lo abre, y lo lee, para despues extraer
        #los datos seleccionados por el patron
        for el in file:
          if "weight:" in el:
            coin = funciones.re.findall(patron, el)
            for i in coin:
              flotantes.append(float(i))
          if "name:" in el:
            coin2 = funciones.re.findall(patron2, el)
            for i in coin2:
              nombre.append(str(i))

  return nombre, flotantes


def ext_altura(lista, dir):
  tam = len(lista)
  flotantes = list()
  nombre = list()
  patron = r"[-+]?\d*\.\d+|\d"
  #patron que realiza la busqueda de numeros flotantes
  patron2 = r"name:(\w+(?:-\w+)?)\n"
  #patron que realiza la busqueda de nombres
  for i in range(0, tam + 1):
    if str(i) + ".txt" in lista:
      fo = open(dir + "/" + str(i) + ".txt", 'r')
      texto = fo.read()
      fo.close()
      with open(dir + "/" + texto, "r") as file:
        #Si existe el archivo lo abre, y lo lee, para despues extraer
        #los datos seleccionados por el patron
        for el in file:
          if "height:" in el:
            coin = funciones.re.findall(patron, el)
            for i in coin:
              flotantes.append(float(i))
          if "name:" in el:
            coin2 = funciones.re.findall(patron2, el)
            for i in coin2:
              nombre.append(str(i))
  return nombre, flotantes


def ext_id(lista, dir):
  tam = len(lista)
  id = list()
  patron = r"id:\s*(\w+)"
  #Patron que busca el id en el archivo
  for i in range(0, tam + 1):
    if str(i) + ".txt" in lista:
      fo = open(dir + "/" + str(i) + ".txt", 'r')
      texto = fo.read()
      fo.close()
      with open(dir + "/" + texto, "r") as file:
        #Si existe el archivo lo abre, y lo lee, para despues extraer
        #los datos seleccionados por el patron
        for el in file:
          if "id:" in el:
            coin = funciones.re.findall(patron, el)
            for i in coin:
              id.append(str(i))
  return id


def ext_tipo(lista, dir):
  tam = len(lista)
  tipo = list()
  patron = r"type:\s*(\w+)"
  #patron que busca el tipo de pokemon
  for i in range(0, tam + 1):
    if str(i) + ".txt" in lista:
      fo = open(dir + "/" + str(i) + ".txt", 'r')
      texto = fo.read()
      fo.close()
      with open(dir + "/" + texto, "r") as file:
        for el in file:
          if "type:" in el:
            coin = funciones.re.findall(patron, el)
            for i in coin:
              tipo.append(str(i))
  #Se eliminan los pokemones que no tienen tipo, y se cuentan los que si hay
  frec = funciones.Counter(tipo)
  return frec


#a,b=historial()
#print(a,b)


def ImpExl(diccionario):
  dir = funciones.os.path.abspath(".")
  while True:
    #Estilo de ciclo para verificar que el usuario ingrese una opcion valida
    Cn2 = str(input("\nDesea agregar estos datos a una hoja de excel(S/N): "))
    if Cn2 == "S" or Cn2 == "s":
      #Si existe, Se abre el archivo Excel para sobreescribilo
      try:
        print("accediendo al archivo..")
        libro = funciones.load_workbook(dir + "/Reporte/" + "historial.xlsx")
      except FileNotFoundError:
        print("Carpeta no existente, creando..")
        funciones.time.sleep(2)
        funciones.os.mkdir(dir + "/Reporte")
      try:
        libro = funciones.load_workbook(dir + "/Reporte/" + "historial.xlsx")
      except FileNotFoundError:
        libro = None
        pass
      if libro == None:
        print("No existe el archivo, se creará uno nuevo..")
        funciones.time.sleep(1)
        libro = funciones.Workbook()
        hoja = libro.active
        numlinea = 1
        tiempo_actual = funciones.time.time()
        for x, y in diccionario.items():
          hoja.cell(1, numlinea, value=x)
          hoja.cell(2, numlinea, value=y)
          numlinea += 1
        hoja.cell(1, 9, value="Fecha y hora de creacion")
        hoja.cell(2, 9, value=funciones.time.ctime(tiempo_actual))
        hoja.column_dimensions['A'].width = 20
        hoja.column_dimensions['B'].width = 20
        hoja.column_dimensions['H'].width = 15
        hoja.column_dimensions['I'].width = 30
        #Se agregan los datos al excel
        libro.save(dir + "/Reporte/" + "historial.xlsx")
        print("Datos guardados correctamente, saliendo...")
        funciones.time.sleep(2)
        libro.close()
        funciones.clean()
        break
      else:
        numlinea = 1
        hoja = libro.active
        len = hoja.max_row
        tiempo_actual = funciones.time.time()
        for values in diccionario.values():
          hoja.cell(len + 1, numlinea, value=values)
          numlinea += 1
        try:
          hoja.cell(len + 1,
                    numlinea + 1,
                    value=funciones.time.ctime(tiempo_actual))
          libro.save(dir + "/Reporte/" + "historial.xlsx")
          libro.close()
          print("Historial modificado correctamente")
          funciones.os.system("pause")
        except PermissionError:
          print("Cierre el archivo para poder modificarlo..")
          funciones.time.sleep(1.5)
          pass
        funciones.clean()
        break
    elif Cn2 == "N" or Cn2 == "n":
      #regresa el menu, y no realiza nada
      print("Regresando al menú...")
      funciones.time.sleep(2)
      funciones.clean()
      break
    else:
      print("Ingrese una opción válida..\n")
      funciones.time.sleep(1.5)
