############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, name, first_harvest, color, is_seedless, is_bestseller=False
    ):
        """Initialize a melon."""

        self.pairings = []
        self.name = name
        self.code  = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)
   

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType("musk", "Muskmelon",1998, "green", True, True)
    musk.add_pairing("mint")
    all_melon_types.append(musk)

    casaba = MelonType("cas", "Casaba", 2003, "orange", False, False)
    casaba.add_pairing("strawberries")
    casaba.add_pairing("mint")
    all_melon_types.append(casaba)
    

    yellow_watermelon = MelonType('yw', 'Yellow Watermelon', 2013, 'yellow', True, True )
    yellow_watermelon.add_pairing('ice cream')
    all_melon_types.append(yellow_watermelon)
    
    crenshaw = MelonType("cren", "Crenshaw", 1996, "green", True, False)
    crenshaw.add_pairing("prosciutto")
    all_melon_types.append(crenshaw)

    return all_melon_types

melon_types = make_melon_types()

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    # musk, casaba, yw, and crenshaw

    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for pair in melon.pairings:
            print(f"- {pair}")



def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melons_by_id = {}
    
    #for loop through melon_types list and find the code:
    for melon in melon_types:
        if melon not in melons_by_id:
            melons_by_id[melon.code] = melon
        # assign the code as dict_keys
        #assin the rest of melon info as values
    return melons_by_id




############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(
        self, melon_type, shape_rating, color_rating, harvest_field, harvested_by
        ):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvest_field = harvest_field
        self.harvested_by = harvested_by

    def is_sellable(self):
        # should be boolean
        if self.shape_rating > 5 and self.color_rating > 5 and self.harvest_field != 3:
            return True



def make_melons(melon_types):
    """Returns a list of Melon objects."""
    melons_by_id = make_melon_type_lookup(melon_types)

    melons = []

    melon1 = Melon(melons_by_id["yw"], 8, 7, 2, "Sheila")
    melon2 = Melon(melons_by_id["yw"], 3, 4, 2, "Sheila")
    melon3 = Melon(melons_by_id["yw"], 9, 8, 3, "Sheila")
    melon4 = Melon(melons_by_id["cas"], 10, 6, 35, "Sheila")
    melon5 = Melon(melons_by_id["cren"], 8, 9, 35, "Michael")
    melon6 = Melon(melons_by_id["cren"], 8, 2, 35, "Michael")
    melon7 = Melon(melons_by_id["cren"], 2, 3, 4, "Michael")
    melon8 = Melon(melons_by_id["musk"], 6, 7, 4, "Michael")
    melon9 = Melon(melons_by_id["yw"], 7, 10, 3, "Sheila")

    melons.extend([melon1, melon2, melon3, melon4, melon5, melon6, melon7, melon8, melon9])

    return melons

melons = make_melons(melon_types)

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        harvester = f"Harvested by {melon.harvested_by}"
        field = f"Field #{melon.harvest_field}"
        status = "CAN BE SOLD" if melon.is_sellable() else "NOT SELLABLE"
        print(f"{harvester} from {field} {status}")
