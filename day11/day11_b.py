import os 
import math
from dataclasses import dataclass

def translate_item(intiger,divisible):
    base = math.floor(intiger/divisible)
    rest = intiger%divisible
    return Item(base,rest,divisible)

@dataclass 
class Item: 
    base: int
    rest: int
    divisible: int  
    
    def add(self,value):
        new_rest = self.rest + value 
        if new_rest% self.divisible == 0: 
            self.base += 1 
        else: 
            self.rest = new_rest
    
    def multiple(self,value): 
        temp_item = translate_item(self.rest * value,self.divisible)
        self.rest = temp_item.rest
        self.base = temp_item.base + self.base * value

    def modulo(self,value): 
        (self.base%value * self.divisible%value + self.rest)%value 

@dataclass
class Operation:
    operation: str 
    second_value: int 
    def calculate(self,item:Item): 
        if self.operation == "+":
            item.add(int(self.second_value))
        elif self.operation == "*": 
            if self.second_value == 'old': 
                item.multiple(item.divisible)
            else: 
                item.multiple(int(self.second_value))
        return item 
           
@dataclass
class Package:
    index: int 
    worry_level: int 

@dataclass
class Monkey:
    index: int
    items: list
    operation: str
    divisible: int 
    true: int 
    false: int 
    inspected_items: int 

    def play(self,item): 
        self.items.pop(0)
        self.inspected_items += 1 
        worry_level = self.operation.calculate(item)
        if item.modulo(self.divisible) == 0: 
            return Package(self.true,worry_level)
        else: 
            return Package(self.false,worry_level) 
    
    def get_package(self,worry_level): 
        self.items.append(worry_level)


       
def get_int(string):
    number = ''.join(x for x in string if x.isdigit())
    return int(number)

def get_items(string,divisible):
    _, itmes = string.split(":")
    return [translate_item(int(i),divisible) for i in itmes.split(",")]

def get_operation(string):
    _, operation = string.split("=")
    operation = operation.split(" ")
    return Operation(
        operation[2], 
        operation[3]
    )

def read_monkey(monkey):
    monkey = monkey.split("\n")
    divisible = get_int(monkey[3])
    return Monkey(
        get_int(monkey[0]), 
        get_items(monkey[1],divisible), 
        get_operation(monkey[2]),
        divisible,
        get_int(monkey[4]),
        get_int(monkey[5]),
        0
    )

# A 
file = open(f"{os.getcwd()}/day11/puzzle_test.txt", "r") 
file = file.read()
monkeys = file.split("\n\n")
monkeys = [read_monkey(m) for m in monkeys]

# PLAY 
for i in range(0,20):
    for monkey in monkeys: 
        item_to_process = monkey.items.copy()
        for item in item_to_process:
            package = monkey.play(item)
            monkeys[package.index].get_package(package.worry_level)

active_monkeys = [] 
for monkey in monkeys:
    print(monkey)
    active_monkeys.append(monkey.inspected_items)


print(active_monkeys)
# # print(sorted(active_monkeys)[-2:])

# # print(math.prod(sorted(active_monkeys)[-2:]))