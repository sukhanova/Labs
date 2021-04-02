"""Restaurant rating lister."""

"""Read the ratings in from the file, store them in a dictionary and spits out the ratings
 in alphabetical order by restaurant"""
def process_scores():
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

print(process_scores())