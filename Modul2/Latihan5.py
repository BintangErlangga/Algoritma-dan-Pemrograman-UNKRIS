# episode latihan logika dan komparasi

#membuat gabungan area rentang dari angka

#++++++++3------------10++++++++

inputUser = float(input('masukan angka yang bernilai\nkurang dari 3\natau\nlebih besar dari 10\n'))

#++++++++3
# Memeriksa angka kurang dari 3

iskurangdari =(inputUser<3)
print("kurang dari 3 =",iskurangdari)

isLebihdari =(inputUser>10)
print("lebih dari 10 =",isLebihdari)

#++++++++3------------10++++++++
isCorrect= iskurangdari or isLebihdari
print('angka yang anda masukan :',isCorrect)

# -----3++++++++10--------

# kasus irisan 
print("\n",10*"=","\n")
inputUser =float(input('masukan angka yang bernilai \nlebih dari 3\ndan\nkurang dari 10\n'))

# -----3++++++++++++++++++
# lebih dari 3

isLebihdari = inputUser >3
print('Lebih dari 3 =',isLebihdari)

#+++++++++++++++10-------
#kurang dari 10

isKurangdari = inputUser <10
print("kurang dari 1 =", isKurangdari)


#---3++++++++10--------
isCorrect = isKurangdari and isLebihdari
print("angka yang anda masukan: ", isCorrect)
