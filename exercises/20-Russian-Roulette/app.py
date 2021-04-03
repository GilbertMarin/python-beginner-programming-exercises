import random

bullet_position = 3

def spin_chamber():
	chamber_position = random.randint(1,6)
	return chamber_position

#  DON'T CHANGE THE CODE ABOVE
def fire_gun():
	# YOUR CODE HERE
    output = ''
    if spin_chamber() == bullet_position:
        output = 'You are dead!'
    else:
        output = 'Keep playing!'

    return output

print(fire_gun())