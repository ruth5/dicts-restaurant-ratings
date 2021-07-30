"""Restaurant rating lister."""



# put your code here
def alphabetize_ratings(filename = 'scores.txt'):
    parsed_ratings = {}
    file_object = open(filename, "r")
    for line in file_object:
        line = line.rstrip()
        words = line.split(":")
        parsed_ratings[words[0]] = words[1]

    sorted_restaurants = sorted(parsed_ratings)
    for restaurant in sorted_restaurants:
        print(f'{restaurant} is rated at {parsed_ratings[restaurant]}.')
