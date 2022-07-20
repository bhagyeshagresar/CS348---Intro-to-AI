import common
import math #note, for this lab only, your are allowed to import math








def interval(delta):
	empty_list = []

	
	for i in range(2000):
		empty_list.append((delta*i) - 10)

	
	return empty_list











def detect_slope_intercept(image):
	# PUT YOUR CODE HERE
	# access the image using "image[y][x]"
	# where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT 
	# set line.m and line.b
	# to create an auxiliar bidimentional structure 
	# you can use "space=common.init_space(heigh, width)"
	line=common.Line()
	line.m=0
	line.b=0

	h_map = common.init_space(2000,2000)
	m_list = interval(0.01)
	
	
	for y in range(0, common.constants.WIDTH):
		for x in range(0, common.constants.HEIGHT):
			if(image[y][x] == 0):

				for m in m_list:
					m1= int((m*100)+1000)
					b = int(y - (m*x))
					
					if (b >= -1000 and b < 1000):
						h_map[b+1000][m1] += 1
					

					

	
	
	h_max = 0
	for b in range(2000):
		for m in range(2000):
			if(h_map[b][m] > h_max):
				h_max = h_map[b][m]
				m2 = (m - 1000)*0.01
				line.m = m2
				line.b = b-1000
	
	

	return line



					


def detect_circles(image):
	# PUT YOUR CODE HERE
	# access the image using "image[y][x]"
	# where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT 
	# to create an auxiliar bidimentional structure 
	# you can use "space=common.init_space(heigh, width)"

	h_map = common.init_space(200,200)

	for y in range(0, common.constants.WIDTH):
		for x in range(0, common.constants.HEIGHT):
			if(image[y][x] == 0):
				for a in range(200):
					for b in range(200):
						distance = (math.sqrt(math.pow(a-x, 2) + math.pow(b-y, 2)))
						if (distance >= 29.6 and distance <= 30.00):
							h_map[a][b] += 1
							

	num_circles = 0
	for a in range(200):
		for b in range(200):
			if h_map[a][b] > 40:
				num_circles += 1




				 




	return num_circles/2
				

