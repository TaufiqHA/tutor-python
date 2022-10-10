# tipe data : angka satuan (integer)
from ctypes import c_double, c_char, c_long
integer = 1
print("data : ", integer)
print("- bertipe : ", type(integer))

# tipe data : angka dengan koma / decimal (float)
float = 1.2
print("data : ", float)
print("- bertipe : ", type(float))

# tipe data : kumpulan karakter (string)
string = "Taufiq Hidayah Abdullah"
print("data : ", string)
print("- bertipe : ", type(string))

# tipe data : biner atau true / false (boolean)
boolean = False  # khusus untuk type data boolean harus menggunakan huruf kapital pada awal kata True dan Flase
print("data : ", boolean)
print("- bertipe : ", type(boolean))

# type data khusus
# bilangan kompleks
complex = complex(5, 6)
print("data : ", complex)
print("- bertipe : ", type(complex))

# type data dari bahasa c
# double
double = c_double(1.5)
print("data : ", double)
print("- bertipe : ", type(double))

# char
# char = c_char("taufiq")
# print("data : ", char)
# print("- bertipe : ", type(char))

