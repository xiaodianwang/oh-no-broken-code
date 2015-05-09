# I had this great script, but my keyboard broke and I can't indent
# any of my code. Can you indent it for me?

cats = ['Grizabella', 'Rum Tum Tugger', 'Demeter', 'Munkustrap',
'Mistoffelees', 'Macavity', 'Rumpleteazer', 'Mungo Jerry', 'Skimbleshanks']

instruments = ['keyboard', 'cello', 'bass', 'flute', 'pipe', 'piano',
'violin', 'oboe', 'triangle']

def get_cat_and_instrument(position):
	cat = cats[position]
	instrument = instruments[position]
	return "{} plays the {}".format(cat, instrument)

# Print out my cat orchestra one by one
total_cats = len(cats)
position = 0

while True:
	if position >= total_cats:
	    break
	print get_cat_and_instrument(position)
	position += 1

# Could you do the assignment of cats and instruments any other ways?
#Initialize a dictionary of {<cat>: <instrument>}
#Loop through the list of cats
#For each cat, randomly select an instrument index. If that index has
#been selected before, keep re-selecting until you don't have a duplicate index.
#Then add your cat and instrument at your corresponding selected index to the dictionary
#Return the dictionary
from random import randrange

def get_cat_instrument_dict():
	cats_orchestra = {}
	picked_indices = []
	total_instruments = len(instruments)

	for cat in cats:
		rand_instrument =randrange(0, total_instruments)
		while rand_instrument in picked_indices:
			rand_instrument=randrange(0, total_instruments)
		cats_orchestra[cat] = instruments[rand_instrument]
		picked_indices.append(rand_instrument)
	return cats_orchestra

print "\n\nPart 2: Randomly assign an instrument to each cat."
cats_band = get_cat_instrument_dict()
for cat, instrument in cats_band.iteritems():
	print "{c} plays the {i}".format(c=cat, i=instrument)
	
