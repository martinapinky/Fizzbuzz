class Car(object):

    def __init__(self):
        self.model = 'GM'
        self.name = "General"

    def __init__(self, name, model):
        self.model = model
        self.name = name

    def __init__(self, name):
        self.name = name
        self.model = 'GM'

    def number_of_doors(self):
        if self.name == 'Porshe' or 'Koenigsegg':
            return 2
        else:
            return 4
    def



