# This file has a few mistakes and some things I forgot to put in.
# When I run it I don't get anything... can you fix it so I
# get asked for my vacation spot, and get a recommendation?
# Hint:
# Start at the bottom and work upwards.


vacation_spots = ['Tahoe', 'Hawaii', 'New York', 'Mexico']

seasons = ['spring', 'summer', 'fall', 'winter']

weather_patterns = {
    'spring': 'rain',
    'summer': 'sun',
    'fall': 'wind',
    'winter': 'snow'
}

activities = {
    'rain': 'visiting museums',
    'wind': 'kiteboarding',
    'sun': 'sunbathing',
    'snow': 'skiing'
}


def best_vacation_spot(weather_type):
    # Look at the weather type and return the vacation spot that
    # is the best for that weather.
    # You can use this mapping:
    # snow = Tahoe
    # wind = Hawaii
    # rain = New York
    # sun = Mexico
    spots_for_weather = {
        'snow': 'Tahoe',
        'wind': 'Hawaii',
        'rain': 'New York',
        'sun': 'Mexico'
    }
    return spots_for_weather[weather_type]


def vacation_activity(weather_type):
    # Look up the vacation activity from activities
    # and return just the activity itself
    return activities[weather_type]


def get_my_vacation():

    season = raw_input("What season do you want to travel? ").lower()

    # check if season is in the seasons list
    if not season in seasons:
        print "Sorry, that isn't a season. I can't help you."
        exit()

    # look up the weather type for that season
    weather_type = weather_patterns[season]

    # get the best vacation spot for that type
    spot = best_vacation_spot(weather_type)

    # get the best vacation activity for that type
    activity = vacation_activity(weather_type)

    print "You should travel to {}, where you can spend your time {}!".format(spot, activity)


def main():
    print "Welcome to the Vacation-o-Matic!"
    get_my_vacation()


if __name__=="__main__":
    main()