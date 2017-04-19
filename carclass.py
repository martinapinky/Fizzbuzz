class Car(object):
    num_of_doors = 4
    speed = 0

    def __init__(self, *args): #args -- tuple of anonymous arguments  #kwargs -- dictionary of named arguments
        self_args = ['General', 'GM', 'saloon']
        for arg_index in range(0, len(args)):
            self_args[arg_index] = args[arg_index]

        self.name = self_args[0]
        self.model = self_args[1]
        self.type = self_args[2]
        self.num_of_doors = Car.num_of_doors
        self.num_of_wheels = 4

        if self.name == 'Porshe' or self.name == 'Koenigsegg':
            self.num_of_doors = 2

        if self.type == 'trailer':
            self.num_of_wheels = 8

        self.speed = 0

    def drive(self, n):
        if self.name == 'Mercedes':
            self.speed = (1000/3) * n
        else:
            self.speed = 11 * n
        return self

    def is_saloon(self):
        if self.type == 'saloon':
            return True
        else:
            return False

mycar = Car('Porshe', 'Truck', 'trailer')
print(mycar.speed)
print(mycar.name)
print(mycar.num_of_doors)
print(mycar.drive(7).speed)



