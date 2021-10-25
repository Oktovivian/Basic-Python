# fungsi dengan menggunakan argumen sederhana
def siswa(nama):
    print('siswa ini bernama:',nama)
#siswa('mario')


print()
# fungsi dengan menggunakan keywords argumen
def guru(nama, pelajaran):
    print('guru ini bernama:',nama)
    print('mengajar:',pelajaran)

#guru(nama='popong',pelajaran='seni rupa')
#guru(pelajaran='olahraga',nama='endang')
# guru('olahraga','raihan') #ini contoh yang salah


print()
# fungsi dengan menggunakan defaults
def penjagaSekolah(nama, shift='siang', galak='tidak'):
    print('penjaga sekolah ini bernama:',nama)
    print('shiftnya:',shift)
    print('galak:',galak)

penjagaSekolah('entis')
penjagaSekolah('Maman','malam','iya')
penjagaSekolah('Abdul',galak='sangat')
#penjagaSekolah(shift='malam',galak='iya') #ini akan error karena nama tidak ada defaultnya


