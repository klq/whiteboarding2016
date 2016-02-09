import numpy 
​
X_train = numpy.array([[1,1,1], [0,0,0],[-1,-1,-1],[10,10,10]])
y_train = numpy.array(['red', 'white','blue','chartreuse'])
X_test = numpy.array([1.1, 1.1, 1.1])
distance = []
k = 1
​
for train_p in X_train:
    distance.append(numpy.linalg.norm(X_test - train_p))
sorted_dist = [(x,y) for (x,y) in sorted(zip(distance,y_train))]
    
print  sorted_dist[:k]