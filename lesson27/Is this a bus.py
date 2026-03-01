class Vehicle:
    def __init__(self,name,max_speed,milage):
        self.name = name
        self.max_speed=max_speed
        self.milage = milage


class Bus(Vehicle):
    pass

school_bus = Bus("School Volvo",12,300)
print("Vechicle Name",school_bus.name)
print("Speed",school_bus.max_speed)
print("Millage",school_bus.milage)