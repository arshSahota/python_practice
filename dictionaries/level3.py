prices = {
    "apple": 2,
    "banana": 3,
    "orange": 2
}

mango_price = prices.get("mango", 0)

print(mango_price)

#problem 2
items = ["apple", "banana", "apple", "orange", "banana", "apple"]

fruit_count = {}

for fruit in items:
    fruit_count[fruit] = fruit_count.get(fruit, 0)+1 

print(fruit_count)

#problem 3

scores = {
    "John": 75,
    "Emma": 90,
    "Liam": 60
}

arshdeep_score = scores.get("Arshdeep", 50)

#problem #4

# if the word does not exist it will get an error, because we did not 
# insert a default value
# it will give an error KeyError

# challenge Problem


orders = ["tea", "coffee", "tea", "juice", "coffee", "tea"]

beverages = {}

for order in orders:
    beverages[order] = beverages.get(order, 0)+1

freq_drink = 0
for drink in beverages:
    if freq_drink < beverages[drink]:
        freq_drink = beverages[drink]

print(freq_drink)