print("We gonna learn loops in Python!")

# loops

for i in range(6):
  print(i)

names = ["Ryujin", "Lia", "Chaeryeong", "Yuna", "Yeji"]

for name in names:
  print(name)

name = "Chaeryeong"

for char in name: 
  print(char)

# Dictionaries 

players = {"Ryuujin": "19", "Liia": "20"}
print(players["Ryuujin"])

players = {"Ryujin": "21", "Lia": "22"}
print(players["Lia"])

players["Yeji"] = "22"

print(players["Yeji"])

#Functions 

def square(x): 
  return x * x

for i in range(10):
  print(f"The square of {i} is {square(i)}")
