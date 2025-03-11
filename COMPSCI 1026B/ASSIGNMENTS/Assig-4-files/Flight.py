from Airport import *


class Flight:
    def __init__(self, flightNo, origAirport, destAirport):
        if not isinstance(origAirport, Airport) or not isinstance(destAirport, Airport):
            raise TypeError("The origin and destination must be Airport objects")
        if not (flightNo[:3].isalpha() and flightNo[3:].isdigit() and len(flightNo) == 6):
            raise TypeError("The flight number format is incorrect")
        self._flightNo = flightNo
        self._origin = origAirport
        self._destination = destAirport
        
    def __repr__(self):
        if self.isDomesticFlight() == True:
            return f"Flight({self._flightNo}): {self._origin.getCity()} -> {self._destination.getCity()}[domestic]"
        else:
            return f"Flight({self._flightNo}): {self._origin.getCity()} -> {self._destination.getCity()}[international]"

    def __eq__(self, other): 
        if isinstance(other, Flight) == False:
            return False
        return self._origin == other._origin and self._destination == other._destination
    
    def getFlightNumber(self):
        return self._flightNo
    
    def getOrigin(self):
        return self._origin
    
    def getDestination(self):
        return self._destination
    
    def isDomesticFlight(self):
        return self._origin.getCountry() == self._destination.getCountry()
    
    def setOrigin(self, origin):
        if not isinstance(origin, Airport):
            raise TypeError("The origin must be an Airport object")
        self._origin = origin
    
    def setDestination(self, destination):
        if not isinstance(destination, Airport):
            raise TypeError("The destination must be an Airport object")
        self._destination = destination
