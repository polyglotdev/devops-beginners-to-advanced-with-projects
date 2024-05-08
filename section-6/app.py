def add(x, y):
    return x + y


result = add(1, 2)
print(result)

# list
my_list = [1, 2, 3]


def print_list(list):
    sum = 0
    for item in list:
        sum += item
    return sum


print(print_list(my_list))

nba_players = {
    'Stephen Curry': 30,
    'Kevin Durant': 35,
    'Lebron James': 23,
    'Kawhi Leonard': 2
}

for player, number in nba_players.items():
    print(f'{player} wears number {number}')
