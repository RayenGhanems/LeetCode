# itialization (__init__ method):
  1. Three data structures are initialized: cuisine_to_heap (defaultdict of heaps for each cuisine), food_to_cuisine (mapping foods to cuisines), and food_to_rating (mapping foods to their ratings).
  2. The provided food names, cuisines, and ratings are used to populate these data structures.
# Change Rating (changeRating method):
  1. Updates the rating of a given food.
  2. Retrieves the cuisine of the food, then pushes the updated rating and food onto the corresponding cuisine's heap.
  3. Updates the rating in the food_to_rating dictionary.
# Highest Rated (highestRated method):
  1.Retrieves the highest-rated food for a specified cuisine in lexicographical order.
  2. Iterates through the heap of the specified cuisine, considering the lexicographically smallest food with the highest rating.
  3. Skips outdated data by comparing the stored rating with the rating on the heap.
Returns the name of the highest-rated food in the specified cuisine.​
