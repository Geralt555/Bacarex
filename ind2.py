line = "В соединении молекул"

for ind in range(len(line) - 1):
    if line[ind] == line[ind + 1]:
        print(ind + 1, ind + 2)
        break
else:
    print('Таких нет!!!')
