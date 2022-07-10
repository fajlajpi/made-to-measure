from mtm_classes import Tour, Stop, Block
import mtm_data

# Get the mock data from mtm_data here to use more easily
tours_db = mtm_data.tours_db
stops_db_clock = mtm_data.stops_db_clock
stops_db_intro = mtm_data.stops_db_intro
stops_db_ots = mtm_data.stops_db_ots
blocks_db_clock = mtm_data.blocks_db_clock

# Helper variable(s) for console printouts
dashes = "\n"+30*"-"+"\n"

tours_available = []  # Initialise empty list of available tours to populate from mock data
tour_chosen = None    # Initialise None for the tour chosen

# Populate tours list with mock data
for item in tours_db:
    tours_available.append(
        Tour(item["name"], item["categories"], item["start_lat"], item["start_lon"], item["first_stop"],
             item["description"])
    )

# Print a welcome message
print("Welcome to Made-To-Measure Tours!")
print(dashes)

# Print a list of available tours
print("Our currently available tours:")
for i in range(len(tours_available)):
    print(f"{i+1}) {tours_available[i].name}")
print("\n")

# Get a tour choice from user - commented out and fixed to 1 for now
# choice = int(input("Please pick a tour number: ").strip())
print("Please pick a tour number: 1")
choice = 1
print(dashes)

# User chooses tour 1, which we have mock data for, so populate stops from mock data now
if choice == 1:
    tour_chosen = tours_available[choice-1]
    previous_stop = None
    for item in stops_db_clock:
        if tour_chosen.first_stop is None:  # Are we building the very first stop?
            tour_chosen.first_stop = previous_stop = Stop(item["id"], item["name"], tour_chosen, item["lat"], item["lon"],
                                                          item["categories"], item["description"], item["blocks"],
                                                          item["next_stop"])
        else:
            previous_stop.next_stop = Stop(item["id"], item["name"], tour_chosen, item["lat"], item["lon"],
                                           item["categories"], item["description"], item["blocks"], item["next_stop"])

else:
    # Ask user to pick 1, because we don't have mock data for any other yet
    print("Please pick tour 1 for now. Prototype stuff.")

# Confirm users choice and print a list of stops
print(f"You've picked: {tour_chosen.name}")
print("This tour consists of the following stops:")
stops_list = tour_chosen.get_stops_list()
for stop in stops_list:
    print(f" - {stop.name}")

# Pull all the blocks relevant to the Tour and its Stops, and get their categories into the Tour category set
# In future, this will be done via SQL queries and IDs, for now we work with mock data
# Also for now we are hardcoding the users choice as the Clock tour
for item in blocks_db_clock:
    tour_chosen.categories = tour_chosen.categories.union(item["category"])

print(dashes)

# Ask the user for categories to add
print("Your chosen tour allows for following categories of extra information:")
for cat in tour_chosen.categories:
    print(cat, sep=" ", end=" ")
print("\nCurrently, you have no extra categories chosen.\nTo add them, please write the names to add.")
print("Separate multiple categories by spaces. Leave an empty line to add nothing.")
categories_input = set(input("Categories to add: ").split())

# Error check the input
check_passed = False
while not check_passed:
    if not categories_input.issubset(tour_chosen.categories):
        print("Categories not recognised. Please try again and check for any spelling errors.")
        categories_input = set(input("Categories to add: ").split())
    else:
        check_passed = True

# Overwrite tour categories (originally there were all available categories there) with user's choices
tour_chosen.categories = categories_input

print("You have chosen the following categories: ")
if len(tour_chosen.categories) == 0:
    print("None, just the basic tour.")
else:
    for cat in tour_chosen.categories:
        print(cat, sep=" ", end=" ")
print(f"\n{dashes}")

# We now have a Tour chosen, as well as the extra categories. Time to build out Stops in full.
for stop in stops_list:
    for block in blocks_db_clock:
        if block["parent"] == stop.id:
            if block["primary"]:
                stop.blocks.append(Block(block["name"], block["parent"], block["primary"], block["category"],
                                         block["text"]))
            elif block["category"].issubset(tour_chosen.categories):
                stop.blocks.append(Block(block["name"], block["parent"], block["primary"], block["category"],
                                         block["text"]))


stop_counter = 1
for stop in stops_list:
    print(f"{stop_counter}) {stop.name}")
    print(f"Latitude: {stop.lat}  |  Longitude: {stop.lon}")
    print(f"Guide transcript:")
    for block in stop.blocks:
        print(f"  {block.text}")
    print(dashes)
    stop_counter += 1

print("We hope the tour was to your liking! See you on the next one!")