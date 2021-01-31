# coding: utf-

n, m = [int(m) for m in input().split()]
# n (バインダーのポケットの数) 
# m (名刺の番号)
# print(n, m)

for p in range(1, m + 1):
    first_card_page = 1 + 2 * n * (p - 1)
    if first_card_page - n <= m <= first_card_page + n - 1:
        if m >= first_card_page:
            card = first_card_page
            for i in range(2 * n - 1, 0, -2):
                if card == m:
                    print(m + i)
                    break
                card += 1
        else:
            card = first_card_page
            for i in range(-2 * n + 1, 0, 2):
                card -= 1
                if card == m:
                    print(m + i) 
                    break
        break
