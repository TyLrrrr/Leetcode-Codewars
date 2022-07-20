#codewars Challenge: mplement the function which takes an array containing the names of people that like an item. 
# It must return the display text as shown in the examples:
#[]                                -->  "no one likes this"
#["Peter"]                         -->  "Peter likes this"
#["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
#["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
#["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
# Note: For 4 or more names, the number in "and 2 others" simply increases.

def likes(names):
    x = len(names)
    output = ""
    if x > 3:
        y = x-2
        output = names[0] + ", " + names[1] + " and " + str(y) + " others like this"
    elif x == 3:
        output = names[0] + ", " + names[1] + " and " + names[2] + " like this"
    elif x == 2:
        output = names[0] + " and " + names[1] + " like this"
    elif x == 1:
        output = names[0] + " likes this"
    else:
        output = "no one likes this"
    return output
