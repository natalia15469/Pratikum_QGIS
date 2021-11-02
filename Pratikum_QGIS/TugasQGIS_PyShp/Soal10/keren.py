# Nama : Natalya Br Sidauruk
# NPM : 1194060
# Kelas : Diploma IV Teknik Informatika-3B
# 1194060 MOD 8 = 4, Dimana n adalah dijit NPM kedua dari belakang 
#Membangun Bujur Sangkar, dan angka 2 terakhir NPM = 6, jadi membangun 6 bujur sangkar

import shapefile
w=shapefile.Writer("soal10", shapeType=shapefile.POLYGON)
w.shapeType

w.field("kolom1","C")
w.field("kolom2","C")

w.record("pratt","satu")
w.record("pritt","dua")
w.record("prutt","tiga")
w.record("prett","empat")
w.record("prott","lima")
w.record("tuttt","enam")

w.poly([[[3,1], [8,1], [7,4], [2,4], [3,1]]])
w.poly([[[11,1], [16,1], [15,4], [10,4], [11,1]]])

w.poly([[[19,1], [24,1], [23,4], [18,4], [19,1]]])
w.poly([[[3,6], [8,6], [7,9], [2,9], [3,6]]])

w.poly([[[11,6], [16,6], [15,9], [10,9], [11,6]]])
w.poly([[[19,6], [24,6], [23,9], [18,9], [19,6]]])


w.close()