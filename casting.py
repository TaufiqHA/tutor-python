# casting adalah merubah type data ke type data yang lain

# tipe data integer

print("===STRING===")
integer = 9
print("data : ", integer, " type : ", type(integer))

float = float(integer)
print("data : ", float, ", type : ", type(float))

string = str(integer)
print("data : ", string, ", type : ", type(string))

boolean = bool(integer)  # nilainya akan false jika nilai dari integer = 0
print("data : ", boolean, ", type : ", type(boolean))

# tipe data float
print("===FLOAT===")
float = 9.0
print("data : ", float, " type : ", type(float))

integer = int(float)
print("data : ", integer, ", type : ", type(integer))

string = str(float)
print("data : ", string, ", type : ", type(string))

boolean = bool(float)  # nilainya akan false jika nilai dari float = 0
print("data : ", boolean, ", type : ", type(boolean))

# tipe data boolean
print("===BOOLEAN===")
boolean = True
print("data : ", boolean, " type : ", type(boolean))

integer = int(boolean)
print("data : ", integer, ", type : ", type(integer))

string = str(boolean)
print("data : ", string, ", type : ", type(string))

float = float(boolean)
print("data : ", float, ", type : ", type(float))
