import re


class UnicornRanch(object):
    def __init__(self):
        self.ranch_sqft = 326700
        self.barn_sqft = 1200

        self.watering_pond = {
            'gallons':'458268'
        }

        self.prop_tax_rates = {
            'water_acre_foot': '0.74',
            'structure': '1.33202/sqft',
            'grassland': '.003 per .004 acre'
        }

        self.GALLONS_PER_ACRE_FOOT = 325851
        self.PROPERTY_VALUE = 1200000
        self.SQUARE_FEET_PER_ACRE = 43560

    def get_taxes(self) -> dict:
        """
        """

        barn_tax = self.get_barn_tax(self.barn_sqft)
        print(barn_tax)

        water_tax = self.get_water_tax(int(self.watering_pond['gallons']))
        print(water_tax)

        grassland_tax = self.get_grassland_tax(self.ranch_sqft - self.barn_sqft)
        print(grassland_tax)

        effective_rate = (barn_tax + water_tax + grassland_tax) / self.PROPERTY_VALUE
        print("Effective tax rate: {rate}".format(
            rate=effective_rate))


    def get_barn_tax(self, area: int) -> float:
        """
        """

        # Get tax rate decimal from string
        extracted_rate = re.match(r'\d+\.\d+', self.prop_tax_rates['structure']).group(0)
        tax_rate = float(extracted_rate)

        # Multiply by tax rate and return
        return area * tax_rate


    def get_water_tax(self, volume: int) -> float:
        """
        """

        # Convert gallons to acre feet
        volume_in_acre_feet = volume / self.GALLONS_PER_ACRE_FOOT

        # Multiply by cost and return
        return volume_in_acre_feet * float(self.prop_tax_rates['water_acre_foot'])
    

    def get_grassland_tax(self, area: int) -> float:
        """Calculate grassland value from an area.

        :param area: Area in square feet
        """

        # Convert square feet to acres
        size_in_acres = area / self.SQUARE_FEET_PER_ACRE

        # Convert to units of .004 acre
        taxable_units = size_in_acres / .004

        # Multiply by cost and return
        return taxable_units * .003

