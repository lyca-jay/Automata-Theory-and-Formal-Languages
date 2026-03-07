from itertools import combinations

def a_priori(transactions, min_support):

    items = set()
    for t in transactions:
        for item in t:
            items.add(item)

    def support_count(itemset):
        count = 0
        for t in transactions:
            if set(itemset).issubset(t):
                count +=1
        return count
    
    for i in range(1,3):
        for combo in combinations(items, i):
            support = support_count(combo)
            if support >= min_support:
                print(combo, "Support:", support)

print("\nExample 1: Grocery Transactions")

transactions1 = [
    ['bread','milk'],
    ['bread','diaper','beer'],
    ['milk','diaper','beer'],
    ['bread','milk','diaper']
]

a_priori(transactions1,2)


print("\nExample 2: Online Store")

transactions2 = [
    ['laptop','mouse'],
    ['laptop','keyboard'],
    ['laptop','mouse','keyboard'],
    ['mouse','keyboard']
]

a_priori(transactions2,2)