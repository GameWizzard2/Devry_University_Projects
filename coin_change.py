def coin_change(coins, amount_due):
    """
    # setup
    Calculate the minimum number of coins needed to complete the transaction.
    
    Parameters:
    coins (list): A list of coin denominations.
    amount_due (int): The amount due for which we need to determine the number of coins.
    
    Returns:
    list: A list containing the number of coins of each denomination needed to return the amount.
          Each element is a tuple of the form (coin denomination, count of coins needed).
          Example: [(25, 2)] means 2 coins of 25 cents.
    """
    coins.sort(reverse=True)
    coin_count = []
    
    for coin in coins:
        if amount_due == 0:
            break
        count = amount_due // coin  # Number of coins of this denomination.
        amount_due -= count * coin  # Reduce the remaining amount_due.
        coin_count.append((coin, count))
    
    # If amount_due is not 0 after using all coins, it means the change is not possible.
    # FIXME Really, this should produce a logging error.
    if amount_due != 0:
        return "Change not possible with given coin denominations"
    
    return coin_count

# call function and return coin_count list.
coins = [1, 5, 10, 25]
amount_due = 63
coin_count = coin_change(coins, amount_due)
# FIXME should make an if else block to check if coin_count is list or str.

# Print amount of coins needed to return for each denomination.
print(f"The the minimum number of coins needed to complete transiaction for the amount of {amount_due} is:")
for change in coin_count:
    coin_word = "coin" if change[1] == 1 else "coins"
    print(f"{change[1]} {coin_word} of {change[0]} cents is owed.")
        