from pyscript import document, display


#assigning each member to a grade level
grade_7 = {"Joaquin Hizon", "Eron Almiron"}
grade_8 = {"Thomas Cruz", "Alexander Great"}
grade_9 = {"Coca Cola", "Jane Doe"}
grade_10 = {"Chloe Almiron", "Sebastian Stan"}

def add_member(e):
    #
    members_set = grade_7 | grade_8 | grade_9 | grade_10

    #getting first and last name
    first_name = document.getElementById("firstname").value.strip()
    last_name = document.getElementById("lastname").value.strip()
    full_name = f"{first_name} {last_name}"

    #putting the new input inside a set
    new_member_set = {full_name}

    #combining grade sets and the new member set
    members_set = members_set | new_member_set

    #arranging in alphabetical order and joins them into one string
    members_list_html = "<br>".join(sorted(members_set))

    #calculating total members 
    total_count = len(members_set)

    #displaying the amount of members and a list of all the members
    document.getElementById("members_box").innerHTML = (
        f"Total Member: {total_count}",
        f"All Members:<br>{members_list_html}"
    )

#list of members
club_members = ["Joaquin Hizon", "Eron Almiron", "Jeff De Jesus","Cassandra De Jesus","Sebastian Stan"]

def whitelist(e):
    
    #clearing the previous result to display the new message 
    document.getElementById("output").innerHTML = ""

   
    #getting the values
    first_name = document.getElementById("firstname").value
    last_name = document.getElementById("lastname").value
    full_name = first_name + " " + last_name

    #checking if inputted name is in the list
    is_member = full_name in club_members

    #response after checking if inputted name is on the list
    message = {
        True: "Congratulations "+ full_name +"! You are part of the Varsity team.",
        False: "Sorry "+ full_name +", your name is not on the list."
    }

    #displaying the result
    display(message[is_member], target="output")


#assigning the element symbol, atomic number, and atomic mass for each nonmetal
nonmetals= {"H": ("Hydrogen", 1, 1.008),
            "He": ("Helium", 2, 4.003),
            "C": ("Carbon", 6, 12.011),
            "N": ("Nitrogen", 7, 14.007),
            "O": ("Oxygen", 8, 15.999),
            "F": ("Fluorine", 9, 18.998),
            "Ne": ("Neon", 10, 20.180),
            "P": ("Phosphorus", 15, 30.974),
            "S": ("Sulfur", 16, 32.06),
            "Cl": ("Chlorine", 17, 35.45),
            "Ar": ("Argon", 18, 39.948),
            "Se": ("Selenium", 34, 78.971),
            "Br": ("Bromine", 35, 79.904),
            "Kr": ("Krypton", 36, 83.798),
            "I": ("Iodine", 53, 126.90),
            "Xe": ("Xenon", 54, 131.29),
            "Rn": ("Radon", 86, 222.02)
            
            }


#function to search for a non-metal
def search_nonmetal(e):  
    #getting the value from the input field
    Planet2 = document.getElementById("nonmetal1").value
    #retrieving information from dictionary
    result = nonmetals.get(Planet2, ("Non-metal not found", "-", "-"))
    #displaying the result 
    #non-metal code, Name, Atomic Number, Atomic Mass
    document.getElementById("name").innerText = result[0]
    document.getElementById("number").innerText = result[1]
    document.getElementById("mass").innerText = result[2]