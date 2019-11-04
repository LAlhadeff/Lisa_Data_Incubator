import re
f = open( 'temp_datalab_records_social_facebook.csv', 'r' )
lines = []
liked = []
talked = []
for line in f:
    cells = line.split( "," ) ## Split into cells
  #  print(cells)
    likes = (cells[6])
    #print(likes)
    liked.append(likes)
    talks = cells[7]
    # talks = cells[7]
    talked.append(talks)
f.close() # Data stored locally so close file

del liked[0]
del talked[0]

with open("likes.txt", 'w') as f:
	for item in liked:
		f.write("%s\n" % item)

with open("talked_about.txt", 'w') as f:
	for item in talked:
		f.write("%s\n" % item)