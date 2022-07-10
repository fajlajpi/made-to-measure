"""
Class definitions for MTM Tours
Defined classes:
Tour ... Higher level object storing essential tour information and tour stops
Stop ... Lower level object, storing information about individual stops
Block ... Atom level object, storing fragments to build a Stop from
"""


class Tour:
    """
    Class for overall tour data as well as individual stops.

    ...

    Attributes
    ----------
    name : str
        name of the tour
    start_lat : float
        starting position - latitude component
    start_lon : float
        starting position - longitude component
    categories : set
        categories chosen by the user for adding additional info to Stops
    first_stop : Stop
        first Stop of the tour (default is None for an un-constructed Tour)
    description : str
        textual description of the tour

    Methods
    -------
    add_stop(stop: Stop)
        adds a stop to the tour itinerary (at the end)
    insert_stop(stop: Stop)
        inserts a stop to the tour itinerary before the given Stop
    remove_stop(stop: Stop)
        removes a given Stop in a Tour
    get_stop(stop: Stop)
        gets a stop from the itinerary
    get_stops_list()
        gets a list of all stops within the tour
    """
    def __init__(self, name, categories: set, start_lat=0.0, start_lon=0.0, first_stop=None, description=""):
        self.name = name
        self.start_lat = start_lat
        self.start_lon = start_lon
        self.categories = categories
        self.first_stop = first_stop
        self.description = description

    def add_stop(self, stop):
        pass

    def insert_stop(self, stop):
        pass

    def remove_stop(self, stop):
        pass

    def get_stop(self, stop):
        pass

    def get_stops_list(self) -> list:
        if self.first_stop is None:  # If first_stop is None, return None
            return None
        else:
            output = [self.first_stop]
            next_stop = self.first_stop.next_stop
            while next_stop is not None:
                output.append(next_stop)
                next_stop = next_stop.next_stop
            return output


class Stop:
    """
    Class for individual stops within a tour. Stops cannot exist outside a Tour object

    ...

    Attributes
    ----------
    name : str
        name of the stop
    parent: Tour
        the Tour object this Stop belongs into
    next_stop : Stop
        next Stop in the itinerary
    lat : float
        GPS coordinates for the stop - latitude component
    lon : float
        GPS coordinates for the stop - longitude component
    categories : Set
        categories the stop includes
    description : str
        description of the stop
    blocks : List
        list of block objects that form the stop itself

    Methods
    -------

    """
    def __init__(self, id, name, parent, lat=0.0, lon=0.0, categories=None, description=None, blocks=None, next_stop=None):
        self.id = id
        self.name = name
        self.parent = parent
        self.lat = lat
        self.lon = lon
        self.categories = categories
        self.description = description
        self.blocks = blocks
        self.next_stop = next_stop
        pass

class Block:
    """
    Class for block fragments that are used to construct a stop based on parameters specified within Tour

    ...

    Attributes
    ----------
    name : str
        name of the block
    parent : Stop
        the Stop this Block can be a part of
    primary : Boolean
        whether this Block is the primary block for a Stop
    category : Set
        category or categories the Block belongs to (i.e. keywords)
    text : str
        textual content of the block

    Methods
    -------

    """
    def __init__(self, name, parent, primary=False, category=None, text=None):
        self.name = name
        self.parent = parent
        self.primary = primary
        self.category = category
        self.text = text
