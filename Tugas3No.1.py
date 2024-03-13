data_mahasiswa = {'yasmir':'123','Amir':'090104','ivan':'111','yasri':'222','yanti':'333','yasna':'444',
                  'yanto':'555','yuni':'666','yana':'777','yuta':'888'}

welcome = '''
******************************************************************
************** Selamat Datang Di Simak UNKHAIR *******************
********************** Silahkan Login*****************************
******************************************************************
'''
print (welcome)

username = input ("Masukan Userename Anda : ")
password = input ("Masukan Password Anda : ")

if username in data_mahasiswa and data_mahasiswa [username] == password :
    print ("Anda Berhasil Login Ke Simak")
else :
    print ("Login Gagal. Username Atau Password Yang Anda Masukan Salah")
