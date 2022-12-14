M = [[1 , 2 , 3],                                   #матриця 3*3 у вигляді вложених списків
     [4, 5, 6],
     [7, 8, 9]]
print(M)

print(M[1])                                         #виводимо другу строку
print(M[1][2])                                      #виводимо 3[2] елемент 2[1] строки

col12 = [row[1] for row in M]                       #зібрати елементи в стовпець 2
print(col12)
print(M)                                            #матриця не змінилася

print([row[1] + 1 for row in M])                    #додає 1 до кожного елемента в стовпці 2
print([row[1] for row in M if row[1] % 2 == 0])     #фільтрування і вивід парних елементів в стовпці 2

print(M)

diag = [M[i][i] for i in [0, 1, 2]]                 #збирає діагональ з матриці
print(diag)

doubles = [c * 2 for c in 'spam']                   #повторює символи з строки
print(doubles)

print(list(range(4)))                               #список від 0 до 3
print(list(range(-6, 7, 2)))                        #список від -6 до 6 з кроком 2