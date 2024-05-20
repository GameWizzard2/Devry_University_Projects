# rewrote as one-liner ☺
coin_change = lambda amount_due, coins=[25, 10, 5, 1]: [[x, count:=amount_due // x, amount_due:= amount_due-count*x]  for x in coins]


for change in (coin_count:=coin_change(amount_due=63)):
    print(f"{change[1]} coin{"" if change[1] == 1 else "s"} of {change[0]} cents is owed.")
