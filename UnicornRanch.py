
class UnicornRanch(object):
    def __init__(self):
        self.ranch_sqft = 326700
        self.barn_sqft = 1200

        sefl.watering_pond = {
            'depth':30,
            'shape':'circle',
            'radi': 681
        }

        self.prop_tax_rates = {
            'water_surface_acerage': '0.74',
            'structure': '1.33202',
            'grassland': '.003 per .004 acre'
        }

        # Need to write a function that returns the following
        # - in a dictionary.
        #   - estimated property tax bill for this year.
        #   - estimated property tax bill with 1.2% appreciation, next 5 years.

        # Submissions:
        #    - Submit as a PR, to this repo. Your desination branch must be your first/last initials.

        # Note:
        # - further exercises will build on the code you write here.
