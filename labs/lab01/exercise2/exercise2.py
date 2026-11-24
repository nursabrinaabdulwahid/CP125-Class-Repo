# Lab 01 Exercise 2: Camping Logistics
import math
def calculate_tent_cost(participants, tent_capacity, tent_price):
    tent_needed = math.ceil(participants/tent_capacity)
    return(tent_needed*tent_price)