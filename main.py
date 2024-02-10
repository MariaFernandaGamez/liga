import modulos.menu as mp
import modulos.reportes as mr
import modulos.equipos as me
if __name__== '__main__':
    equiposLiga =[]
    isAppRunning =True
    while isAppRunning:
        op=mp.CrearMenu()
        if (op ==1):
            isAddTeam = True
            while isAddTeam:
                me.os.system('cls')
                me.AddTeam(equiposLiga)
                isAddTeam = bool(input('¿Desea agragar otro equipo?, (S) Para SI, (N) Para no'))

        elif (op ==2):
            pass
        elif (op ==3):
            isReport = True
            while isReport:
                opr =mr.CrearMenu()  
                if (opr == 'A'):
                    pass
                elif (opr == 'B'):
                    pass
                elif (opr == 'C'):
                    pass
                elif (opr == 'B'):
                    pass
                elif (opr == 'D'):
                    pass
                elif (opr == 'E'):
                    pass
                elif (opr == 'F'):
                    isReport =False
        elif (op ==4):
            isAppRunning=False
      