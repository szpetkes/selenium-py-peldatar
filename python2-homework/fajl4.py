with open("adat.txt", "r") as file4:
    lista = file4.readlines()

with open("adat3.txt", "w") as newfile4:
    newfile4.write(str(lista))
