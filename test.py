import numpy as np
import time


# Pour Calculer le temps d'itération
# average_time = 0
# for _ in range(repeats):
# 	start_time = time.perf_counter() #Timer Debut

# 	for x in arr:
# 		for y in x:
# 			print("I")

# 	end_time = time.perf_counter() ##Timer Fin    
# 	average_time += end_time - start_time

# print(f"Temps total : {average_time:.6f} secondes")



# arr = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) # Temps total : 0.007072 secondes Un tableau normal est environ 2 fois plus rapide.
        # for x in arr:
        #     print("I")


# Création du plateau vide
# gameBoard = np.array([[0, 0, 0, 0, 0], 
#                 [0, 0, 0, 0, 0], 
#                 [0, 0, 0, 0, 0], 
#                 [0, 0, 0, 0, 0], 
#                 [0, 0, 0, 0, 0]]) # Temps total : 0.016867 secondes

# for rows in gameBoard:
# 	for element in rows:
# 		print(element)


# def show_board():
# 	print("------------")
# 	for rows in gameBoard:
# 		print(rows)
# 	print("------------")

# show_board()


class Game:
	def __init__(self):
		self.max_number_of_pawns = 8
		self.actual_number_of_pawns = 0
		self.max_number_of_players = 2
		self.gameBoard = np.array([[0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0]])

	def element_to_coordinates(self, element) :
		match element:
			case 1 :
				return 0,0
			case 2 :
				return 0,1
			case 3 :
				return 0,2
			case 4 :
				return 0,3
			case 5 :
				return 0,4
			case 6 :
				return 1,0
			case 7 :
				return 1,1
			case 8 :
				return 1,2
			case 9 :
				return 1,3
			case 10 :
				return 1,4
			case 11 :
				return 2,0
			case 12 :
				return 2,1
			case 13 :
				return 2,2
			case 14 :
				return 2,3
			case 15 :
				return 2,4
			case 16 :
				return 3,0
			case 17 :
				return 3,1
			case 18 :
				return 3,2
			case 19 :
				return 3,3
			case 20 :
				return 3,4
			case 21 :
				return 4,0
			case 22 :
				return 4,1
			case 23 :
				return 4,2
			case 24 :
				return 4,3
			case 25 :
				return 4,4

		
	def show_board(self):
		print("------------")
		for rows in self.gameBoard:
			print(rows)
		print("------------")

	def place_pawns(self, element, id):
		if self.check_if_element_is_valid(element) :
			if self.actual_number_of_pawns <= self.max_number_of_pawns :
				if self.check_if_empty(element) :
					x,y = self.element_to_coordinates(element)
					self.gameBoard[x][y] = id
					self.actual_number_of_pawns+=1
				else :
					print("Un pion est déjà sur cette case")

	def check_if_empty(self, element):
		x,y = self.element_to_coordinates(element)
		if self.gameBoard[x][y] == 0 :
			return True
		else :
			return False

	def check_if_element_is_valid(self, element) :
		if isinstance(element, int):
			if (element >= 1 and element <= 25 and element ):
				return True
			else:
				print("Element non valide, element entre 1 et 25")
				return False
		else:
			print("Element non valide, element doit être de type int")
			return False

	def move_pawns(self, from_element, to_element, id):
		if self.check_if_element_is_valid(from_element) and self.check_if_element_is_valid(to_element) :
			if self.check_if_move_is_valid(from_element, to_element) :
				if self.check_pawns_id(from_element, id) :
					if self.check_if_empty(to_element) :
						x,y = self.element_to_coordinates(to_element)
						self.gameBoard[x][y] = id
						x,y = self.element_to_coordinates(from_element)
						self.gameBoard[x][y] = 0
					else :
						print("Un pion est déjà sur cette case")
				else :
					print("Ce pion ne t'appartiens pas")
			else :
				print("Déplacement impossible, seules les cases autour du pion sont autorisées.")

	def check_pawns_id(self, element, id):
		x,y = self.element_to_coordinates(element)
		if self.gameBoard[x][y] == id :
			return True
		else :
			return False

	def check_if_move_is_valid(self, from_element, to_element):
		x,y = self.element_to_coordinates(from_element)
		a,b = self.element_to_coordinates(to_element)
		
		# liste des points à check 
		if ( 
			x == a and y+1 == b or # à droite 
			x == a and y-1 == b or # à gauche
			x+1 == a and y == b or # en haut
			x-1 == a and y == b or # en bas
			x+1 == a and y+1 == b or # en haut à droite 
			x+1 == a and y-1 == b or # en haut à gauche 
			x-1 == a and y+1 == b or # en bas à droite 
			x-1 == a and y-1 == b    # en bas à gauche 
		) :
			return True
		return False


	# def check_win_condition(self):
	# 	self.gameBoard[x][y]


# Faire en sorte de pouvoir choisir la couleurs des pions
class Player:

	compteur_id = 0  

	def __init__(self):
		self.number_of_pawns = 4
		self.color = "black"
		Player.compteur_id += 1
		self.id = Player.compteur_id


	def move_pawns(self):
		print("test")

	def place_pawns(self, element):
		if self.number_of_pawns > 0 :
			if game.place_pawns(element, self.id) :
				self.number_of_pawns-=1
		else:
			print("Plus de jeton à placer")		

	def move_pawns(self, from_element, to_element):
		game.move_pawns(from_element, to_element, self.id)


	# __str__ is a special method that controls what is returned when the object is printed
	# def __str__(self):
    # 	return f"{self.name} ({self.age})"


game = Game()
game.show_board()

p1 = Player()
# print(p1.id)
p1.place_pawns(5)
p1.place_pawns(10)
p1.place_pawns(13)
p1.place_pawns(15)
p1.place_pawns(16)


p2 = Player()
# print(p2.id)
p2.place_pawns(21)
p2.place_pawns(22)
p2.place_pawns(23)
p2.place_pawns(212)
p2.place_pawns("")
game.show_board()
p2.place_pawns(15)
p2.place_pawns(24)
p2.place_pawns(25)


game.show_board()

p1.move_pawns(16,18)
p1.move_pawns(16,19)
p1.move_pawns(16,21)
game.show_board()






# Pour tester de remplir le plateau
# for x in range(25):
# 	y = x + 1
# 	game.place_pawns(y)
# 	game.show_board()



		# # liste des points à check 
		# self.gameBoard[x][y+1] # à droite 
		# self.gameBoard[x][y-1] # à gauche
		# self.gameBoard[x+1][y] # en haut 
		# self.gameBoard[x-1][y] # en bas
		# self.gameBoard[x+1][y+1] # en haut à droite 
		# self.gameBoard[x+1][y-1] # en haut à gauche 
		# self.gameBoard[x-1][y+1] # en bas à droite 
		# self.gameBoard[x-1][y-1] # en bas à gauche 