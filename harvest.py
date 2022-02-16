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
    melon_dict = {}
    
    #for loop through melon_types list and find the code:
    for melon in melon_types:
        if melon not in melon_dict:
            melon_dict[melon.code] = melon
        # assign the code as dict_keys
        #assin the rest of melon info as values
    return melon_dict

make_melon_type_lookup(melon_types)

############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest


#name, code, first_harvest, color, is_seedless, is_bestseller=False

# musk = MelonType(
#     "musk",
#     "Muskmelon",
#     1998,
#     "green",
#     True,
#     True
# )
# musk.add_pairing("mint")