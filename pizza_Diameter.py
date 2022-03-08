#!/usr/bin/env python3

# Created by Ethan Prieur
# Created on March 2022
# This is A File for Calculating the Cost of pizza

import constants


def main():
    # This function calculates the cost of pizza

    # Input
    diameter = float(input("Enter Diameter of Pizza in mm: "))

    # Process
    price_Of_Pizza = (
        constants.LABOR + constants.RENT + (constants.COST_PER_INCH * diameter)
    )

    total = price_Of_Pizza * constants.HST

    # Output
    print("")
    print("The cost for a {0} inch pizza is: ${1:,.2f}".format(diameter, total))

    print("\nDone.")


if __name__ == "__main__":
    main()
