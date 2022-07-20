import common


def classify_fn(weights, features):
	y_new = ((weights[0]*features[0]) + (weights[1]*features[1])) + weights[2]

	

	if y_new > 0:

		return 1
	else:
		return 0



	
	
def classify_multiclass_fn(weights, features):

	# evaluations = []
	index = 0

	max_value = -1000
	for i in range(10):
		evaluations = ((weights[i][0]*features[0]) + (weights[i][1]*features[1]))
		if evaluations > max_value:
			max_value = evaluations
			index = i

	

	return index





















def part_one_classifier(data_train, data_test):
	# PUT YOUR CODE HERE
	# Access the training data using "data_train[i][j]"
	# Training data contains 3 cols per row: X in 
	# index 0, Y in index 1 and Class in index 2
	# Access the test data using "data_test[i][j]"
	# Test data contains 2 cols per row: X in 
	# index 0 and Y in index 1, and a blank space in index 2 
	# to be filled with class
	# The class value could be a 0 or a 1

	weights = [0, 0, 1]
	features = [0, 0]
	correct_counts = 0
	
	while correct_counts != common.constants.TRAINING_SIZE:
		correct_counts = 0
		for i in range(common.constants.TRAINING_SIZE):

				features[0] = data_train[i][0]
				features[1] = data_train[i][1]
				y = data_train[i][2]
				y_pred = classify_fn(weights, features)

				if y == y_pred:
					correct_counts += 1
					
				else:
					if y_pred == 1:
						weights[0] = weights[0] - (0.01*features[0])
						weights[1] = weights[1] - (0.01*features[1])
						weights[2] = weights[2] -(0.01*1)
					if y_pred == 0:
						weights[0] = weights[0] + (0.01*features[0])
						weights[1] = weights[1] + (0.01*features[1])
						weights[2] = weights[2] +(0.01*1)


				





	for e in range(common.constants.TEST_SIZE):
		features[0] = data_test[e][0]
		features[1] = data_test[e][1]
		data_test[e][2] = classify_fn(weights, features)


	





	


def part_two_classifier(data_train, data_test):
	# PUT YOUR CODE HERE
	# Access the training data using "data_train[i][j]"
	# Training data contains 3 cols per row: X in 
	# index 0, Y in index 1 and Class in index 2
	# Access the test data using "data_test[i][j]"
	# Test data contains 2 cols per row: X in 
	# index 0 and Y in index 1, and a blank space in index 2 
	# to be filled with class
	# The class value could be a 0 or a 8


	weights = [[0 for i in range(2)] for i in range(10)]
	features = [0, 0]
	correct_counts = 0

	while correct_counts != common.constants.TRAINING_SIZE:
		# print("inside while loop")
		correct_counts = 0
		
		for i in range(common.constants.TRAINING_SIZE):
			# print("inside for loop")
			features[0] = data_train[i][0]
			features[1] = data_train[i][1]
			y = data_train[i][2]

			y_pred = classify_multiclass_fn(weights, features)

		
		

			# print("y", y)
			# print("y_pred", y_pred)

			if y == y_pred:
				correct_counts += 1
				# print("correct counts", correct_counts)
			else:
				#true label
				weights[int(y)][0] = weights[int(y)][0] + (0.01*features[0])
				weights[int(y)][1] = weights[int(y)][1] + (0.01*features[1])

				weights[int(y_pred)][0] = weights[int(y_pred)][0] - (0.01*features[0])
				weights[int(y_pred)][1] = weights[int(y_pred)][1] - (0.01*features[1])



	for e in range(common.constants.TEST_SIZE):
		features[0] = data_test[e][0]
		features[1] = data_test[e][1]

		data_test[e][2] = classify_multiclass_fn(weights, features)

