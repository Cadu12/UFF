while True:
    try:
        a, b = [int(i) for i in input().split()]
        h = int((a * 12) / 360)
        m = int((b * 60) / 360)
        print(f"{h:02}:{m:02}")
    except:
        break