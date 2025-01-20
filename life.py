import random as ran
gender = ran.randint(0, 2)
mymalenames = [ "George", "john", "bart", "echo", "william", "wong",]
myfemalenames = ["Georgia", "ayesha", "candy"]
if gender == 2:
    myname = ran.choice(mymalenames)
elif gender == 1:
    myname = ran.choice(myfemalenames)
else:
    myname = input("name urslef ")
print("your name is", myname)
age = 0
momname = ran.choice(myfemalenames)
print("your mom is", momname)
momage = ran.randint(18, 40)
print("she is", momage, "years old")
dadname = ran.choice(mymalenames)
print("your dad is", dadname)
dadage = ran.randint(18, 100)
print("he is", dadage, "years old")
petExists = ran.randint(0, 1)
if petExists == 1:
    pettypes = ["dog", "cat", "lion", "snake", "rabbit", ]
    pettype = ran.choice(pettypes)
    petnames = ["good", "cinderella", "athena", "hercules", "george"]
    petname = ran.choice(petnames)
    petNeutered = ran.choice(["neutered", "non-neutered"])
    print("we have a", petNeutered, pettype, "named", petname)
Dead = 0
friends = {}
while Dead == 0:
    if age > 0 and age < 3:
        incedent = ran.choice([])
    print("\nyoure", age)
    print("do:\n1. age up\n2. interact\n3. assets")
    ans = input()
    if ans == "1":
        age += 1
