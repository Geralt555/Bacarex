#  Дано предложение. Определить порядковые номера первой пары одинаковых соседних
#  символов. Если таких символов нет, то должно быть напечатано соответствующее
#  сообщение.

line = "Змееед любит растения "
ti, tv = 0, line[0]
for ind, val in enumerate(line):
    if val == tv and ind - ti == 1:
        print(val, ' -> ', ti + 1, ind + 1)
        break
    ti, tv = ind, val
