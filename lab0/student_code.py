def order(data):
	n = len(data)

	if n == 0:
		return data

	for i in range(0, n - 1):
		for j in range(i+1, n):
			if data[i] > data[j]:
				m = data[i]
				data[i] = data[j]
				data[j] = m



	return data