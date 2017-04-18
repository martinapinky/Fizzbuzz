class Car(object):

    def __init__(self):
        self.model = 'GM'
        self.name = "General"
        self.num_of_doors = 4
        self.num_of_wheels = 4
        self.speed = 0
        self.type = 'saloon'

    def __init__(self, name, model):
        self.model = model
        self.name = name
        if self.name == 'Porshe' or 'Koenigsegg':
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4
        self.num_of_wheels = 4
        self.speed = 0
        self.type = 'saloon'

    def __init__(self, name):
        self.name = name
        self.model = 'GM'
        if self.name == 'Porshe' or 'Koenigsegg':
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4
        self.num_of_wheels = 4
        self.speed = 0
        self.type = 'saloon'

    def __init__(self, name, model, type):
        self.model = model
        self.name = name
        if self.name == 'Porshe' or 'Koenigsegg':
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4
        self.type = type
        if self.type == 'trailer':
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4
        self.speed = 0

    def drive(self, n):
        if self.name == 'Mercedes':
            self.speed = 1000
        else:
            self.speed = 11 * n

    def is_saloon(self):
        if self.type == 'saloon':
            return True
        else:
            return False




