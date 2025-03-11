from Airport import *
from Flight import *

class Aviation:
   def __init__(self):
      self._allAirports = [] 
      self._allFlights =  {}   # initializing the lists and dictionaries 
      self._allCountries = {}

   def  getAllAirports(self):     # setters and getters
      return self._allAirports
   def  getAllFlights(self):
      return self._allFlights
   def  getAllCountries(self):
      return self._allCountries
   

   def setAllAirports (self, _allAirports):
      self._allAirports = _allAirports
   
   def setAllFlights(self,_allFlights):
      self._allFlights = _allFlights
   def setAllCountries(self, _allCountries):
      self._allCountries = _allCountries

   



   def loadData(self, airportFile, flightFile, countriesFile): 
 
      try:
         co = open(countriesFile, 'r', encoding='utf8')
         for line in co:
               line = line.strip().split(",")
               country = line[0].strip()
               continent = " ".join(line[1].split())     ## assigning variables for readability purposes
         
               self._allCountries[country] = [continent] ## sets the continent as the value to the country(the key)
   
         ai= open(airportFile, 'r', encoding='utf8')
         for line in ai:
         
            line = line.strip().split(",")
            line = [element.strip() for element in line]      

            country = " ".join(line[1].strip().split())   ## This is to make sure internal spaces in the continent name is preserved Ex. North America instead of NorthAmerica
            code = line[0].strip()
            city = line[2].strip()  
                  
            code = line[0]    ## assigning these variables for the sake of readability
            city = line[2]
            continent = self._allCountries[country]
            airport = Airport(code, city, country, continent) ## define each airport as an obejct of class Airport as it is added to the list of airports
            self._allAirports.append(airport)

            
   
    
         fl = open(flightFile, 'r',encoding='utf8') #  the rest of the definition for loadData() is going to be used to create the self._allFlights dictionary.

         flightsList = []
         flightsAsObjectsList = [] 
         for line in fl:
               line = line.replace(" ", "").strip(" ").replace("\n","").replace('\t',"").split(",")
               flightsList.append(line) # now we have a series of list that we need to turn into flight objects.
         
         for flight in flightsList:
               flightNo =  flight[0] 
               origAirportCode = flight[1]  
               destAirportCode = flight[2]
               origAirport = None
               destAirport = None
         
            # we need to identify origAirports and destAirports in order to add those Airport objects as parameters to the Flight object
          
               for airport in self._allAirports:       # for every list in flightsList, we iterate through the airports list
               
                  if airport.getCode()  ==  origAirportCode:  ## origAirport must be set to the airport to which teh airport code corresponds.
                     origAirport = airport

                  if airport.getCode() == destAirportCode:
                     destAirport = airport

               if destAirport and origAirport:   # If a matching destAirport and a matching origAiport have been found:
                  flight = Flight(flightNo, origAirport, destAirport) # turn the flight from a list into an object of class Flight

                  flightsAsObjectsList.append(flight)    # Now we have a list of all Flight Objects
     
   
         # Now we need to create a dictionary with an airport code as the key and the value being a list of all Flight Objects originating from it

         # How about we do :
            #for every airport in airports list:
               # take the airport code
               # for every flight in flights list:
                  # compare the airport code and the origin code within the flight object
                  # if they match:
                     # add this key-value pair to the dictionary as airportcode: [list of flights originating fom this airport]

         for airport in self._allAirports: 
            airportCode = airport.getCode() ## assigns the airport's code to the variable airportCode
            flightsFromAirport = [] ## creates an empty list of all flights originating from the given airport
            for flight in flightsAsObjectsList:  # iterates through every Flight object in the list
               origAirportCode = flight.getOrigin().getCode() # assigns another variable for readability purposes
        
               if origAirportCode == airportCode:  # if they match:
                     flightsFromAirport.append(flight) ## append the Flight object to flightsFromAirport        
         
            self._allFlights[airportCode] = flightsFromAirport   # sets the list flightsFromAirport to be the value for the key airportCode
              
   
         co.close()  # closing all the files
         ai.close()
         fl.close()
                
      except FileNotFoundError as e:
          print("", end='')
          return False
      return True
   
       


   def getAirportByCode(self, code):
      found = False     
      for airport in self._allAirports:    # iterates through every item in self._allAirports
         if airport.getCode() == code:   # if the item's code matches the inputted code:
                  found = True   #  
                  return airport  # return the item
      if not found:    
            return  -1
         
   def findAllCityFlights(self, city):   
      #Return a list that contains all Flight objects that 
      # involve the given city either as the origin or the destination
      flightsFromCity = []
      for airportCode in self._allFlights:
         for flight in self._allFlights[airportCode]: # iterates through the dictionary
            if flight.getOrigin().getCity() == city or flight.getDestination().getCity() == city: # Check if the inputted city corresponds to either of the airport codes. 
                  flightsFromCity.append(flight)
      return flightsFromCity 
            
   def findFlightByNo(self,flightNo):
      found = False
      for airportCode in self._allFlights: # iterates through the flights 
         for flight in self._allFlights[airportCode]:
            if str(flight.getFlightNumber()) == str(flightNo): # there is no __eq__ method for Flight objects, so they must be converted to strings before being compared
                  found = True
                  return flight
      if not found:
         return -1




   def findAllCountryFlights(self, country):
      flightsInvolvingCountry = [] 
      for airportCode in self._allFlights:     
         for flight in self._allFlights[airportCode]: #iterate through the dictionary
           if country == flight.getOrigin().getCountry() or country == flight.getDestination().getCountry(): # checks if the country is the destination or if it is teh origin of the flight
               flightsInvolvingCountry.append(flight) # if it does, append to the list
      return  flightsInvolvingCountry
   


   def findFlightBetween(self, origAirport, destAirport):
      intermediateAirports = set()  
      DirectFlightFound = False # establish a found flag
 
      for flight in self._allFlights[origAirport.getCode()]:  # Checks for a direct flight
            if str(flight.getOrigin()) == str(origAirport) and str(flight.getDestination()) == str(destAirport): # Once again, the flgiht objects must be compared as strings because they lack a __eq__ method
                  DirectFlightFound = True   # triggers the found flag
                  return  f"Direct Flight({flight.getFlightNumber()}): {flight.getOrigin().getCode()} to {flight.getDestination().getCode()}" # returns the flight
            


            if DirectFlightFound == False:    # looks for a connecting flight
               for airportCode in self._allFlights: # iterates through dictionary
                  for startingFlight in self._allFlights[airportCode]:
                     if str(startingFlight.getOrigin()) == str(origAirport): ##  # finds a flight that starts at the desired origin airport
                        airportCodeToCheck  = startingFlight.getDestination().getCode()  ## initializing a vartiable here for readbility. Since we now know to target the airport at which the startingflight lands, we can instruct the code to only look at that key in the dictioanry
                        for endingFlight in self._allFlights[airportCodeToCheck]: # Looks for an ending flight that starts at the desired airprot
                           if str(startingFlight.getDestination()) == str(endingFlight.getOrigin()):# double checks if the starting flight ends at the airport from which endingflight originates, just in case something goes wrong with the line above
                                 for endingFlight in self._allFlights[airportCodeToCheck]: # checks for flights that start at the endpoint of the starting flight
                                    if str(endingFlight.getOrigin()) == str(startingFlight.getDestination()) and str(endingFlight.getDestination())== str(destAirport): # confirms that the starting and endingflights connect and that they start and end at the proper airports
                                       intermediateAirports.add(endingFlight.getOrigin().getCode()) # add the middle airport to the set
                                      
      if intermediateAirports:
         return intermediateAirports # if the set exists, return it
      if not intermediateAirports:
         return -1
            
                
   def findReturnFlight(self, firstFlight):
       found = False  # establishing a found flag 
       for airportCode in self._allFlights:     # parses through every flight in the dictionary
           for flight in self._allFlights[airportCode]: 
            if flight.getDestination() == firstFlight.getOrigin() and flight.getOrigin() == firstFlight.getDestination(): # checks if the destinations and origins line up. If so, the flight is returned
                  found = True # set the flag to True
                  return flight
       if not found: 
           return -1


   def findFlightsAcross(self, ocean):

      flightCodesFromAmericas = []
      flightCodesFromAustralasia = []   ## initializing lists for use in the function
      flightCodesFromEuropeAfrica = []
      flightCodesToAmericas = []
      flightCodesToAustralasia = []
      flightCodesToEuropeAfrica = []

      flightCodesCrossingPacific = set() #initializing sets that will be outputted at the end
      flightCodesCrossingAtlantic = set()


      for airportCode in self._allFlights:  # for all airports in the Flights dictioanry
            

            airport = self.getAirportByCode(airportCode)
               # continents in the dictionary are lists with one item due to how loadData() works. 
            if airport.getContinent()[0] in ["North America", "South America"]: #if the airport is in the given continents:
               for flight in self._allFlights[airportCode]:                                 # takes advantage of the fact that flights are bound to the airport to which they originate
                     flightCodesFromAmericas.append(flight.getFlightNumber())                    #  append to the relevant list
            if airport.getContinent()[0] in ["Europe", "Africa"]:
               for flight in self._allFlights[airportCode]:
                     flightCodesFromEuropeAfrica.append(flight.getFlightNumber())
            if airport.getContinent()[0] in ["Australia", "Asia"]:
               for flight in self._allFlights[airportCode]:
                     flightCodesFromAustralasia.append(flight.getFlightNumber())



      for airportCode in self._allFlights:   # parses through the dictionary again
          for flight in self._allFlights[airportCode]:
              flightDestinationContinent = flight.getDestination().getContinent() # setting this variable for readability. This variable holds the continent to which the flight is destined.
              flightNumber = flight.getFlightNumber()

              if flightDestinationContinent[0] in ["North America", "South America"]: # now we assign each flight number to a list based on the continent of its destination
                   flightCodesToAmericas.append(flightNumber)
                   
              if flightDestinationContinent[0] in ["Europe", "Africa"]:
                   flightCodesToEuropeAfrica.append(flightNumber)
              if flightDestinationContinent[0] in ["Australia", "Asia"]:
                   flightCodesToAustralasia.append(flightNumber)
   

   


      for airportCode in self._allFlights:   # parses through the dictionary once again. It's possible to put the code below into the previous loop, but it's easier to just make a new loop
          for flight in self._allFlights[airportCode]:
             
              flightNumber = flight.getFlightNumber() #  Assigning variable for readbility
            
              if flightNumber in flightCodesFromAmericas and flightNumber in flightCodesToEuropeAfrica: #checks if the flight is from NA/SA to EU/AFRICA
                  flightCodesCrossingAtlantic.add(flightNumber)
                 
              if flightNumber in flightCodesToAmericas and flightNumber in flightCodesFromEuropeAfrica: # checks if flight is from EU/AFRICA to NA/SA
                  flightCodesCrossingAtlantic.add(flightNumber)
           

              if flightNumber in flightCodesFromAmericas and flightNumber in flightCodesToAustralasia or flightNumber in flightCodesToAmericas and flightNumber in flightCodesFromAustralasia: #Checks if flight is between ASIA/AUS and NA/SA
                  flightCodesCrossingPacific.add(flightNumber)
 
 

      if ocean  == "Pacific": ## chooses which set to output at the end based on the desired ocean
          return flightCodesCrossingPacific
      if ocean  == "Atlantic":
          return flightCodesCrossingAtlantic
                  

   
           