def find_card(cards):
    result = 0
    for card in cards:
        result = result ^ card
    return result
             
n = int(input())
cards = list(map(int, input().split()))
print(find_card(cards))