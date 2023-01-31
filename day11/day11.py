import os 
import math
from dataclasses import dataclass

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
        old = item 
        self.items.pop(0)
        self.inspected_items += 1 
        worry_level = math.floor(eval(self.operation)/3) 
        if worry_level%self.divisible == 0: 
            return Package(self.true,worry_level)
        else: 
            return Package(self.false,worry_level) 
    
    def get_package(self,worry_level): 
        self.items.append(worry_level)
            
def get_int(string):
    number = ''.join(x for x in string if x.isdigit())
    return int(number)

def get_items(string):
    _, itmes = string.split(":")
    return [int(i) for i in itmes.split(",")]

def get_operation(string):
    _, operation = string.split("=")
    return operation

def read_monkey(monkey):
    monkey = monkey.split("\n")
    return Monkey(
        get_int(monkey[0]), 
        get_items(monkey[1]), 
        get_operation(monkey[2]),
        get_int(monkey[3]),
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
    active_monkeys.append(monkey.inspected_items)

print(active_monkeys)
print(sorted(active_monkeys)[-2:])

print(math.prod(sorted(active_monkeys)[-2:]))