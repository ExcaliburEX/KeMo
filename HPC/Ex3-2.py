import random


a = []

for i in range(10):
    a.append(random.random() * 10)
    
print(max(a),min(a))