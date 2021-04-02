"""Restaurant rating lister."""

"""Read the ratings in from the file, store them in a dictionary and spits out the ratings
 in alphabetical order by restaurant"""

#  def restaurant_rating(filename):
file = open('scores.txt')  

restaurant_scores = {}

for line in file:
    line = line.strip()
    restaurant, score = line.split(":")
    print(line)
