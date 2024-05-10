#!/usr/bin/python3
""" 
User class
"""

class User:
    """ User class with email property """

    def __init__(self):
        """ Initialize user with no email """
        self.__email = None

    @property
    def email(self):
        """ Getter for email property """
        return self.__email

    @email.setter
    def email(self, value):
        """ Setter for email property """
        if not isinstance(value, str):
            raise TypeError("Email must be a string")
        self.__email = value

if __name__ == "__main__":
    # Test the User class
    u = User()
    u.email = "john@snow.com"  # This will call the email setter
    print(u.email)              # This will call the email getter to retrieve the email

