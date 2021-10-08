import pickle
#객체 하나씩 불러옴
with open("object.bin", "rb") as f:
    p1 = pickle.load(f)
print(p1)
print(p1.name)
print(p1.color)
#객체 여러개 불러옴
with open('objects.bin', 'rb') as f:
    people = pickle.load(f)
# print(people)
# print(people[0])
# print(people[1])
for person in people:
    print(person)