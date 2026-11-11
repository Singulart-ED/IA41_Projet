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
# 	for case in rows:
# 		print(case)


# def show_board():
# 	print("------------")
# 	for rows in gameBoard:
# 		print(rows)
# 	print("------------")

# show_board()


class Game:
	def __init__(self):
		self.max_number_of_pawns = 8
		self.number_of_players = 2
		self.gameBoard = np.array([[0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0]])

	def show_board(self):
		print("------------")
		for rows in self.gameBoard:
			print(rows)
		print("------------")

	def place_pawns(self, case):
		if (case >= 1 and case <= 25 ):
			match case:
				case 1 :
					self.gameBoard[0][0] = 1
				case 2 :
					self.gameBoard[0][1] = 1
				case 3 :
					self.gameBoard[0][2] = 1
				case 4 :
					self.gameBoard[0][3] = 1
				case 5 :
					self.gameBoard[0][4] = 1
				case 6 :
					self.gameBoard[1][0] = 1
				case 7 :
					self.gameBoard[1][1] = 1
				case 8 :
					self.gameBoard[1][2] = 1
				case 9 :
					self.gameBoard[1][3] = 1
				case 10 :
					self.gameBoard[1][4] = 1
				case 11 :
					self.gameBoard[2][0] = 1
				case 12 :
					self.gameBoard[2][1] = 1
				case 13 :
					self.gameBoard[2][2] = 1
				case 14 :
					self.gameBoard[2][3] = 1
				case 15 :
					self.gameBoard[2][4] = 1
				case 16 :
					self.gameBoard[3][0] = 1
				case 17 :
					self.gameBoard[3][1] = 1
				case 18 :
					self.gameBoard[3][2] = 1
				case 19 :
					self.gameBoard[3][3] = 1
				case 20 :
					self.gameBoard[3][4] = 1
				case 21 :
					self.gameBoard[4][0] = 1
				case 22 :
					self.gameBoard[4][1] = 1
				case 23 :
					self.gameBoard[4][2] = 1
				case 24 :
					self.gameBoard[4][3] = 1
				case 25 :
					self.gameBoard[4][4] = 1
		else:
			print("Case non valide")	



# Faire en sorte de pouvoir choisir la couleurs des pions
class Player:
	def __init__(self):
		self.number_of_pawns = 4
		self.color = "black"

	def move_pawns(self):
		print("test")
		


	# __str__ is a special method that controls what is returned when the object is printed
	# def __str__(self):
    # 	return f"{self.name} ({self.age})"





game = Game()
game.show_board()
for x in range(25):
	y = x + 1
	game.place_pawns(y)
	game.show_board()


p1 = Player()
# p1.place_pawns()

