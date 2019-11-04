from collections import Counter # We're going to use collections to calculate the number of repeated paths
d = 4 # Number of dimensions
m = 10 # Path length
n = 10 # Grid intersections

## Counting variables
#counter = 0 # counter for path lengths
next_position = []
curr_position = [0]
curr_position[0] = [0]*d
#print(curr_position)

for_value = int(m/2) ## Efficiency
#print(for_value)

"""
find all the positions you can be in, starting at a given position "curr_position", taking as inputes dimensions (d), path length (m) and grif intersections (n).
"""
def number_paths(curr_position, d, m, n): 
	#print(curr_position)
	next_position = []
	for step_no in range(0, (for_value)):
		for position in curr_position:
		#print(curr_position)
			for c in range(0, d):
				step = [0 for _ in range (d)]
				step[c] = 1
				#print("worked")

				if position[c] == 0: # if we're at a zero gridline
					next_position.append([position[i] + step[i] for i in range(len(position))])
					#print(next_position)
					# append all possible next positions in this dimension 
					#print("Stillworked")
				elif position[c] == n-1: # if we hit the end
					next_position.append([position[i] - step[i] for i in range(len(position))])
					# can only move in a negative direction i.e. "add the negative" to move back
					#print(f"2", next_position)
				else: # at any internal grid intersection
					# append both possible options
					next_position.append([position[i] + step[i] for i in range(len(position))])
					next_position.append([position[i] - step[i] for i in range(len(position))])
					#print("LoL")
		curr_position = next_position.copy() #  make a copy of next_position 
											 #  this is new current_position
		next_position = []	# clear next_position for next run
	return(curr_position)	# from this function we obtain all the possible current positions
	
current_pos = number_paths(curr_position, d, m, n) # call function

## Using tuples to count number of repeats: ##
"""
tuple of tubples is a tuble containing both coordinates, and number of instances that this coordinate occurs.
"""
tuple_of_tuples = tuple(tuple(x) for x in current_pos)
count=Counter(tuple_of_tuples) # count number of instences

keys = (count.keys()) # get the keys (i.e. coordinates)
values = (count.values()) # get the values (i.e. no. of instances)
key_values = [ v for v in keys ] # pull keys into list
list_of_keys = [list(elem) for elem in key_values] # pull values into a list
list_of_values = [ w for w in values ] # pull values into a list

selector = 0
total_paths = 0
for i in list_of_keys:
	curr_position = [0]
	curr_position[0] = i
	"""
	The number of occurrances is used as a multiplyer: from this point, there are only n possible new path options so we only explore each instance of the point onece.
	"""
	multiplyer = list_of_values[selector]
	# call function for each point in the list:
	current_pos = number_paths(curr_position, d, m, n) 
	# multiply result by number of occurrences:
	total_paths += len(current_pos)*multiplyer 
	selector +=1 # Selector is being used to iterate through the list
print(f"The number of paths is", total_paths)