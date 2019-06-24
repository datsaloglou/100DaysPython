
content = ["Wayne is the toughest guy in Letterkenny.", list(range(0,101,10)), ("Wayne", "Dan", "Katy", "Daryl"), 10.4]

for i in range(0, len(content)):
    # if the object is immutable, print the type and advance to the next step. 
    if type(content[i]) is tuple:
        print ("{} is a {}".format(content[i], type(content[i])))
    # if the object is mutable and a string, add "Allegedly" to the end.   
    elif type(content[i]) is str:
        content[i] += " Allegedly."
        print(content[i])
    # if the object is mutable and a number, take 10 % off (for an int) and overwrite the value in the existing position.
    elif type(content[i]) is list:
        new_list = content[i]
        for j in range(0, len(new_list)):
            if type(new_list[j]) is int:
                new_list[j] -= new_list[j] * .1
                # print the new value 
            # to 20 % off (for a float) and overwrite the value in the existing position.
            elif type(new_list[j]) is float:
                new_list[j] -= new_list[j] * .2
                # print the new value 
        content[i] = new_list
        print(new_list)
    elif type(content[i]) is int:
        content[i] -= content[i] * .1
        # print the new value 
        print(content[i])
    # to 20 % off (for a float) and overwrite the value in the existing position.
    elif type(content[i]) is float:
        content[i] -= content[i] * .2
        # print the new value 
        print(content[i])
    # If an object is not a string, number, or tuple end the program immediately 
    # while displaying the object and the type for review.
    else:
        print("{} is a {}, and nothing was done about it.".format(content[i], type(content[i])))
        break

 


