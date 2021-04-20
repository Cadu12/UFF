hi, mi, hf, mf = [int(i) for i in input().split()]

if hi == hf and mi == mf:
    print(f"O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    total_hora = hf - hi
    total_min = mf - mi
    if total_hora < 0:
        total_hora = 24 + (hf - hi)
    if total_min < 0:
        total_min = 60 + (mf - mi)
        total_hora -= 1
        if total_hora < 0:
            total_hora = 24 + (hf - hi) - 1
    
    print(f"O JOGO DUROU {total_hora} HORA(S) E {total_min} MINUTO(S)")