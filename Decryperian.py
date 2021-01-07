
class Decryperian:

	def __init__(self, data):
		self.data = data

	def tpyrced(self):

		caracteres = list((self.data).encode())
		print("bytes: ", caracteres) # Visualizamos el valor de cada caracter convertido a bytes
		print("Caracteres: ",len(caracteres))
		# Plain text

		print("\n[*] Plain text: " + self.data + "\n")

		# Encrypt algorithm

		key = input("KEY: ") # Pedimos al usuario una llave para la encriptacion de los datos.
		key_caracteres = list((key.encode()))

		print("key bytes: ", key_caracteres,"\n") # Visualizamos el valor de cada caracter convertido a bytes

		cypher_text = [item for item in map(lambda x, y : x + y, caracteres, key_caracteres)] # Llamamos a una funcion anonima con 'lambda', asignamos argumentos y un operador.
		print("1: ",cypher_text)
		cypher_text = [int(item) for item in map(lambda x : x - 50, cypher_text)] 
		print("2: ",cypher_text)
		cypher_text = [item for item in map(lambda x : chr(x), cypher_text)]
		print("3: ",cypher_text,"\n")

		# Cypher text

		print("[*] Cypher text: " , cypher_text , "\n")
		return cypher_text