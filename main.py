class Human:
    def __init__(self,name,age):
        self.Name=name
        self.Age=age

human_list=[Human("Andriy",22),
            Human("Bohdan",52),
            Human("Artem",19)]

print(human_list)

human_iter=iter(human_list)

for elem in human_iter:
    print(elem.Name, elem.Age)


