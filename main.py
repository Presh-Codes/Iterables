MyList = ["apple", "mango", "grape", "pineapple", "watermelon", "guava", "cherry", "blue berry", "banana", "pear"]
print(MyList[2])
for x in MyList:
    print(x)
print("\n\n")

MyTuple = ("apple", "mango", "grape", "pineapple", "watermelon", "guava", "cherry", "blue berry", "banana", "pear")
print(MyTuple[4])
for y in MyTuple:
    print(y)
print("\n\n")

MySet = {"apple", "mango", "grape", "pineapple", "watermelon", "guava", "cherry", "blue berry", "banana", "pear"}
print("banana" in MySet)
for c in MySet:
    print(c)
print("\n\n")

MyDictionary = {
    "name": "Precious",
    "class": "SS3",
    "age": 16,
    "height": 4.6,
    "school": "Shalom Science and Technology Academy",
    "state": "Enugu"
}
print(MyDictionary["name"])
for n in MyDictionary:
    print(MyDictionary[n])