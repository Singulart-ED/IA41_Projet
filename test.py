
# Représentation possible du Teeko
# Une matrice 5 * 5
# Un double tableau 5 * 5

# Liste 
# w, h = 5, 5
# Matrix = [[0 for x in range(w)] for y in range(h)] 

# i = 0
# j = 0

# for i in range(5):
#     print(Matrix[i])
#     ++i


# # Tableau à 2 dimensions
import numpy as np

# arr = np.array([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])

# # print(arr)

# for i in range(5):
#     print(arr[i])
#     ++i







# arr = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) # Temps total : 0.004260 secondes
        # for x in arr:
        #     print("I")

arr = np.array([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]) #
        # for x in arr:
        #     for y in x:
        #         print("I")

repeats2 = 2
repeats = 44

import time
for _ in range(repeats2):
    average_time = 0
    for _ in range(repeats):
        start_time = time.perf_counter() #Timer Debut
        
        for x in arr:
            for y in x:
                print("I")
        
        end_time = time.perf_counter() ##Timer Fin    
        average_time += end_time - start_time

        
average_time /= repeats2


print(f"Temps total : {average_time:.6f} secondes")
    