from datetime import datetime

def signoZodiacal():
    dia = int(input("Ingresa tu dia de nacimiento (dd): "))
    mes = int(input("Ingresa tu mes de nacimiento(mm): "))
    anio = int(input("Ingresa tu año de nacimiento(aaaa): "))
    
    fechaNac = datetime(anio,mes,dia)
    
    fechas_zodiacales = {
        "Aries": (datetime(anio, 3, 21), datetime(anio, 4, 19)),
        "Tauro": (datetime(anio, 4, 20), datetime(anio, 5, 20)),
        "Géminis": (datetime(anio, 5, 21), datetime(anio, 6, 20)),
        "Cáncer": (datetime(anio, 6, 21), datetime(anio, 7, 22)),
        "Leo": (datetime(anio, 7, 23), datetime(anio, 8, 22)),
        "Virgo": (datetime(anio, 8, 23), datetime(anio, 9, 22)),
        "Libra": (datetime(anio, 9, 23), datetime(anio, 10, 22)),
        "Escorpio": (datetime(anio, 10, 23), datetime(anio, 11, 21)),
        "Sagitario": (datetime(anio, 11, 22), datetime(anio, 12, 21)),
        "Capricornio": (datetime(anio, 12, 22), datetime(anio, 1, 19)),
        "Acuario": (datetime(anio, 1, 20), datetime(anio, 2, 18)),
        "Piscis": (datetime(anio, 2, 19), datetime(anio, 3, 20)),
    }


    for signo, (fechaInicio, fechaFin) in fechas_zodiacales.items():
        if fechaInicio <= fechaNac <= fechaFin:
            signoZodical = signo
            break    
    if signoZodical:
        print(f"Tu signo zodiacal es {signoZodical}.")
    else:
        print("No tienes signo zodiacal xd")
 