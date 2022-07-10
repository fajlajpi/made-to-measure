"""
Temporary data to construct tours from for the purpose of the prototype
"""

tours_db = [
    {
        "name": "Astronomical Clock in 15 minutes",
        "categories": set(),
        "start_lat": 50.0869463,
        "start_lon": 14.4207657,
        "first_stop": None,
        "description": "Two stops to describe the Astronomical Clock, its history and meaning."
    },
    {
        "name": "Introduction in Old Town Square",
        "categories": set(),
        "start_lat": 50.0879079,
        "start_lon": 14.4205973,
        "first_stop": None,
        "description": "Starting from Cartier, across to St. Nicholas, and off to the centre"
    },
    {
        "name": "Old Town Square Overview",
        "categories": set(),
        "start_lat": 50.0870095,
        "start_lon": 14.4212799,
        "first_stop": None,
        "description": "Three stops, start at Železná, to the centre and to Pařížská"
    }
]

stops_db_clock = [
    {
        "id": "clock",
        "name": "Astronomical Clock",
        "parent": None,
        "lat": 50.0869463,
        "lon": 14.4207657,
        "categories": None,
        "description": "",
        "blocks": [],
        "next_stop": None,
    },
    {
        "id": "clock_far",
        "name": "Clock from afar",
        "parent": None,
        "lat": 50.0872183,
        "lon": 14.4214309,
        "categories": None,
        "description": "",
        "blocks": [],
        "next_stop": None,
    }
]

stops_db_intro = [
    {
        "name": "Corner of OTS and Pařížská",
        "parent": None,
        "lat": 50.0879079,
        "lon": 14.4205973,
        "categories": None,
        "description": "",
        "blocks": None,
        "next_stop": None,
    },
    {
        "name": "",
        "parent": None,
        "lat": 50.0877371,
        "lon": 14.4200019,
        "categories": None,
        "description": "",
        "blocks": None,
        "next_stop": None,
    },
    {
        "name": "",
        "parent": None,
        "lat": 50.0876122,
        "lon": 14.4207866,
        "categories": None,
        "description": "",
        "blocks": None,
        "next_stop": None,
    }
]

stops_db_ots = [
    {
        "name": "",
        "parent": None,
        "lat": 50.0870095,
        "lon": 14.4212799,
        "categories": None,
        "description": "",
        "blocks": None,
        "next_stop": None,
    },
    {
        "name": "",
        "parent": None,
        "lat": 50.0875283,
        "lon": 14.4211055,
        "categories": None,
        "description": "",
        "blocks": None,
        "next_stop": None,
    },
    {
        "name": "",
        "parent": None,
        "lat": 50.0877555,
        "lon": 14.4206462,
        "categories": None,
        "description": "",
        "blocks": None,
        "next_stop": None,
    }
]

# name, parent, primary=False, category=None, text=None
blocks_db_clock = [
    {
        "name": "clock",
        "parent": "clock",
        "primary": True,
        "category": set(),
        "text": "This is the astronomical clock. It's very old and pretty."
    },
    {
        "name": "clock_extra_art",
        "parent": "clock",
        "primary": False,
        "category": {"art"},
        "text": "The lower dial was painted originally by Josef Mánes."
    },
    {
        "name": "clock_extra_food",
        "parent": "clock",
        "primary": False,
        "category": {"food"},
        "text": "There's a Starbucks on the corner behind us."
    },
    {
        "name": "clock_far",
        "parent": "clock_far",
        "primary": True,
        "category": set(),
        "text": "This is the clock from afar. It's still very old and pretty."
    },
    {
        "name": "clock_far_food",
        "parent": "clock_far",
        "primary": False,
        "category": {"food"},
        "text": "There's more restaurants there, but they're all overpriced here."
    },
    {
        "name": "clock_far_music",
        "parent": "clock_far",
        "primary": False,
        "category": {"music"},
        "text": "There used to be a trumpet player on this tower playing a piece every hour."
    }
]
