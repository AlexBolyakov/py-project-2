
# Part 1 - Classes and Object Orientation

# class Cupcake():

#     def __init__(self,name,price,flavor,filling,frosting):
#         self.name = name
#         self.price = price
#         self.flavor = flavor
#         self.filling = filling
#         self.frosting = frosting
#         self.sprinkles = []

#     def add_sprinkles(self,*args):
#         for item in args:
#             self.sprinkles.append(item)

# my_cupcake = Cupcake("Brownie",4.99,"Chocolate","Mousse","Rasberry")
# print(my_cupcake.sprinkles)

# my_cupcake.add_sprinkles("Oreo crumbs","Chocolate Chip", "Vanilla")
# print(my_cupcake.sprinkles)

# Part 2 - Parent/child classes, inheritance, polymorphism
# from abc import ABC, abstractmethod

# class Cupcake(ABC):

#     size = "regular"
#     def __init__(self,name,price,flavor,filling,frosting):
#         self.name = name
#         self.price = price
#         self.flavor = flavor
#         self.filling = filling
#         self.frosting = frosting
#         self.sprinkles = []

#     def add_sprinkles(self,*args):
#         for item in args:
#             self.sprinkles.append(item)
    
#     @abstractmethod

#     def calculate_price(self, quantity):
#         return quantity * self.price
    
# class Mini(Cupcake):
    
#     size = "mini"
#     def __init__(self,name,price,flavor,frosting):
#         self.name = name
#         self.price = price
#         self.flavor = flavor
#         self.frosting = frosting
#         self.sprinkles = []

#     def calculate_price(self, quantity):
#         return quantity * self.price

# mini_cupcake = Mini("Mini",2.99,"Cookie","Light")

# print("Mini cupcake name:", mini_cupcake.name)
# print("Mini cupcake price:", mini_cupcake.price)
# print("Mini cupcake flavor:", mini_cupcake.flavor)
# print("Mini cupcake size:", mini_cupcake.size)
# print("Mini cupcake frosting:", mini_cupcake.frosting)



# part 3 
# Creating and saving cupcake orders

from abc import ABC, abstractmethod
from pprint import pprint
import csv


class Cupcake(ABC):

    size = "regular"
    def __init__(self,name,price,flavor,filling,frosting):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.filling = filling
        self.frosting = frosting
        self.sprinkles = []

    def add_sprinkles(self,*args):
        for item in args:
            self.sprinkles.append(item)
    
    @abstractmethod

    def calculate_price(self, quantity):
        return quantity * self.price
    
class Regular(Cupcake):
    size = "regular"

    def calculate_price(self, quantity):
        return quantity * self.price

class Mini(Cupcake):
    
    size = "mini"
    def __init__(self,name,price,flavor,frosting):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []

    def calculate_price(self, quantity):
        return quantity * self.price


class Large(Cupcake):
    size = "large"

    def calculate_price(self, quantity):
        return quantity * self.price

# cupcake1 = Regular("Stars and Stripes", 2.99, "Vanilla", "Vanilla", "Chocolate")
# cupcake1.add_sprinkles("Red","White","Blue")
# cupcake2 = Mini("Oreo", .99, "Chocolate", "Cookies and Cream")
# cupcake2.add_sprinkles("Oreo pieces")
# cupcake3 = Large("Red Velvet", 3.99, "Red Velvet", "Cream Cheese", None)

# cupcake_list = [
#     cupcake1,
#     cupcake2,
#     cupcake3
# ]

def write_new_csv(file,cupcakes):
    with open(file, "w", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        
        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                writer.writerow({"size": cupcake.size, 
                                 "name": cupcake.name, 
                                 "price": cupcake.price,
                                 "flavor": cupcake.flavor, 
                                 "frosting": cupcake.frosting, 
                                 "filling": cupcake.filling, 
                                 "sprinkles": cupcake.sprinkles})
            else:
                writer.writerow({"size": cupcake.size, 
                                 "name": cupcake.name, 
                                 "price": cupcake.price, 
                                 "flavor": cupcake.flavor, 
                                 "frosting": cupcake.frosting, 
                                 "sprinkles": cupcake.sprinkles})


# write_new_csv("sample.csv", cupcake_list)


def get_cupcakes(file):
    
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        return reader

result = get_cupcakes("sample.csv")


def find_cupcake(file, name):
    for cupcake in get_cupcakes(file):
        if cupcake["name"] == name:
          return cupcake 
            
    return None


def view_order(file):
    
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        return reader



def add_cupcake_dictionary(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        print(type(cupcake))
        writer.writerow(cupcake)
        
        # if hasattr(cupcake, "filling"):
        #         writer.writerow({"size": cupcake["size"], 
        #                          "name": cupcake.name, 
        #                          "price": cupcake.price,
        #                          "flavor": cupcake.flavor, 
        #                          "frosting": cupcake.frosting, 
        #                          "filling": cupcake.filling, 
        #                          "sprinkles": cupcake.sprinkles})
        # else:
        #         writer.writerow({"size": cupcake.size, 
        #                          "name": cupcake.name, 
        #                          "price": cupcake.price, 
        #                          "flavor": cupcake.flavor, 
        #                          "frosting": cupcake.frosting, 
        #                          "sprinkles": cupcake.sprinkles})


# new_cupcake = Regular("Chocolate Heaven", 2.49, "Chocolate", "Chocolate Ganache", "Vanilla")
# new_cupcake.add_sprinkles("Chocolate Chips")
# add_cupcake_dictionary("sample.csv", new_cupcake)

# new_cupcake1 = Regular("Chocolate Heaven", 4.49, "Chocolate", "Browny", "Rasberry")
# new_cupcake1.add_sprinkles("Chocolate Chips")
# add_cupcake_dictionary("sample.csv", new_cupcake1)



# def read_csv(file):
    
#     with open(file) as csvfile:
#         reader = csv.DictReader(csvfile)

#         for row in reader:
#             pprint(row)

# read_csv("sample.csv")



