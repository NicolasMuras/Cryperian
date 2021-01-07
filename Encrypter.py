from random import randint, uniform,random

print("Encripta datos utilizando programacion funcional, un metodo eficaz para transformar datos y ahorrar recursos.")
print("[!] Debe asegurarse de que la cantidad de caracteres de su palabra y su KEY coincidan.\n")

datos = input("Introduce la palabra a encriptar: ")
output_name = input("Output file name: ")
caracteres = list((datos).encode())
print("bytes: ", caracteres) # Visualizamos el valor de cada caracter convertido a bytes
print("Caracteres: ",len(caracteres))
# Plain text

print("\n[*] Plain text: " + datos + "\n")

# Encrypt algorithm

key = input("KEY: ") # Pedimos al usuario una llave para la encriptacion de los datos.
if key == "":
	while len(key) < len(caracteres): key = key + str(randint(32,126))
	print(key)
key_caracteres = list((key.encode()))

print("key bytes: ", key_caracteres,"\n") # Visualizamos el valor de cada caracter convertido a bytes

cypher_text = [item for item in map(lambda x, y : x + y, caracteres, key_caracteres)] # Llamamos a una funcion anonima con 'lambda', asignamos argumentos y un operador.
print("1: ",cypher_text)
cypher_text = [int(item) for item in map(lambda x : x - 50, cypher_text)] 
print("2: ",cypher_text)
cypher_text = [item for item in map(lambda x : chr(x), cypher_text)]
print("3: ",cypher_text,"\n")

# Cypher text

key_file = open("{}".format(output_name),"w")
key_file.write("""def tpyrc(key_2, key_1):
	print("0: ",key_2)
	key_2 = [item for item in map(lambda x : ord(x), key_2)]
	print("1: ",key_2)
	key_2 = [int(item) for item in map(lambda x : x + 50, key_2)]
	print("2: ",key_2)
	key_2 = [item for item in map(lambda x, y : x - y, key_2, key_1)]
	print("3: ",key_2)
	def toChar(dato):
		if isinstance(dato, list):
			return [chr(x) for x in dato]
		else:
			return dato.chr()

	new = toChar(key_2)
	plain = "".join(list(map(str, new)))
	print("4: ",plain)
	return plain
#-------------------------------------------------------------------------------------------------------------
key_1 = {}
key_2 = {}
exec(tpyrc(key_2, key_1))""".format((str(key_caracteres)),(str(cypher_text))))
key_file.close()

print("[*] Cypher text: " , cypher_text , "\n")

# Decrypt algorithm

cypher_text = [item for item in map(lambda x : ord(x), cypher_text)]
print("1: ",cypher_text)
cypher_text = [int(item) for item in map(lambda x : x + 50, cypher_text)]
print("2: ",cypher_text)
cypher_text = [item for item in map(lambda x, y : x - y, cypher_text, key_caracteres)]
print("3: ",cypher_text)

def toChar(dato): # Funcion recursiva para transformar enteros a caracteres.
	if isinstance(dato, list):
		return [chr(x) for x in dato]
	else:
		return dato.chr()

nueva = toChar(cypher_text)
print("4: ",nueva,"\n")

# Plain text
plain_text = "".join(list(map(str, nueva))) # Unimos la lista en una cadena.
print("[*] Plain text: " , plain_text , "\n") # Resultado final !