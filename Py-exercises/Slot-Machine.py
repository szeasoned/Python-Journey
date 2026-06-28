import random

def show_symbols():
    symbols = ['🍒', '🍋','🍇','🔔', '⭐']
    return [random.choice(symbols) for _ in range(3)]

def calc_bet(bet, row):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍋':
            return bet * 4
        if row[0] == '🍇':
            return bet * 5
        if row[0] == '🔔':
            return bet * 10
        if row[0] == '⭐':
            return bet * 25
    return 0

def show_balance(balance):
    print("—" * 28)
    print(f"Your current balance is ${balance}")

def main():
    balance = 100
    print("—" * 28)
    print("    PYTHON SLOT MACHINE")
    show_balance(balance)

    while True:
        bet = input("Enter bet: ")
        if not bet.isdigit():
            print("Enter a valid bet!")
            continue

        bet = int(bet)
        if balance < bet:
            print("Insufficient balance!")
            continue

        print("Spinning....")

        balance -= bet
        row = show_symbols()
        print("—" * 28)
        print(" | ".join(row))

        payout = calc_bet(bet, row)
        balance += payout

        if payout > 0:
            print(f"You won ${payout}. Your new balance is {balance}")
        else:
            print(f"You lost! Your current balance is {balance}")
        print("—" * 28)

        play_again = input("Do you want to play again? (Y/N) ").upper()
        if play_again != 'Y':
            break
        else:
            continue

    print("—" * 28)
    print(f"Game ended! Your balance is {balance}")
    print("—" * 28)

if __name__ == '__main__':
    main()