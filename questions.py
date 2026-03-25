import random
categorias ={
	"Lenguajes" : ["python"],
	"Estructuras" : ["lista", "cadena", "bucle"],
	"Conceptos" : ["programa", "variable", "funcion", "entero"]
}

print("¡Bienvenido al Ahorcado!")
print("Categorias disponible: ")
for nombre in categorias.keys():
	print(f"-{nombre}")

seleccion = ""
while seleccion not in categorias:
	seleccion = input("Elegi una categoria: ").capitalize() # No dara error si se usa minuscula en vez de mayuscula o viceversa
	if seleccion not in categorias:
		print("Esa categoria no existe. Intenta de nuevo.")

lista_de_palabras = categorias[seleccion]
palabras_mezcladas = random.sample(lista_de_palabras, k =len(lista_de_palabras))

score = 0


for word in palabras_mezcladas:
	attempts = 6
	guessed = [] 
	while attempts > 0:
		# Mostrar progreso: letras adivinadas y guiones para las que faltan
		progress = ""
		for letter in word:
			if letter in guessed:
				progress += letter + " "
			else:
				progress += "_ "
		print(progress)
		# Verificar si el jugador ya adivinó la palabra completa
		if "_" not in progress:
			print("¡Ganaste!")
			score += 6
			break
		print(f"Intentos restantes: {attempts}")
		print(f"Letras usadas: {', '.join(guessed)}")
		
		letter = input("Ingresá una letra: ").lower()
		
		#Se fija que el usario ingrese un solo caracter y que sea una letra
		if len(letter) != 1 or not letter.isalpha():
			print ("Entrada no valida.")
			print()
			continue
		
		if letter in guessed:
			print("Ya usaste esa letra.")
			score -= 1
		elif letter in word:
			guessed.append(letter)
			print("¡Bien! Esa letra está en la palabra.")
		else:
			guessed.append(letter)
			attempts -= 1
			score -= 1
			print("Esa letra no está en la palabra.")

		print()

	else:
		print(f"¡Perdiste! La palabra era: {word}")
		score = 0

print (f"Tu puntaje final es: {score} ")