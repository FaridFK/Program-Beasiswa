#Program Beasiswa
Pilihan=1
while Pilihan !=0:
    print("1. Beasiswa Prestasi")
    print("2. Beasiswa Kurang Mampu")
    print("3. Beasiswa Luar Negri")
    
    pilihan=int(input("Masukan pilihan anda:"))
    print('')
    print('')
    
    if pilihan==1:
        masnama=input("Masukan nama kamu:")
        masnilai=int(input("Masukan nilai IPK kamu:"))
        if masnilai >=3.00:
            print('')
            print("Selamat anda terpilih untuk mendapatkan Beasiswa Prestasi.")
        else:
            print("Mohon maaf anda belum terpilih mendapatkan Beasiswa Prestasi, tetap semangat dan jangan putus asa!")
    print('')
    print('')

    if pilihan==2:
        masnama=input("Masukan nama kamu:")
        maswa=int(input("Masukan gaji perbulan orang tua, tanpa titik:"))
        if maswa <=2000000:
            print('')
            print("Selamat anda terpilih untuk mendapatkan bantuan Beasiwa Kurang Mampu.")
        else:
            print('')
            print("Mohon maaf anda belum terpilih mendapatkan bantuan Beasiswa Kurang Mampu, tetap semangat dan jangan putus asa!")
    print('')
    print('')
    
    if pilihan==3:
        masnama=input("Masukan nama kamu:")
        masnilai=int(input("Masukan nilai IPK kamu:"))
        if masnilai >=3.30:
            print('')
            print("Selamat anda terpilih untuk mendapatkan Beasiswa Luar Negri.")
        else:
            print('')
            print("Mohon maaf anda belum terpilih mendapatkan Beasiswa Luar Negri  tetap semangat dan jangan putus asa!")
    print('')
    print('')
