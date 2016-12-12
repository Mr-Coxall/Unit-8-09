# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This class is used to define a transportation object

#from abc import ABCMeta, abstractmethod, abstractproperty

class Transportation:
    # this class defines a transportation object
    #__metaclass__ = ABCMeta

    # class variable shared by all instances
    
    def __init__(self):
        # private fields
        
        self.__speed = 0

    # properties
    #@abstractproperty
    def get_speed(self):
        # get the speed property
        return self.__speed
    
    
    # private methods
    
    # public methods
    
    #@abstractmethod
    def current_state(self):
        # returns the current state of the transportation thing as a string 
        
        # this varaible is local to this method
        return_string = 'Speed: ' + str(self.__speed)
        
        return return_string
