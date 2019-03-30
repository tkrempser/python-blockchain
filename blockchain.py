# Initializing the blockchain list
blockchain = []


def get_last_block():
    """Returns the last blockchain value.
    
    Returns:
        The last blockchain value or None if the blockchain is empty.
    """
    if blockchain:
        return blockchain[-1]
    return None


def add_transaction(transaction_amount, last_transaction=[1]):
    """Append a new transaction to the blockchain.
    
    Args:
        transaction_amount (int): The amount value to be appended.
        last_transaction (int): The last transaction on the blockchain (default [1]).
    """
    if not last_transaction:
        last_transaction = [1]

    blockchain.append([last_transaction, transaction_amount])


def get_transaction_amount():
    """Get the user trasaction amount input and returns it as float.

    Returns:
        float: The user amount.
    """
    return float(input('Type the amount please: '))


def print_blockchain_blocks():
    """Output the blockchain blocks"""
    print('-' * 30)
    print('Current blockchain: ' + str(blockchain))
    for index, block in enumerate(blockchain):
        print('Block ' + str(index) + ': ' + str(block))


def show_options():
    """Show available options"""
    print('-' * 30)
    print('Select an option')
    print('1: Add a new transaction')
    print('2: Output blockchain')
    print('q: Quit')


def get_choice():
    return input('Your choice: ')


while True:
    show_options()
    choice = get_choice()

    if choice == '1':
        add_transaction(get_transaction_amount(), get_last_block())
    elif choice == '2':
        print_blockchain_blocks()
    elif choice == 'q':
        break
    else:
        print('Invalid option.')

print('Done!')
