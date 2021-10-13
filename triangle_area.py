#!/usr/bin/env python3

# Created by: Daria Bernice Calitis
# Created on: Oct 2021
# This program calculates the area of the triangle


def calculate_area(base_length, height):
    # this function calculates the area of the triangle
    # process
    area_of_triangle = (base_length * height) / 2

    # output
    print("\nThe area of the triangle is {0} cm²".format(area_of_triangle))


def main():
    # this function is the main function
    # input
    length_input = input("Enter the base length of a triangle (cm): ")
    height_input = input("Enter the height of a triangle (cm): ")

    try:
        # call function
        calculate_area(float(length_input), float(height_input))
    except (Exception):
        print("\nInvalid Input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
