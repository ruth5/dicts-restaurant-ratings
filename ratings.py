"""Restaurant rating lister."""

import random


def add_restaurants_from_file(ratings, filename = 'scores.txt'):
    file_object = open(filename, "r")
    for line in file_object:
        line = line.rstrip()
        words = line.split(":")
        parsed_ratings = add_restaurant(ratings, words[0], words[1])
    return ratings

def show_all_sorted_ratings(ratings, filename = 'scores.txt'):
    sorted_restaurants = sorted(ratings)
    for restaurant in sorted_restaurants:
        print(f'{restaurant} is rated at {ratings[restaurant]}.')
    
def add_restaurant(ratings, name, rating):
    valid_ratings = (1, 2, 3, 4, 5)
    if int(rating) in valid_ratings:
        ratings[name] = rating
    else:
        print(f"Invalid rating for {name}. Entry not added.")
    return ratings

parsed_ratings = {}
parsed_ratings = add_restaurants_from_file(parsed_ratings)
while True:
    print("\nEnter 's' to see restaurant ratings.")
    print("Enter 'n' to add a new restaurant.")
    print("Enter 'r' to update a random restaurant's rating.")
    print("Enter 'c' to update a chosen restaurant's rating.")
    print("Enter 'q' to quit.")
    option = input("> ").lower()
    if option == "s":
        show_all_sorted_ratings(parsed_ratings)
    elif option == "n":
        print("Enter a restaurant name.")
        restaurant_name = input("> ")
        print("Enter a restaurant rating.")
        restaurant_rating = input("> ")
        parsed_ratings = add_restaurant(parsed_ratings, restaurant_name, restaurant_rating)
    elif option == "r":
        restaurants = list(parsed_ratings.keys())
        random_restaurant = random.choice(restaurants)
        print(f"Enter a restaurant rating for {random_restaurant}.")
        restaurant_rating = input("> ")
        parsed_ratings = add_restaurant(parsed_ratings, random_restaurant, restaurant_rating)
    elif option == "c":
        print("Enter a restaurant name.")
        restaurant_name = input("> ")
        print(f"Enter a restaurant rating for {restaurant_name}.")
        restaurant_rating = input("> ")
        if parsed_ratings.get(restaurant_name) is None:
            print("Restaurant does not exist. Adding rating anyways.")
        parsed_ratings = add_restaurant(parsed_ratings, restaurant_name, restaurant_rating)
    elif option == "q":
        break
    else:
        print("Invalid input. Please try again.")