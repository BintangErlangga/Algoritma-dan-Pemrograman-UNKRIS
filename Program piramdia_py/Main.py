def piramida (tinggi):
    count = 1
    spasi =int(tinggi/2)

    while True :
        if (count%2):
            print(" "*spasi,"*"*count)
            spasi -= 1
            count += 1
        else :
            count +=1
            continue
        if count > tinggi :
            break

        
def input_tinggi():
    max = 10
    tinggi = input("Masukkan Tinggi Yang diinginkan ("+ str(max) + ") : ")
    if not tinggi.isdigit():
        print("tolong masukan angka :" )
        return input_tinggi()
    tinggi = int(tinggi)
    if tinggi > max :
        print(f'Maximal tinggi adalah ',str(max))
        return input_tinggi
    return piramida(tinggi)

input_tinggi()