############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    # flavor = "yum"

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.extend(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code

def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    muskmelon = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    muskmelon.add_pairing(['mint'])
    all_melon_types.append(muskmelon)

    casaba = MelonType('cas', 2003, 'orange', False, False, 'Casaba')
    casaba.add_pairing(['strawberries', 'mint'])
    all_melon_types.append(casaba)
    
    crenshaw = MelonType('cren', 1996, 'green', False, False, 'Crenshaw')
    crenshaw.add_pairing(['proscuitto'])
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType('yw', 2013, 'yellow', False, True, 'Yellow Watermelon')
    yellow_watermelon.add_pairing(['ice cream'])
    all_melon_types.append(yellow_watermelon)


    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print "\n{} pairs with".format(melon.name)
        for pairing in melon.pairings:
            print "-{}".format(pairing)


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    reporting_code = {}

    for melon in melon_types:
        reporting_code[melon.code] = melon

    return reporting_code

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""
    def __init__(self, code, shape_rating, color_rating, field, harvester):
        self.code = code
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester = harvester

    def is_sellable(self):
        """Returns if sellable or not."""

        return self.shape_rating > 5 and self.color_rating > 5 and self.field != 3


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    harvest =[]

    melon_1 = Melon(melon_types['yw'], 8, 7, 2, 'Sheila')
    harvest.append(melon_1)

    melon_2 = Melon(melon_types['yw'], 3, 4, 2, 'Sheila')
    harvest.append(melon_2)

    melon_3 = Melon(melon_types['yw'], 9, 8, 3, 'Sheila')
    harvest.append(melon_3)
    
    return harvest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 


melons = make_melon_types()
melons_by_id = make_melon_type_lookup(melons)
print make_melons(melons_by_id)
