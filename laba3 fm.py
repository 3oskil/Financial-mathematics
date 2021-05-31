import matplotlib.pyplot as plt
import numpy as np

Z, g, n = 500000, 0.11, 5
k, Zk, Dk, Ik = 1, [(Z if i == 0 else 0) for i in range(n + 1)], [0 for _ in range(n)], [0 for _ in range(n)]
A = np.around((Z * g) / (1 - (1 + g) ** -n), decimals=2)
while k <= 5:
    Ik[k - 1] = np.around(Zk[k - 1] * g, decimals=2)
    Dk[k - 1] = np.around(A - Ik[k - 1], decimals=2)
    Zk[k] = np.around(Zk[k - 1] - Dk[k - 1], decimals=2)
    print(f'Год: {k}\n',
          f'Срочная уплата: {A}\n',
          f'Процентный платеж: {Ik[k - 1]}\n',
          f'Выплата по основному долгу: {Dk[k - 1]}\n',
          f'Остаток основного долга: {Zk[k]}\n')
    k += 1
print(
    f'Срочная уплата: {A * n}\n',
    f'Процентный платеж: {sum(Ik)}\n',
    f'Выплата по основному долгу: {sum(Dk)}\n',
    f'Остаток основного долга: {Zk[len(Zk) - 1]}\n'
)

x = np.arange(1, n + 1)
y1 = Dk
y2 = Ik

fig, ax = plt.subplots()

ax.bar(x, y1, color='lightgreen', width=-0.9, edgecolor="black", tick_label=[i for i in range(1, n + 1)], align='edge')
ax.bar(x, y2, bottom=y1, color='paleturquoise', width=-0.9, edgecolor="black", align='edge')

for i, dk in enumerate(Dk):
    ax.text(i + 0.35, dk - 1000, Dk[i], va='top')

for i, ik in enumerate(Ik):
    ax.text(i + 0.35, ik + Dk[i] - 1000, Ik[i], va='top')

ax.set_facecolor('seashell')
ax.set_title('Структура погашения кредита равными срочными уплатами')
fig.set_figwidth(12)
fig.set_figheight(6)
fig.set_facecolor('floralwhite')

plt.show()


Z, g, n = 500000, 0.11, 5
k, Zk, Dk, Ik = 1, [(Z if i == 0 else 0) for i in range(n + 1)], [Z / n for i in range(n)], [0 for _ in range(n)]
Ak = [0 for _ in range(n)]
while k <= n:
    Ik[k - 1] = np.around(Zk[k - 1] * g, decimals=2)
    Ak[k - 1] = np.around(Dk[k - 1] + Ik[k - 1], decimals=2)
    Zk[k] = np.around(Zk[k - 1] - Dk[k - 1], decimals=2)
    print(f'Год: {k}\n',
          f'Выплата по основному долгу: {Dk[0]}\n',
          f'Процентный платеж: {Ik[k - 1]}\n',
          f'Срочная уплата: {Ak[k - 1]}\n',
          f'Остаток основного долга: {Zk[k]}\n')
    k += 1
print(
    f'Выплата по основному долгу: {sum(Dk)}\n',
    f'Процентный платеж: {sum(Ik)}\n',
    f'Срочная уплата: {sum(Ak)}\n',
    f'Остаток основного долга: {Zk[len(Zk) - 1]}\n'
)

x = np.arange(1, n + 1)
y1 = Dk
y2 = Ik

fig, ax = plt.subplots()

ax.bar(x, y1, color='lightgreen', width=-0.9, edgecolor="black", tick_label=[i for i in range(1, n + 1)], align='edge')
ax.bar(x, y2, bottom=y1, color='paleturquoise', width=-0.9, edgecolor="black", align='edge')

for i, dk in enumerate(Dk):
    ax.text(i + 0.35, dk - 1000, Dk[i], va='top')

for i, ik in enumerate(Ik):
    ax.text(i + 0.35, ik + Dk[i] - 1000, Ik[i], va='top')

ax.set_facecolor('seashell')
ax.set_title('Структура погашения кредита равными выплатами по погашению основного долга')
fig.set_figwidth(12)
fig.set_figheight(6)
fig.set_facecolor('floralwhite')

plt.show()


Z, g, n = 500000, 0.11, 5
k, Zk, Dk, Ik = 1, [(Z if i == 0 else 0) for i in range(n + 1)], [(0 if i < n - 1 else Z) for i in range(n)], [0 for _ in range(n)]
Ak = [0 for _ in range(n)]
print(Dk)
while k <= n:
    Ik[k - 1] = np.around(Zk[k - 1] * g, decimals=2)
    Ak[k - 1] = np.around(Dk[k - 1] + Ik[k - 1], decimals=2)
    Zk[k] = np.around(Zk[k - 1] - Dk[k - 1], decimals=2)
    print(f'Год: {k}\n',
          f'Выплата по основному долгу: {Dk[0]}\n',
          f'Процентный платеж: {Ik[k - 1]}\n',
          f'Срочная уплата: {Ak[k - 1]}\n',
          f'Остаток основного долга: {Zk[k]}\n')
    k += 1
print(
    f'Выплата по основному долгу: {sum(Dk)}\n',
    f'Процентный платеж: {sum(Ik)}\n',
    f'Срочная уплата: {sum(Ak)}\n',
    f'Остаток основного долга: {Zk[len(Zk) - 1]}\n'
)

x = np.arange(1, n + 1)
y1 = Dk
y2 = Ik

fig, ax = plt.subplots()

ax.bar(x, y1, color='lightgreen', width=-0.9, edgecolor="black", tick_label=[i for i in range(1, n + 1)], align='edge')
ax.bar(x, y2, bottom=y1, color='paleturquoise', width=-0.9, edgecolor="black", align='edge')

for i, dk in enumerate(Dk):
    if dk != 0:
        ax.text(i + 0.35, dk - 1000, Dk[i], va='top')
    else:
        continue

for i, ik in enumerate(Ik):
    ax.text(i + 0.35, ik + Dk[i] - 1000, Ik[i], va='top')

ax.set_facecolor('seashell')
ax.set_title('Структура погашения кредита с погашением основного долга одним платежом в конце срока кредитования')
fig.set_figwidth(12)
fig.set_figheight(6)
fig.set_facecolor('floralwhite')

plt.show()



Z, g, n, c = 500000, 0.11, 5, 30000
k, Zk, Dk, Ik = 1, [(Z if i == 0 else 0) for i in range(n + 1)], [((Z / n) - (c * (n - 1) / 2) if i == 0 else 0) for i in range(n)], [0 for _ in range(n)]
Ak = [0 for _ in range(n)]
while k <= n:
    if k > 1:
        Dk[k - 1] = Dk[k - 2] + c
    Ik[k - 1] = np.around(Zk[k - 1] * g, decimals=2)
    Ak[k - 1] = np.around(Dk[k - 1] + Ik[k - 1], decimals=2)
    Zk[k] = np.around(Zk[k - 1] - Dk[k - 1], decimals=2)
    print(f'Год: {k}\n',
          f'Выплата по основному долгу: {Dk[k - 1]}\n',
          f'Процентный платеж: {Ik[k - 1]}\n',
          f'Срочная уплата: {Ak[k - 1]}\n',
          f'Остаток основного долга: {Zk[k]}\n')
    k += 1
print(
    f'Выплата по основному долгу: {sum(Dk)}\n',
    f'Процентный платеж: {sum(Ik)}\n',
    f'Срочная уплата: {sum(Ak)}\n',
    f'Остаток основного долга: {Zk[len(Zk) - 1]}\n'
)

x = np.arange(1, n + 1)
y1 = Dk
y2 = Ik

fig, ax = plt.subplots()

ax.bar(x, y1, color='lightgreen', width=-0.9, edgecolor="black", tick_label=[i for i in range(1, n + 1)], align='edge')
ax.bar(x, y2, bottom=y1, color='paleturquoise', width=-0.9, edgecolor="black", align='edge')

for i, dk in enumerate(Dk):
    ax.text(i + 0.35, dk - 1000, Dk[i], va='top')

for i, ik in enumerate(Ik):
    ax.text(i + 0.35, ik + Dk[i] - 1000, Ik[i], va='top')

ax.set_facecolor('seashell')
ax.set_title(' Структура погашения кредита с платежами по основному долгу, возрастающими в арифметической прогрессии')
fig.set_figwidth(12)
fig.set_figheight(6)
fig.set_facecolor('floralwhite')

plt.show()


Z, g, n = 500000, 0.11, 5
k = 0
Ak = [(100000 if i < n - 1 else 0) for i in range(n)]
Ik, Dk, Zk = [0 for _ in range(n)], [0 for _ in range(n)], [(Z if i == 0 else 0) for i in range(n)]
while k < n:
    Ik[k] = np.around((Zk[k - 1] if k > 0 else Zk[k]) * g, decimals=2)
    if k == n - 1:
        Ak[n - 1] = Ik[k] + Zk[k - 1]
    Dk[k] = Ak[k] - Ik[k]
    Zk[k] = (Zk[k] if k == 0 else Zk[k - 1]) - Dk[k]
    print(f'Год: {k + 1}\n',
          f'Срочная уплата: {Ak[k]}\n',
          f'Процентный платеж: {Ik[k]}\n',
          f'Выплата по основному долгу: {Dk[k]}\n',
          f'Остаток основного долга: {Zk[k]}\n')
    k += 1
print(
    f'Срочная уплата: {sum(Ak)}\n',
    f'Процентный платеж: {sum(Ik)}\n',
    f'Выплата по основному долгу: {sum(Dk)}\n',
    f'Остаток основного долга: {Zk[len(Zk) - 1]}\n'
)

x = np.arange(1, n + 1)
y1 = Dk
y2 = Ik

fig, ax = plt.subplots()

ax.bar(x, y1, color='lightgreen', width=-0.9, edgecolor="black", tick_label=[i for i in range(1, n + 1)], align='edge')
ax.bar(x, y2, bottom=y1, color='paleturquoise', width=-0.9, edgecolor="black", align='edge')

for i, dk in enumerate(Dk):
    ax.text(i + 0.35, dk - 1000, Dk[i], va='top')

for i, ik in enumerate(Ik):
    ax.text(i + 0.35, ik + Dk[i] - 1000, Ik[i], va='top')

ax.set_facecolor('seashell')
ax.set_title('Структура погашения кредита последовательностью платежей, все элементы которой, кроме последнего, заданы')
fig.set_figwidth(12)
fig.set_figheight(6)
fig.set_facecolor('floralwhite')

plt.show()


x = np.arange(1, 5 + 1)
y1 = [74157.8 for _ in range(5)]
y2 = [0, 0, 0, 0, 500000.16]
y3 = [55000 for _ in range(5)]

fig, ax = plt.subplots()

ax.bar(x, y1, color='paleturquoise', width=-0.9, edgecolor="black", tick_label=[i for i in range(1, 5 + 1)], align='edge')
ax.bar(x, y2, bottom=y1, color='lightgreen', width=-0.9, edgecolor="black", align='edge')
ax.bar(x, y3, color='r', width=-0.9, edgecolor="black", align='edge')

for i, dk in enumerate(y1):
    ax.text(i + 0.35, dk - 1000, y1[i], va='top')

ax.text(4.35, 500000.16 - 10000, y2[4], va='top')

for i, ak in enumerate(y3):
    ax.text(i + 0.35, ak - 1000, y3[i], va='top')

ax.set_facecolor('seashell')
ax.set_title('Структура погашения кредита с помощью погасительного фонда')
fig.set_figwidth(12)
fig.set_figheight(6)
fig.set_facecolor('floralwhite')

plt.show()


Z, g, n, p, t = 500000, 0.11, 0.5, 12, 6
k = 1
Ak = np.around((Z * (1 + g * n)) / (p * n), decimals=2)
Ik, Dk, Zk = [0 for _ in range(t)], [0 for _ in range(t)], [0 for _ in range(t)]
while k <= t:
    Ik[k - 1] = np.around(((p * n - k + 1) / (p * n * (p * n + 1) / 2)) * Z * n * g, decimals=2)
    Dk[k - 1] = np.around(Ak - Ik[k - 1], decimals=2)
    Zk[k - 1] = np.around((Z - Dk[k - 1] if k == 1 else Zk[k - 2] - Dk[k - 1]), decimals=2)
    print(f'Год: {k}\n',
          f'Срочная уплата: {Ak}\n',
          f'Процентный платеж: {Ik[k - 1]}\n',
          f'Выплата по основному долгу: {Dk[k - 1]}\n',
          f'Остаток основного долга: {Zk[k - 1]}\n')
    k += 1
print(
    f'Срочная уплата: {Ak * t}\n',
    f'Процентный платеж: {sum(Ik)}\n',
    f'Выплата по основному долгу: {sum(Dk)}\n',
    f'Остаток основного долга: {Zk[len(Zk) - 1]}\n'
)

x = np.arange(1, t + 1)
y1 = Dk
y2 = Ik

fig, ax = plt.subplots()

ax.bar(x, y1, color='lightgreen', width=-0.9, edgecolor="black", tick_label=[i for i in range(1, t + 1)], align='edge')
ax.bar(x, y2, bottom=y1, color='paleturquoise', width=-0.9, edgecolor="black", align='edge')

for i, dk in enumerate(Dk):
    ax.text(i + 0.35, dk - 500, Dk[i], va='top')

for i, ik in enumerate(Ik):
    ax.text(i + 0.35, ik + Dk[i], Ik[i])

ax.set_facecolor('seashell')
ax.set_title('Структура погашения потребительского кредита ежемесячными платежами')
fig.set_figwidth(12)
fig.set_figheight(6)
fig.set_facecolor('floralwhite')

plt.show()
