class Car(object):

    def __init__(self):
        self.model = 'GM'
        self.name = "General"
        self.num_of_doors = 4

    def __init__(self, name, model):
        self.model = model
        self.name = name
        if self.name == 'Porshe' or 'Koenigsegg':
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4

    def __init__(self, name):
        self.name = name
        self.model = 'GM'
        if self.name == 'Porshe' or 'Koenigsegg':
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4


    def __init__(self, name, model, ):
        self.model = model
        self.name = name
        if self.name == 'Porshe' or 'Koenigsegg':
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4



