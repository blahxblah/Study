from collections import Counter

def find_single_card(n, cards):
    count = Counter(cards)
    for card, frequency in count.items():
        if frequency == 1:
            return card
    return None

# N을 입력받는다
N = int(input().strip())
# N개의 카드에 적힌 숫자를 입력받는다
cards = list(map(int, input().strip().split()))

print(find_single_card(N, cards))