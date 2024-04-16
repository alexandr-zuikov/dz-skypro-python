class Smartphone:
    brand = "Brand"
    model = "Model"
    number = "+79000000000"

    def __init__(self, brand, model, number):
        self.brand = brand
        self.model = model
        self.number = number

    def print_catalog(self):
            print(self.brand,"-",self.model,".",self.number)