import os
def CrearMenu():
    lstOpciones=['A','B','C','D','E','F']
    opciones= ['A. Equipo con mayor numero de goles','B. Equipo con mas puntos','C. Equipo que gano mas partidos','D. Total de goles anotados por todos los equipos','E. Promedio de goles anotados en el torneo','F. Salir al menu principal']
    os.system('cls')
    titulo = """
      ++++++++++++++++++++++++++++++
      + LIGA BETPLAY MENU REPORTES +
      ++++++++++++++++++++++++++++++
    """
    print(titulo)
    for item in opciones:
      print(item)
    try:
       op = input(':)_')
    except:
       print ('Error en la opcion')
       os.system('pause')
       CrearMenu()
    else:
       return op
