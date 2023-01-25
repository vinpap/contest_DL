import math

def neuron(X, weights, bias, activation="reLu"):
	

	result = bias
	for i, j in zip(weights, X):
		result += i*j

	if activation == "reLu": return reLu(result)
	elif activation == "sigmoid": return sigmoid(result)
	else: return result



def sigmoid(x): return 1/(1 + math.exp(-x))


def reLu(x):
	
	if x<0: return 0
	else: return x


X = [1, -3.1, -7.2, 2.1]
out_1 = neuron(X, [2.1, 1.2, 0.3, 1.3], bias=-3, activation="reLu")
out_2 = neuron(X, [0.1, 1.2, 4.9, 3.1], bias=-5, activation="reLu")
out_3 = neuron(X, [0.4, 2.6, 2.5, 3.8], bias=-3, activation="reLu")

print(out_1, out_2, out_3)


y_pred = neuron([out_1, out_2, out_3], 
	[1.1, -4.1, 0.7],
	bias=5.1,
	activation="sigmoid")
print(y_pred)

