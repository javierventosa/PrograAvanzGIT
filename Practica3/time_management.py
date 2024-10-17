import re

class Time:
    """
    Class that represents a time with AM/PM or 24 hours format.
   
    Class Attributes:
      TIME_FORMATS # ("AM", "PM", "24 HOURS") (AM = 00:00-11:59, PM = 12:00-23:59)
      time_count = 0 # Counts the number of Time objects created
    Attributes:
        hours #Stores the hours 
          #(1 to 12 for AM/PM, 0 to 23 for 24 hours)
        minutes #Stores the minutes (0 to 59)
        seconds #Stores the seconds (0 to 59)
        format #Stores the time format: “AM", "PM","24 HOURS"
    """
    TIME_FORMATS = ["AM", "PM", "24 HOURS"]
    time_count = 0

    def __init__(self, hours=0, minutes=0, seconds=0, format=""):
        """
        Method to Initialize attributes to 0.
        """
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.format = format 
        Time.time_count += 1

    def __asign_format(self, pszFormat):
        """
        Checks pszFormat has correct value & assigns it to format
        Converts to upper case to avoid problems with 
        capitalization.
        Args:
        pszFormat: String with time format ("AM", "PM" or "24 
        HOURS").
        Returns:
        True if the format is correct, False otherwise.
        """
        upper_format = pszFormat.upper()
        if upper_format in Time.TIME_FORMATS:
            self.format = upper_format
            return True
        else:
            return False

    def __is_24hour_format(self):
        """
        Checks if the time format is "24 HOURS".
        Returns:
        True if the format is "24 HOURS", False otherwise.
        """
        return self.format == "24 HOURS"

    def _is_valid_time(self):
        """
        Checks if the time is correct according to the format.
        Returns:
        True if the time is correct, False otherwise.
        """
        if self.__is_24hour_format():
            if self.hours < 0 or self.hours > 23:
                return False
        else:
            if self.hours < 1 or self.hours > 12:
                return False
        if self.minutes < 0 or self.minutes > 59:
            return False
        if self.seconds < 0 or self.seconds > 59:
            return False
        return True
         

    def set_time(self, nHoras, nMinutos, nSegundos, pszFormato):
        """
        Assigns a time to the class.
        Args:
            nHoras: Hours (1 to 12 AM/PM, 0 to 23 for 24 hours).
            nMinutos: Minutes (0 to 59).
            nSegundos: Seconds (0 to 59).
            pszFormato: Time format ("AM", "PM" or "24 HOURS").
            Returns:
            True if the time could be assigned correctly, 
            False otherwise.
        """
        if self.__asign_format(pszFormato):
            self.hours = nHoras
            self.minutes = nMinutos
            self.seconds = nSegundos
            if self._is_valid_time():
                return True
        return False

    def get_time (self):
        """
        Returns the current time of the class.
        """
        if self.format in ["AM", "PM"]:
            return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d} {self.format}"
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"


    @classmethod
    def from_string(cls, time_string):
        """
        Class method to create Time object from string.
        Args:
            time_string (str): A string representing time in the 
            format "HH:MM:SS FORMAT", where FORMAT is AM, PM, or 24 HOURS.
        Returns:
            Time: new Time object with the parsed time.
            If the time string is invalid, print a message.
        """
        # Import the 're' module for regular expressions
        # Define regular expression pattern to match time strings
        pattern = r"^(?P<hours>\d{2}):(?P<minutes>\d{2}):(?P<seconds>\d{2}) (?P<format>AM|PM|24 HOURS)$"
        
        # Use re.match to check if the time_string matches pattern
        match = re.match(pattern, time_string)
        
        if match:
            # Extract hours, minutes, seconds, & format from matched groups
            hours, minutes, seconds, format = match.groups()

            #Convert hours, minutes and seconds
            hours = int(hours)
            minutes = int(minutes)
            seconds = int(seconds)
            
            # Create a new Time object
            new_time = cls(hours, minutes, seconds, format)
            
            # Return the new Time object
            return new_time
        else:
            # Print a message if the time string is invalid
            print("Invalid time string. Please use the format HH:MM:SS FORMAT.")
            return None
            

    @staticmethod
    def is_valid_format(time_format):
        """
        Static method to check if a given time format is valid.
        Args:
        time_format (str): The time format to check.
        Returns:
        bool: True if the format is valid (AM, PM, or 24 HOURS), 
            False otherwise.
        """
        return time_format in Time.TIME_FORMATS

    @classmethod
    def get_time_count(cls):
        """
        Class method to get total number of Time objects created

        Returns:
            int: The number of Time objects created.
        """
        return cls.time_count