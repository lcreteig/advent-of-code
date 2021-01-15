#!/usr/bin/env python3

def calc_fuel(mass):
    return (mass // 3) - 2

def calc_fuel_tot(mass):
    fuel_list = []
    while calc_fuel(mass) > 0:
        mass = calc_fuel(mass)
        fuel_list.append(mass)
    return sum(fuel_list)

if __name__ == '__main__':
    with open('input_day01') as f:
        masses = [int(i) for i in f]
    
    print('Part 1:', sum([calc_fuel(m) for m in masses]))
    print('Part 2:', sum([calc_fuel_tot(m) for m in masses]))