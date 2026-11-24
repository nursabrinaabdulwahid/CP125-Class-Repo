# Lab 01 Exercise 1: Road Trip Budgeter

def is_budget_sufficient(one_way_km, budget):
    price = ((1/10)*(one_way_km*2))+(2.00)
    sufficient = price < budget