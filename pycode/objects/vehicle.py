class Vehicle:
    """
    Vehicle is a type that describes a machine that helps us travel
    """


    def __init__(self, distance_travelled=0, unit='miles'):
        """
        Customizes the init of object
        """
        self.distance_travelled = distance_travelled
        self.unit = unit

    # @classmethod
    # def bicycle(cls, tires=None):
    #     if not tires:
    #         tires = [cls.default_tire, cls.default_tire]
    #     return cls(None, tires)


    def description(self):
        message = f"A {self.__class__.__name__} has travelled {self.distance_travelled} {self.unit}"
        print(message)
        return message

    def __str__(self):
        # like toString method.
        return f"<{self.__class__.__name__} {self.__dict__}>"