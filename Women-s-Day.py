
import math
from colorama import Fore

n = 4
for i in range(0, 2 * n + 1): 
	
	for j in range(0, 2 * n + 1): 
	
		center_dist = math.sqrt((i - n) * (i - n) 
							+ (j - n) * (j - n)) 
		if (center_dist > n - 0.5
				and center_dist < n + 0.5): 
			print("0", end = "") 
		else: 
			print(Fore.RED,end = " ") 
	
	if (i == n+4): 
		print(Fore.RED,"2024",end = "")
	print("") 

for i in range(0, 2 * n + 1): 
	
	for j in range(0, 2 * n + 1): 
		center_dist = math.sqrt((i - n) * (i - n) 
							+ (j - n) * (j - n)) 
		if (center_dist > n - 0.5
				and center_dist < n + 0.5): 
			print("0", end = "") 
		else: 
			print(end = " ") 
	if (i == n-4): 
		print(Fore.RED,"Happy Women's Day",end = "") 
	print("") 
	
	
