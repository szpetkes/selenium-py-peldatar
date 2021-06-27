with open("adat.txt", "r") as file3:
    list1 = file3.readlines()
    list2 = []
    for i in list1:
        list2.append(i.strip())

with open("adat2.txt", "w") as newfile3:
    newfile3.write(str(list2))
