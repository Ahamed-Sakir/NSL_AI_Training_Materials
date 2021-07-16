class Shirt:
    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        self.color = shirt_color
        self.size = shirt_size
        self.style = shirt_style
        self.price = shirt_price

    def change_price(self, new_price):
        self.price = new_price

    def discount(self, discount):
        return self.price * (1 - discount)


#Shirt('Black', 'L', 'Formal', 1500)
shirt_one = Shirt('Red', 'M', 'Casual', 200)
print(shirt_one.price)
shirt_one.change_price(1500)
print('New Price of shirt_one:', shirt_one.price)
print('Discount price of shirt one:', shirt_one.discount(.5))

shirt_gallery = []
shirt_one = Shirt('Black', 'L', 'Casual', 1500)
shirt_two = Shirt('White', 'XL', 'Formal', 2000)
shirt_three = Shirt('Purple', 'L', 'Short shirt', 1200)

shirt_gallery.append(shirt_one)
shirt_gallery.append(shirt_two)
shirt_gallery.append(shirt_three)

for i in range(len(shirt_gallery)):
    print(shirt_gallery[i].color, shirt_gallery[i].price)