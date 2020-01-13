class ContactInfo (object):
  # constructor
  def __init__ (self, street, city, state, zip_code, country, phone, email):
      self.street=street
      self.city=city
      self.state=state
      self.zip_code=zip_code
      self.country=country
      self.phone=phone
      self.email=email
      

  # string representation of Contact Info
  def __str__ (self):
      return phone_book[self]=(self.street:street,city,state,zip_code,country,phone,email)

# Define global dictionary to hold all the contact information
phone_book = {}

# This function adds the contact information of a new person in the
# dictionary
def add_person():
  # Prompt the user to enter the name of the new person

  # Check if name exists in phone book. If it does print a message
  # to that effect and return

  # Prompt the user to enter the required contact information

  # Create the ContactInfo object
  contactObj = ContactInfo (street, city, state, zip_code, country, phone, email)

  # Add the name and the contact information to the phone dictionary

  # Print message that the information was added successfully

# This function deletes an existing person from the phone dictionary
def delete_person():
  # Prompt the user to enter the name of the person

  # If the name exists in phone book delete it.
  # Print message as to the action.

# This function updates the information of an existing person
def update_person():
  # Prompt the user to enter the name of the person

  # Check if name exists in phone book. If it does prompt
  # the user to enter the required information.

  # Write a message as to the action

# This function prints the contact information of an existing person
def search_person():
  # Prompt the user to enter the name of the person

  # Check if name exists in phone book. If it does print the
  # information in a neat format.

  # If the name does not exist print a message to that effect.

# This function open the file for writing and writes out the contents
# of the dictionary.
def save_quit():
  # Open file for writing

  # Iterate through the dictionary and write out the items in the file

  # Close file

  # Print  message

# This function prints the menu, prompts the user for his/her selection
# and returns it.
def menu():

# This function opens the file for reading, reads the contact information
# for each person and adds it to the dictionary.
def create_phone_book():
  # Open file for reading
  in_file = open ("phone.txt", "r")

  # Read first line (name)
  line = in_file.readline()
  line = line.strip()

  # Loop through the entries for each person
  while (line != ""):
    name = line

    # Read street

    # Read city

    # Read state

    # Read zip-code

    # Read country

    # Read phone number

    # Read e-mail address

    # Read blank line

    # Read first line of the next block of data
    line = in_file.readline()
    line = line.strip()

    # Create ContactInfo object

    # Add to phone dictionary

  # Close file

def main():
  # Read file and create phone book dictionary
  create_phone_book()

  # Print logo
  print("Phone Book")

  # Print menu and get selection
  selection = menu()

  # Process request, print menu and prompt again and again
  # until the user types 5 to quit.

  # Save, print goodbye message, quit
