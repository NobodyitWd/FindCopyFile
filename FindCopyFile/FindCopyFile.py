import os

def Del(mass):
    for i in mass:
        os.remove(i)
        print("Copy[ies] deleted.")

chdir = input("Input full path:    ") # Выберем директорию.
print("Please stand by. it's may take time.")
try:
    os.chdir(chdir)
except:
    print("Incorrect path!")
    exit(0)

rem = [] # Здесь копии.
d = os.listdir()
di = []

for i in d: # Получим список файлов.
    if not os.path.isdir(i):
        di.append(i)

finded = []
for x in range(len(di)):
    for y in range(len(di)):
        if x != y and di[y] not in finded: # Проверим каждый объект на наличие его копий. Если есть копии: первый объект остается нетронутым. Остальные записываем в тетрадь смерти.

            file1 = open(di[x], "rb")
            file2 = open(di[y], "rb")

            reader1 = file1.read()
            reader2 = file2.read()

            file1.close()
            file2.close()

            if reader1 == reader2:
                finded.append(di[x])
                if di[x] not in rem:
                    rem.append(di[x])

if len(rem) == 0:
    print("Good News! u haven't copies!")
    exit(0)

print("This copies will be deleted.")
for i in range(len(rem)):
    print(str(i) + " " + rem[i])
delete = input("Do you wanna to delete copies? you also can [S]elect the file to be deleted [Y/N/S]:    ")
delete = delete.upper()

if delete == "Y":
    Del(rem)
if delete == "S": # Выберем копии которые стоит удалить. Следует писать " 1 2 3 4 8 91011121314". Если число однозначное добавь перед ним пробел.
    print("Select copies. Example:  1 3 4 5 9101112161748. If number < 10 space + number. Else just input number")
    sel = input("Input copies numbers:   ")
    l = len(sel)
    c = l/2
    c = int(c)
    x = 0
    y = 2
    newrem = []
    for i in range(c):
        q = sel[x:y]
        q = q.replace(" ", "")
        newrem.append(rem[int(q)])
        x += 2
        y += 2
    Del(newrem)
if delete == "N":
    print("Мы принимаем ваш выбор.")
    exit(0)
else:
    print("Input correct value!")
    exit(0)