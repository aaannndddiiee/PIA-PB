#En esta excepcion se comprueba que el modulo funciones este, si no cierra el programa
try:
  import funciones
except ModuleNotFoundError:
  print("Debe tener el programa 'Funciones.py' para que pueda funcionar")
  input("Enter para continuar")
  exit()
try:
  import funciones2
except ModuleNotFoundError:
  print("Debe tener el programa 'Funciones2.py' para que pueda funcionar")
  input("Enter para continuar")
  exit()

#La funcion "funciones.clean(), se repite mucho, ya que esta limpia la pantalla"
#inicia la funcion principal
if __name__ == "__main__":
  tiempo_actual = funciones.time.time()
  # Formatear el timestamp como una cadena sin dos puntos
  tiempo = funciones.time.strftime("_[%Y-%m-%d_%H-%M-%S]", funciones.time.localtime(tiempo_actual))
  menu = '''Menu:
            1) Consulta de Datos.
            2) Ver historial.
            3) Eliminar información.
            4) Gráficas.
            5) Cálculos.
            6) Salir.
            '''
  #Menu 1
  while True:
    funciones.clean()
    print(menu)
    opc = funciones.exc_int()
    if opc == 1:
      #Hace la consulta a la API, imprime los datos, y decide si guarda el txt ono
      funciones.clean()
      funciones.consulta()
    elif opc == 2:
      #Imprime el historial, selecciona un ID, imprime sus datos, y se decide si se guarda en un excel o no
      #El excel se creara en caso de que no exista, si no, solo se agregara el dato al ya existente
      funciones.clean()
      lista, dir = funciones.historial()
      funciones.impresion(lista, dir)
    elif opc == 3:
      #Elimina alguna Id seleccionada de los archivos, en caso de que no exista, regresa el menu
      funciones.clean()
      lista, dir = funciones.historial()
      a = funciones.exc_int()
      try:
        fo = open(dir+"/"+str(a)+".txt", 'r')
        texto=fo.read()
        fo.close() 
        funciones.os.remove(dir + "/ "+ str(a) + ".txt")
        funciones.os.remove(dir + "/" + texto)
        print("Archivo eliminado con éxito.")
        funciones.time.sleep(3)
        funciones.clean()
      except OSError:
        print("No se encontro el archivo.")
        funciones.time.sleep(3)
        funciones.clean()
    elif opc == 4:
      #Menu 2
      menu2 = '''
                Graficas:
                1.-Graficar Peso.
                2.-Graficar conteo de tipos.
                3.-Graficar Altura.
                4.-Salir al menú principal.
                '''
      while True:
        funciones.clean()
        print(menu2)
        opc2 = funciones.exc_int()
        if opc2 == 1:
          #Imprime una grafica de los pesos, en caso de que no encuentra datos
          #, se regresa al menu
          funciones.clean()
          lista, dir = funciones.historial()
          nombre, flotantes = funciones2.ext_peso(lista, dir)
          dir = funciones.os.path.abspath(".")
          if not nombre and not flotantes:
            print("No hay datos para mostrar, saliendo... ")
            funciones.time.sleep(4)
            funciones.clean()
          else:
            input("Enter para continuar..")
            x = funciones.np.array(nombre)
            y = funciones.np.array(flotantes)
            fig = funciones.plt.figure(figsize=(20, 10))
            funciones.plt.barh(x,
                               y,
                               color="lime",
                               hatch="/",
                               edgecolor="black")
            funciones.plt.xlabel("Peso[Kg])")
            funciones.plt.ylabel("Nombres")
            funciones.plt.title("Gráfico de pesos")
            try:
              funciones.plt.savefig(dir+"/Graficas/"+'Grafica_peso'+tiempo+'.png')
            except FileNotFoundError:
                print("Carpeta no existente, creando..")
                funciones.time.sleep(2)
                funciones.os.mkdir(dir+"/Graficas")
                funciones.plt.savefig(dir+"/Graficas/"+'Grafica_peso'+tiempo+'.png')
            finally:
                print("Imagen Guardada correctamente.")
            funciones.plt.show()
  
            funciones.clean()
        elif opc2 == 2:
          #Imprime una grafica de pastel, que muestra los tipos de pokemon que se encontraron,
          #en caso de no encontrar, regresa al menu

          lista, dir = funciones.historial()
          tipos = list()
          conttipos = list()
          frec = funciones2.ext_tipo(lista, dir)
          dir = funciones.os.path.abspath(".")
          if not frec:
            print("No hay datos para mostrar, saliendo... ")
            funciones.time.sleep(4)
            funciones.clean()
          else:
            for tipo in frec.most_common():
              conttipos.append(tipo[1])
              tipos.append(tipo[0])
            funciones.os.system("pause")
            fig = funciones.plt.figure(figsize=(20, 10))
            funciones.plt.pie(conttipos,
                              labels=tipos,
                              shadow=True,
                              autopct="%1.1f%%")
            funciones.plt.title("Conteo de Tipos")
            try:
              funciones.plt.savefig(dir+"/graficas/"+'Grafica_Tipos'+tiempo+'.png')
            except FileNotFoundError:
                print("Carpeta no existente, creando..")
                funciones.time.sleep(2)
                funciones.os.mkdir(dir+"/Graficas")
                funciones.plt.savefig(dir+"/Graficas/"+'Grafica_Tipos'+tiempo+'.png')
            funciones.plt.show()
            funciones.clean()
        elif opc2 == 3:
          ##Imprime una grafica de barras, en caso de encontrar datos, regresa al menu
          funciones.clean()
          lista, dir = funciones.historial()
          nombre, flotantes = funciones2.ext_altura(lista, dir)
          dir = funciones.os.path.abspath(".")
          if not nombre and not flotantes:
            print("No hay datos para mostrar, saliendo.. ")
            funciones.time.sleep(4)
            funciones.clean()

          else:
            x = funciones.np.array(nombre)
            y = funciones.np.array(flotantes)
            fig = funciones.plt.figure(figsize=(20, 10))
            funciones.plt.bar(x,
                              y,
                              color="slategray",
                              hatch="/",
                              edgecolor="black")
            funciones.plt.xlabel("Nombre")
            funciones.plt.ylabel("Altura(m)")
            funciones.plt.title("Gráfico de Alturas")
            try:
              funciones.plt.savefig(dir+"/Graficas/"+'Grafica_altura'+tiempo+'.png')
            except FileNotFoundError:
                print("Carpeta no existente, creando..")
                funciones.time.sleep(2)
                funciones.os.mkdir(dir+"/Graficas")
                funciones.plt.savefig(dir+"/Graficas/"+'Grafica_altura'+tiempo+'.png')
            funciones.plt.show()
            funciones.clean()

        elif opc2 == 4:
          break
        else:
          print("Ingrese una opción valida..\n ")
          funciones.time.sleep(1.5)

    elif opc == 5:
      menu3 = '''
                Cálculos:
                1) Cálculo de la media, mediana y moda del peso.
                2) Conversion de un ID a bin,oct y hex.
                3) Top 3 de Tipos de pokemon que más aparecen.
                4) Salir.
                    '''
      while True:
        funciones.clean()
        print(menu3)
        opc3 = funciones.exc_int()
        if opc3 == 1:
          #imprime la mediana, la moda y la media, en caso de no encontrar datos regresa al menú
          funciones.clean()
          lista, dir = funciones.historial()
          nombre, flotantes = funciones2.ext_peso(lista, dir)
          if not nombre and not flotantes:
            print("No hay datos para mostrar, saliendo..")
            funciones.time.sleep(3)
            funciones.clean()
          else:
            print("Cálculo de mediana,media y moda")
            print("-------------------------------\n")
            print("La mediana de los pesos es: ",
                  funciones.statistics.median(flotantes), "kg\n")
            print("La media de los pesos es: ",
                  funciones.statistics.mean(flotantes), "kg\n")
            print("La moda de los pesos es: ",
                  funciones.statistics.mode(flotantes), "kg\n")
            funciones.os.system("pause")
        elif opc3 == 2:
          #Realiza una conversion del id seleccionado, si no existe, regresa al menu
          funciones.clean()
          print("Conversion de id ")
          print("-----------------\n")
          lista, dir = funciones.historial()
          id = funciones2.ext_id(lista, dir)
          i = 0
          id2 = list()
          for ids in id:
            i += 1
            print(i, ".-", ids)
            id2.append(int(ids))
          Ident = funciones.exc_int()
          funciones.clean()
          if Ident in id2:
            print("---------")
            print("Id original: ", Ident)
            print("Id a binario: ", bin(Ident))
            print("Id a Octal: ", oct(Ident))
            print("Id a Hexadecimal", hex(Ident))
          else:
            print("No se encontro esta ID, saliendo..")
          funciones.os.system("pause")
        elif opc3 == 3:
          funciones.clean()
          print("Top 3 de Tipos de Pokemón que más aparecen: ")
          print("-------------------------------------------\n")
          lista, dir = funciones.historial()
          frec = funciones2.ext_tipo(lista, dir)
          if not frec:
            print("No hay datos para mostrar, saliendo...")
            funciones.time.sleep(4)
            funciones.clean()
          else:
            print('{0}\t\t{1}'.format("Tipo", "Apariciones"))
            for tipo in frec.most_common(3):
              print('{0}\t\t{1}'.format(tipo[0], tipo[1]))
            funciones.os.system("pause")
        elif opc3 == 4:
          break
        else:
          print("Ingrese una opción valida...\n ")
          funciones.time.sleep(1.5)
    elif opc == 6:
      #Cierra el programa
      print("Hasta luego...")
      funciones.time.sleep(3)
      exit()
    else:
      #condicional que aparece cuando se escoje un numero diferente
      print("Ingrese una opción valida...\n ")
      funciones.time.sleep(1.5)
