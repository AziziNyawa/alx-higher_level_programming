#!/usr/bin/python3
class BaseGeometry:
    """ Class that defines the attributes of geometric shapes of a base """

    def area(self):
        """ Method that defines the area of a geomtric shape in class base """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Method that recieves the value property

        Árgs:
            name: name of the object
            value: value of the property

        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
