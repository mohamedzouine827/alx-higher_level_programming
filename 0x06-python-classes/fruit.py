class Fruit:
    def __init__(self, name):
        self._name = name
    
    @property
    def fruit_name(self):
        print("{} is the element".format(self._name))
        return self._name
    
    @fruit_name.setter
    def fruit_name(self, value):
        print("value {} is the element".format(self._name))
        self._name = value

    @fruit_name.deleter
    def fruit_name(self):
        print("value {} is deleted".format(self._name))
        del self._name

if __name__ == "__main__":
    fruit = Fruit('Banana')
    print(fruit.fruit_name)
    del fruit.fruit_name
    