import greeting
greeting.do_stuff()

def create_set():
    fruits = {'apple','orange'}
    fruits.add('watermelon')
    fruits.discard('orange')
    print(fruits)
    if 'apple' in fruits:
        print('Yeeee')

def create_dict():
    prices = {'apples': 2.25, 'oranges': 1.0}
    if 'strawberries' not in prices:
        print('I have no idea how much strawberries cost')
    prices['strawberries'] = 1.99 #add entry to dict

def higher_order(): #TODO:
    #bool = special_order(-10,3,abs)

def lambduh():
    #lambda parameters: return value
    square = lambda x: x ** 2
    square(5) #returns 25

class FruitShop(object):

    def __init__(self, name, prices):
        self.name = name
        self.prices = prices

    def get_price_per_pound(self, fruit):
        if fruit in self.prices:
            return self.prices[fruit]
        else:
            return None


