#!/usr/bin/env python3

# Created By: Kestrel Bryce
# Date: Sep. 29, 2022
# This program calculates the
# tax and total of a subtotal


def main():
    # input
    print("This program calculates the")
    print("tax and total of a subtotal.")
    print("")
    subtotal = int(input("Enter the subtotal: $"))

    # process
    # calculating tax
    tax = subtotal * 0.05

    # calculating total
    total = tax + subtotal

    # output
    print("")
    print("Your tax = ${:,.2f}".format(tax))
    print("Your total is = ${:,.2f}".format(total))


if __name__ == "__main__":
    main()
