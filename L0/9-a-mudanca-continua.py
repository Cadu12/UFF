while True:
    try:
        m = float(input())
        a = (86400 / 360) * m
        hora = (int(a / 3600) + 6) % 24
        min = int((a % 3600) / 60)
        sec = int(a % 60)

        if hora >= 6 and hora <= 11:
            print("Bom Dia!!")
        elif hora >= 12 and hora <= 17:
            print("Boa Tarde!!")
        elif hora >= 18 and hora <= 23:
            print("Boa Noite!!")
        else:
            print("De Madrugada!!")
            
        print(f"{0 if hora == 24 else hora:02}:{min:02}:{sec:02}")
    except EOFError:
        break