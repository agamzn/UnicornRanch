class UnicornRanch(object):
    def __init__(self):
        self.ranch_sqft = 326700
        self.barn_sqft = 1200

        self.watering_pond = {
            'gallons':458268,
            'acre_feet':1.4063731
        }

        self.prop_tax_rates = {
            'water_acre_foot':0.74,
            'structure':1.33202,
            'grassland':0.52272
        }
        return;
    def TaxDictionary(self):
        InitialBill = (self.ranch_sqft * self.prop_tax_rates['grassland']) + (self.barn_sqft * self.prop_tax_rates['structure']) + (self.watering_pond['acre_feet'] * self.prop_tax_rates['water_acre_foot'])
        Year2 = InitialBill + (InitialBill * .012)
        Year3 = Year2 + (Year2 * .012)
        Year4 = Year3 + (Year3 * .012)
        Year5 = Year4 + (Year4 * .012)
        self.dictTax = {
            'TaxBill': int(InitialBill),
            'TaxBillYear2': int(Year2),
            'TaxBillYear3': int(Year3),
            'TaxBillYear4': int(Year4),
            'TaxBillYear5': int(Year5),
            'TaxRate': int((InitialBill / 1200000) * 100)
        }
        print("Initial Tax Bill: $" + str(self.dictTax['TaxBill']))
        print("Year 5 Tax Bill @ 1.2% APR: $" + str(self.dictTax['TaxBillYear5']))
        print("Tax Percentage Assuming Property Value of $1.2 Million: " + str(self.dictTax['TaxRate']) + "%")
        return;

x = UnicornRanch()
x.TaxDictionary()
