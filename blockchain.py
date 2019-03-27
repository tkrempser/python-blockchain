# Initializing the blockchain list
blockchain = []


def add_transaction(transaction_amount, last_transaction=[1]):
    """Append a new transaction to the blockchain.
    
    Args:
        transaction_amount (int): The amount value to be appended.
        last_transaction (int): The last transaction on the blockchain (default [1]).
    """
    blockchain.append([last_transaction, transaction_amount])


def get_input():
    """Get the user input and returns it as float.

    Returns:
        float: The user amount.
    """
    return float(input('Type the amount please: '))


while True:
    # Get the first transaction
    add_transaction(get_input())

    # Output the blockchain
    for block in blockchain:
        print(block)

print('Done!')
