import matplotlib.pyplot as plt
import numpy as np
import math as m

P, i, n = 50000, 0.11, 11
Pc, Ps = P, P
list_compound_interest, list_simple_interest, compound_interest, simple_interest = [], [], [], []
for _ in range(n):
    s = P * i
    Ps = Ps + s
    c = Pc * i
    Pc = Pc + c
    simple_interest.append(s)
    compound_interest.append(c)
    list_simple_interest.append(Ps)
    list_compound_interest.append(Pc)
list_compound_interest = [round(i, 2) for i in list_compound_interest]
compound_interest = [round(i, 2) for i in compound_interest]
print(list_simple_interest, simple_interest, list_compound_interest, compound_interest, sep="\n")

x = np.arange(1, n + 1)
y1 = list_simple_interest
y2 = simple_interest

fig, ax = plt.subplots()

ax.bar(x, y1, color='lightgreen', width=1, edgecolor="black", tick_label=[i for i in range(1, n + 1)])
ax.bar(x, y2, bottom=y1, color='limegreen', width=1, edgecolor="black")

ax.set_facecolor('seashell')
ax.set_title('Наращение капитала по принципу простых процентов')
fig.set_figwidth(12)
fig.set_figheight(6)
fig.set_facecolor('floralwhite')

plt.show()

x = np.arange(1, n + 1)
y1 = list_compound_interest
y2 = compound_interest

fig, ax = plt.subplots()

ax.bar(x, y1, color='paleturquoise', width=1, edgecolor="black", tick_label=[i for i in range(1, n + 1)])
ax.bar(x, y2, bottom=y1, color='dodgerblue', width=1, edgecolor="black")

ax.set_facecolor('seashell')
ax.set_title('Наращение капитала по принципу сложных процентов')
fig.set_figwidth(12)
fig.set_figheight(6)
fig.set_facecolor('floralwhite')

plt.show()

x1 = np.arange(1, n + 1) - 0.3
x2 = np.arange(1, n + 1) - 0.1
x3 = np.arange(1, n + 1) + 0.1
x4 = np.arange(1, n + 1) + 0.3
y1 = list_simple_interest
y2 = list_compound_interest
y3 = simple_interest
y4 = compound_interest

fig, ax = plt.subplots()

ax.bar(x1, y1, width=0.2, edgecolor="black", color='lightgreen')
ax.bar(x2, y2, width=0.2, edgecolor="black", color='paleturquoise')
ax.bar(x3, y3, width=0.2, edgecolor="black", color='limegreen')
ax.bar(x4, y4, width=0.2, edgecolor="black", color='dodgerblue')

ax.set_facecolor('seashell')
ax.set_title('Сравнение процессов наращения капитала по схеме простых и сложных процентов')
fig.set_figwidth(12)
fig.set_figheight(6)
fig.set_facecolor('floralwhite')

plt.show()

P, j1, j2, m1, m2, delta, i, n = 50000, 0.12, 0.12304, 12, 2, 0.11941, 0.12683, 2
continuous_interest_rate, nominal_interest_rate_12, nominal_interest_rate_2, effective_interest_rate = [], [], [], []
t, ti, T, Ti = 0, 1 / 12, m1 * n, 1
while Ti <= T:
    t += ti
    S1 = P * m.exp(delta * t)
    S2 = P * (1 + j1 / m1) ** (m1 * t)
    continuous_interest_rate.append(S1)
    nominal_interest_rate_12.append(S2)
    if round(t, 1) % (1 / m2) == 0:
        S3 = P * (1 + j2 / m2) ** (m2 * t)
        nominal_interest_rate_2.append(S3)
    if round(t, 1) % 1 == 0:
        S4 = P * (1 + i) ** t
        effective_interest_rate.append(S4)
    Ti += 1
continuous_interest_rate = [round(i, 2) for i in continuous_interest_rate]
nominal_interest_rate_12 = [round(i, 2) for i in nominal_interest_rate_12]
nominal_interest_rate_2 = [round(i, 2) for i in nominal_interest_rate_2]
effective_interest_rate = [round(i, 2) for i in effective_interest_rate]
print(continuous_interest_rate, nominal_interest_rate_12, nominal_interest_rate_2, effective_interest_rate, sep="\n")

x = np.arange(1, len(nominal_interest_rate_12) + 1) - 0.5
y = nominal_interest_rate_12

fig, ax = plt.subplots()

ax.bar(x, y, color='seashell',
       width=1,
       edgecolor='black',
       tick_label=[i for i in range(1, len(nominal_interest_rate_12) + 1)],
       ls='--',
       linewidth=0.8)

for i in range(len(nominal_interest_rate_12)):
    plt.plot((i, i), (1, nominal_interest_rate_12[i] - 150), color='black', linewidth=2)
plt.plot((len(nominal_interest_rate_12), len(nominal_interest_rate_12)),
         (1, nominal_interest_rate_12[len(nominal_interest_rate_12) - 1] - 150), color='black', linewidth=2)

plt.plot([(i, i) for i in range(len(continuous_interest_rate))],
         [(i, i) for i in continuous_interest_rate], color='gray')

ax.set_facecolor('seashell')
ax.set_xlabel('t')
ax.set_ylabel('S(t)')
ax.set_title('Номинальная годовая ставка j1 = 12% с частотой m1 = 12')
ax.set_xticks([i for i in range(1, len(nominal_interest_rate_12) + 1) if i % m1 == 0])
ax.set_xticklabels([i for i in range(1, n + 1)])
fig.set_facecolor('floralwhite')
fig.set_figwidth(12)
fig.set_figheight(6)

plt.show()

x = np.arange(1, len(nominal_interest_rate_2) + 1) - 0.5
y = nominal_interest_rate_2

fig, ax = plt.subplots()

ax.bar(x, y, color='seashell',
       width=1,
       edgecolor='black',
       tick_label=[i for i in range(1, len(nominal_interest_rate_2) + 1)],
       ls='--',
       linewidth=0.8)

for i in range(len(nominal_interest_rate_2)):
    plt.plot((i, i), (1, nominal_interest_rate_2[i] - 150), color='black', linewidth=2)
plt.plot((len(nominal_interest_rate_2), len(nominal_interest_rate_2)),
         (1, nominal_interest_rate_2[len(nominal_interest_rate_2) - 1] - 150), color='black', linewidth=2)

plt.plot([(i, i) for i in range(len(nominal_interest_rate_2))],
         [(i, i) for i in continuous_interest_rate if round(i, -1) in [round(i, -1) for i in nominal_interest_rate_2]],
         color='gray')

ax.set_facecolor('seashell')
ax.set_xlabel('t')
ax.set_ylabel('S(t)')
ax.set_title('Номинальная годовая ставка j2 = 12,304% с частотой m2 = 2')
ax.set_xticks([i for i in range(1, len(nominal_interest_rate_2) + 1) if i % m2 == 0])
ax.set_xticklabels([i for i in range(1, n + 1)])
fig.set_facecolor('floralwhite')
fig.set_figwidth(12)
fig.set_figheight(6)

plt.show()

x = np.arange(1, len(effective_interest_rate) + 1) - 0.5
y = effective_interest_rate

fig, ax = plt.subplots()

ax.bar(x, y, color='seashell',
       width=1,
       edgecolor='black',
       tick_label=[i for i in range(1, len(effective_interest_rate) + 1)],
       ls='--',
       linewidth=0.8)

for i in range(len(effective_interest_rate)):
    plt.plot((i, i), (1, effective_interest_rate[i] - 150), color='black', linewidth=2)
plt.plot((len(effective_interest_rate), len(effective_interest_rate)),
         (1, effective_interest_rate[len(effective_interest_rate) - 1] - 150), color='black', linewidth=2)

plt.plot([(i, i) for i in range(len(effective_interest_rate))],
         [(i, i) for i in continuous_interest_rate if round(i, -1) in [round(i, -1) for i in effective_interest_rate]],
         color='gray')

ax.set_facecolor('seashell')
ax.set_xlabel('t')
ax.set_ylabel('S(t)')
ax.set_title('Эффективная годовая ставка i = 12,683%')
ax.set_xticks([i for i in range(1, len(effective_interest_rate) + 1)])
ax.set_xticklabels([i for i in range(1, n + 1)])
fig.set_facecolor('floralwhite')
fig.set_figwidth(12)
fig.set_figheight(6)

plt.show()

x1 = np.arange(1, len(nominal_interest_rate_12) + 1) - 0.5
x2 = np.arange(1, len(nominal_interest_rate_12) + 1) - 6
y1 = nominal_interest_rate_12
y2 = [((P + 500 if i == int(len(nominal_interest_rate_12) / 2) - 1 else 0) if i != len(
    nominal_interest_rate_12) - 1 else effective_interest_rate[0] + 500) for i in range(len(nominal_interest_rate_12))]

fig, ax = plt.subplots()

ax.bar(x1, y1,
       color='seashell',
       width=1,
       edgecolor='black',
       ls='--',
       lw=0.8)

ax.bar(x2, y2,
       color='seashell',
       alpha=0.5,
       width=12,
       edgecolor='black',
       ls='--',
       lw=2.5)

for i in range(len(nominal_interest_rate_12)):
    plt.plot((i, i), (1, nominal_interest_rate_12[i] - 150), color='black', linewidth=2)

plt.plot((len(nominal_interest_rate_12), len(nominal_interest_rate_12)),
         (1, nominal_interest_rate_12[len(nominal_interest_rate_12) - 1] - 150),
         color='black', linewidth=2)

plt.plot((len(nominal_interest_rate_12) / 2, len(nominal_interest_rate_12) / 2),
         (1, y2[len(nominal_interest_rate_12) - 1] - 300),
         color='black', linewidth=5, alpha=0.5)

plt.plot((0, 0),
         (1, y2[int(len(nominal_interest_rate_12) / 2) - 1] - 400),
         color='black', linewidth=5, alpha=0.5)

plt.plot((len(nominal_interest_rate_12), len(nominal_interest_rate_12)),
         (1, nominal_interest_rate_12[len(nominal_interest_rate_12) - 1] - 150),
         color='black', linewidth=5, alpha=0.5)

ax.set_facecolor('seashell')
ax.set_xlabel('t')
ax.set_ylabel('S(t)')
ax.set_title('''Наращение капитала по годовой эффективной процентной ставке i = 12,683% и
 номинальной годовой ставке j1 = 12%, m1 = 12''')
ax.set_xticks([i for i in range(1, len(nominal_interest_rate_12) + 1) if i % m1 == 0])
ax.set_xticklabels([i for i in range(1, n + 1)])
fig.set_facecolor('floralwhite')
fig.set_figwidth(12)
fig.set_figheight(6)

plt.show()
