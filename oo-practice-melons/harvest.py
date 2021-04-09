############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []
        self.name = name
        self.color = color
        self.first_harvest = first_harvest
        self.code = code 
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

    musk = MelonType("musk", 1998, "green", True, True, "Muskmelon")
    casaba = MelonType("cas", 2003, "orange", True, False, "Casaba")
    crenshaw = MelonType("cren", 1996, "green", True, True, "Crenshaw")
    yellow_watermelon = MelonType("yw", 2013, "yellow", True, True, "Yellow Watermelon")
    
    all_melon_types = [ musk, casaba, crenshaw, yellow_watermelon ]
   
    musk.add_pairing("mint")
    casaba.add_pairing("mint")
    casaba.add_pairing("strawberries")
    crenshaw.add_pairing("proscuitto")
    yellow_watermelon.add_pairing("ice cream")
    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for pairing in melon.pairings:
            print(f" -{pairing}")

def make_melon_type_lookup(melon_types): # melon_types is a list of Melon instances
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest
    melon_reporting_codes = {}
    for melon in melon_types:
        melon_reporting_codes[melon.code] = melon
    
    return melon_reporting_codes

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



