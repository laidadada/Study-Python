age = 23
message = "Happy " + str(age)+ "rd Birthday!"
print(message)

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())
bicycles[0] = 'xiaoming'
print(bicycles)
bicycles.append('daming')
print(bicycles)
bicycles.insert(1,'xiaohong')
print(bicycles)
del bicycles[0]
print(bicycles)
P_bycles = bicycles.pop()
print(P_bycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")