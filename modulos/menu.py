import os

def CrearMenu():
    lstOpciones =[1,2,3,4]
    titulo = """
      +++++++++++++++++++++
      + LIGA BETPLAY MENU +
      +++++++++++++++++++++
    """
   
    os.system ('cls')
    print(titulo)
    try:
        opciones = "1.Agregar equipo\n2. Registrar fecha\n3. Reportes\n4. Salir"
        print(opciones)
        op= int(input(':) '))
        if not (op in lstOpciones):
          CrearMenu()
    except ValueError:
        print('El dato es invalido')
        os.system('pause')
        CrearMenu()
    else:
        isValid = False
        return op
    
    
    
    