# - Write the docstrings for this class after carefully analyzing the code.
# - Document the __init__() function and the properties with their corresponding docstrings.

class Flight:
    """Class that of Flights
    Atributes:
        String number: contains the flight number
        String origin: contains the origin of flight
        String destination: contains the destination of flight
        Integer num_passengers: contains the number of passengers on the booked flight
    Methods:
        display_flight_data(): Shows and prints the flight data for user
    """
        
    def __init__(self, number, origin, destination, num_passengers, total_weight, pilot, crew):
        """Initialztion data for the Flight class
            Arguments:
                String number: flight number
                String origin: origin of the flight
                String destination: destination of the flight
                Integer num_passengers: passenger total 
                Float total_weight: total weight of entire flight
                Pilot pilot: the pilot of current flight
                List crew: the list for crew members
        """
        self.number = number
        self.origin = origin
        self.destination = destination
        self.num_passengers = num_passengers
        self._total_weight = total_weight
        self._pilot = pilot 
        self._crew = crew
    
    @property
    def total_weight(self):
        """Total weight of the flight which includes the crew, passengers, luggage and fuel"""
        return self._total_weight
    
    @total_weight.setter
    def total_weight(self, weight):
        if weight > 0 and isinstance(weight, float):
            self._total_weight = weight	
    
    @property
    def pilot(self):
        """Current Pilot"""
        return self._pilot
    
    @pilot.setter
    def pilot(self, new_pilot):
        self._pilot = new_pilot
    
    @property
    def crew(self):
        """Current Crew"""
        return self._crew
    
    @crew.setter
    def crew(self, new_crew):
        self._crew = new_crew
    
    def display_flight_data(self):
        """Displays the flight data"""
        print("== Flight ==")
        print("Number:", self.number)
        print("Number of Passengers:", self.num_passengers)
        print("Weight:", self._total_weight)
        print("Pilot:", self._pilot)
        print("Crew:", self._crew)