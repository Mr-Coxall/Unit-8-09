# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This class is used to define a tandum bike object

from bicycle import *

class Tanden_Bike(Bicycle):
    # this class defines a tanden bicycle

    # class variable shared by all instances
    

    def __init__(self, gear, cadence = 0):
        # private fields
        
        Bicycle.__init__(self, gear, cadence = 0)
        self.__seats = 2

        # public properties
        #self.some_property = None

    # properties
    def get_number_of_seats(self):
        # get the number of seats property
        return self.__seats
    
    # private methods
    
    # public methods
    
    def current_state(self):
        # returns the current state of the tandem bicycle as a string 
        
        # this varaible is local to this method
        return_string = Bicycle.current_state(self) + ' # of seats: ' + str(self.__seats)
        
        return return_string
