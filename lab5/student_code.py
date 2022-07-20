
import common

#helpful, but not needed
class variables:
	counter=0


def check_complete_fn(sudoku):

	for y in range(9):
		for x in range(9):
			if(sudoku[y][x] == 0):
				return False
				
		
	
	return True



def check_empty_fn(domain):
	for y in range(9):
		for x in range(9):
			
			if(domain[y][x] == []):
				return False
			
	return True












def copy_fn(domain):
	new_domain = []
	for i in range(len(domain)):
		new_domain.append([row[:] for row in domain[i]])

	return new_domain






def update_fn(sudoku, domain):
	for y in range(9):
		for x in range(9):
			new_list = []

			for i in range(1, 10):
				if(sudoku[y][x] == 0):

					if(common.can_yx_be_z(sudoku, y, x, i)):

						new_list.append(i)
				else:
					new_list.append(sudoku[y][x])
			domain[y][x] = new_list

	return domain		

def forward_recursive(sudoku, domain):
	variables.counter += 1


	if(check_complete_fn(sudoku) == True):
		return True
	else:

		for y in range(9):
			for x in range(9):
				if(sudoku[y][x] == 0):
					for j in range(1, 10):
						if(common.can_yx_be_z(sudoku, y, x, j) == True):
							old_domain = copy_fn(domain)
							sudoku[y][x] = j
							domain = update_fn(sudoku, domain)
							if(check_empty_fn(domain) == True):
								result = forward_recursive(sudoku, domain)
								if result == True:
									return True
							else:	
								domain = copy_fn(old_domain)
							sudoku[y][x] = 0

					return False

						

			

def backtracking(sudoku):
	variables.counter += 1

	if(check_complete_fn(sudoku) == True):
		return True

	else:
		for y in range(9):
			for x in range(9):
				if(sudoku[y][x] == 0):
					for j in range(1, 10):
						if(common.can_yx_be_z(sudoku, y, x, j) == True):
							sudoku[y][x] = j
							result = backtracking(sudoku)
							if result == True:
								return True
							sudoku[y][x] = 0
					return False




def sudoku_backtracking(sudoku):
	variables.counter = 0
	backtracking(sudoku)

	return variables.counter



def sudoku_forwardchecking(sudoku):
	variables.counter = 0
	#put your code here
	domain =  [[[0 for i in range(9)] for j in range(9)] for k in range(9)]
	
	domain = update_fn(sudoku, domain)
	forward_recursive(sudoku, domain)
	

	return variables.counter