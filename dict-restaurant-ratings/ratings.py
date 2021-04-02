"""Restaurant rating lister."""

def process_scores():
    """Read the ratings in from the file, store them in a dictionary"""
    #  def restaurant_rating(filename):
    file = open('scores.txt')  

    restaurant_scores = {}

    for line in file:
        line = line.strip()
        restaurant, score = line.split(":")
        
        #prints each line from file in format restaurant: score
        #print(line)
        restaurant_scores[restaurant] = int(score)
    
    # print(restaurant_scores)
    return restaurant_scores


def add_new_restaurant(scores):
    """Add new restaurant and rating"""
    print("Do you want to add new restaurant and rating? ")
    new_restaurant = input("Restaurant name: ")
    new_rating = int(input("Give restaurant a rating: "))

    scores[new_restaurant] = new_rating
    # print(new_restaurant, new_rating)
    print()

def sort_scores(scores):
    """Print sorted restaurants and its scores"""
    for restaurant, rating in sorted(scores.items()):
        print(f"{restaurant} is rated at {rating}")


# read existing scores from file and store in scores variable
scores = process_scores()

# user can add a new restaurant and new rating
add_new_restaurant(scores)

#print restaurants in alphabetical order and its ratings
sort_scores(scores)