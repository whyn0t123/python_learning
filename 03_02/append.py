motorcycles=[]

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

motorcycles.insert(0,'ducati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycle=motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

last_owned=motorcycles.pop()
print(f"The last motorcycle I owned was the a {last_owned.title()}.")

motorcycles.remove('honda')
print(motorcycles)