# I want to print out my favorite ice cream flavors.

all_flavors = ['chocolate', 'mint', 'strawberry', 'caramel', 'pecan',
               'cookie dough', 'vanilla', 'lemon']
my_faves    = ['mint', 'caramel']


for item in all_flavors:
    if item in my_faves:
        print "I like {}".format(item)

