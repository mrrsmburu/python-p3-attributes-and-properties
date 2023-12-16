#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
     def __init__(self):
        self._name = None

    
    def name(self):
        return self._name

    
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be a string between 1 and 25 characters.")

    
    def breed(self):
        return self._breed

    
    def breed(self, value):
    
        if value in approved_breeds:
            self._breed = value
        else:
            print("Breed must be in the list of approved breeds.") 
                                                                                             