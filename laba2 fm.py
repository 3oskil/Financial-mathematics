import numpy as np

N, i, n = 5, 0.12, 10
S, Si = N * 100000, 0
t = 0
C = np.around((S * i) / ((1 + i) ** n - 1), decimals=1)
while Si < S:
    print(f"Интервал: [{t}, {t + 1}]")
    print("Остаток на начало года:", Si)
    print("Начислено процентво за год:", s := np.around(Si * i, decimals=2))
    print("Остаток на конец года:", Si := Si + s)
    print("Взнос С в конце года:", C)
    Si += C
    print("Сумма после взноса:", Si, '\n')
    t += 1

N, i, n = 5, 0.12, 10
A, A1 = N * 100000, 0
t = 0
C = -np.around((A * i) / (1 - (1 + i) ** -n), decimals=1)
while A > A1:
    print(f"Интервал: [{t}, {t + 1}]")
    print("Остаток на начало года:", A)
    print("Начислено процентво за год:", s := np.around(A * i, decimals=2))
    print("Остаток на конец года:", A := A + s)
    print("Взнос С в конце года:", C)
    A += C
    print("Сумма после взноса:", A, '\n')
    t += 1

N, i, n = 5, 0.12, 12
A1, A2 = 0, 0
n1, n2 = 8, 10
C1, C2 = N * 70, N * 100
t, T = 0, n
C = np.around((((C1 * ((1 - (1 + i) ** -n1) / i)) + (C2 * ((1 - (1 + i) ** -n2) / i))) * i) / (1 - (1 + i) ** -n),
              decimals=2)
while T >= t + 1:
    print(f"Интервал: [{t}, {t + 1}]")
    print("Исходные ренты:")
    print("\t\t\tОстаток на начало года:", A1)
    print("\t\t\tНачислено процентво за год:", s1 := np.around(A1 * i, decimals=2))
    if t < min(n1, n2):
        C12 = C1 + C2
    elif min(n1, n2) <= t + 1 <= max(n1, n2):
        C12 = C2
    else:
        C12 = 0
    print("\t\t\tСуммарный платеж по исходным рентам:", (C12 if t + 1 < n1 else "-"))
    A1 += C12 + s1
    print("\t\t\tОстаток на конец периода:", A1)

    print("\nОбобщенная рента:")
    print("\t\t\t\tОстаток на начало периода:", A2)
    print("\t\t\t\tНачислено процентво за год:", s2 := np.around(A2 * i, decimals=2))
    print("\t\t\t\tПлатеж по обобщенной ренте:", C)
    A2 += C + s2
    print("\t\t\t\tОстаток на конец периода:", A2)
    t += 1


t = 0
S = 0
i, n1, n2 = 0.12, 10, 8
s, a = np.around(((1 + i) ** n1 - 1) / i, decimals=5), np.around((1 - (1 / (1 + i)) ** n2) / i, decimals=5)
C1, C2 = np.around(10000 * a / s, decimals=2), -10000
while t < n1 + n2:
    print(f"Интервал: [{t}, {t + 1}]")
    print("Остаток на начало года:", S)
    print("Начислено процентво за год:", s := np.around(S * i, decimals=2))
    print("Остаток на конец года:", S := S + s)
    print("Взнос (снятие) в конце года:", C := (C1 if t + 1 <= 10 else C2))
    print("Сумма после выплаты:", S := S + C, '\n')
    t += 1
