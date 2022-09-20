
def fechaDelSistema(fecha):

    if fecha == "sabado" :
        return "No es dia lavoral"
    if fecha == "domingo" :
        return "No es dia lavoral"
    else:
        return "Es dia lavoral"

def horario(hora):

    if hora >=7:
        return "Es hora de ir a casa"

    elif hora ==6:
        return "Queda 1 hora de trabajo"
    elif hora ==5:
        return  "Quedan 2 horas de trabajo"
    elif hora ==4:
        return "Quedan 3 horas de trabajo"
    elif hora ==3:
        return "Quedan 4 horas de trabajo"
    elif hora ==2:
        return "Quedan 5 horas de trabajo"
    elif hora ==1:
        return "Acabas de empezar la jornada"
    else:
        return "Acabas de empezar la jornada"

print(fechaDelSistema(fecha = "lunes"))
print(fechaDelSistema(fecha = "domingo"))
print(fechaDelSistema(fecha = "sabado"))
print(fechaDelSistema(fecha = "martes"))
print(fechaDelSistema(fecha = "viernes"))
print(horario(hora=7))
print(horario(hora=6))
print(horario(hora=5))
print(horario(hora=4))
print(horario(hora=2))
print(horario(hora=1))
print(horario(hora=8))



