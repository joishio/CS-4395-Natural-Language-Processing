import sys
import re
import pickle

if(len(sys.argv) > 1): #check system arguments
    if(sys.argv[1] == 'data/data.csv'): 
        datafile = sys.argv[1]

        class Person:
            def __init__(self, last, first, mi, id, phone):

                '''Person clss to store the personal information of employees
                ============================================================================================================
                parameters: str (last name), str (first name), str (middle initial), str(employeee id), str(phone number)'''

                self.last = last
                self.first = first
                self.mi = mi
                self.id = id
                self.phone = phone

            def display(self):

                '''Display function for the Person class
                =================================================
                -prints the formatted information of the person
                ================================================
                Format: 
                Employee id: XX0000
                    first mi last 
                    phone'''

                print("Employee id: ", self.id)
                print("\t", self.first, self.mi, self.last, sep = " ")
                print("\t", self.phone, "\n")

        def input_handling(filename):

            '''The input file and text processing function
            =========================================================================================
            parameters: str (path name of the input file)
            returns: dict (dictionary with keys of employee ids and values of Person objects)
            =========================================================================================
            -confirms that the file name matches data/data.csv
            -opens the file and encodes as utf-8-sig to remove new line ("\n") and invalid chracters
            -splits the read lines of the file using commas
            -ignores the first line of the file when reading by checking for keyword "Last"
            -modifies first and last name to capital case
            -modifies middle initial to single uppercase letter of "X"
            -modifies id using regex to match 2 letter 4 digit format
                -user must reenter id until it matches format
            -modifies phone number using regex to match XXX-XXX-XXXX format
                -user must renter phone until it matches format
            -creates a Person object
            -saves Person in Persons dictionary'''

            if(filename == "data/data.csv"):
                Persons = {} #Persons dictionary

                #opens file
                with open(filename, 'r', encoding="utf-8-sig") as f:
                    for line in f:
                        line = line.strip().split(',')
                        if not line[0] == 'Last':

                            #capitalize last and first names
                            last = line[0].lower()
                            line[0] = last.capitalize()

                            first = line[1].lower()
                            line[1] = first.capitalize()

                            #check middle initial and modify
                            mi = line[2]

                            if(len(mi) < 1 or not mi.isalpha()):
                                line[2] = 'X'
                            else:
                                line[2] = mi[0].upper()

                            #check employee id and modify
                            id = line[3]

                            m = re.search('[A-Z][A-Z]\d\d\d\d', id)
                            while not m:
                                print("ID invalid: ", id, "\nID is two letters followed by 4 digits")
                                id = input("Enter username:")
                                m = re.search('[A-Z][A-Z]\d\d\d\d', id)
                            line[3] = id

                            #check phone number and modify
                            phone = line[4]

                            m = re.search('\d\d\d-\d\d\d-\d\d\d\d', phone)
                            while not m:
                                print("Phone ", phone, " is invalid\nEnter phone number in form 123-456-7890")
                                phone = input("Enter phone number:")
                                m = re.search('\d\d\d-\d\d\d-\d\d\d\d', phone)
                            line[4] = phone

                            #create Person object
                            p = Person(line[0], line[1], line[2], line[3], line[4])

                            #add Person to Persons dictionay
                            if p.id in Persons: #check if id alreay exists in dictionary
                                print("id ", p.id, " is already in use\n")
                                Persons[p.id].append(p)
                            else:
                                Persons[p.id] = [p]
                            
                    return Persons     

            else:
                print("invalid filename")
        
        #save dict as pickle file 'person_dict'
        pickle.dump(input_handling(datafile), open('persons_dict', 'wb'))

        #open pickle file 'person_dict'
        persons_dict = pickle.load(open('persons_dict', 'rb'))

        #print final formatted employeee info list
        print("\nEmployee List:\n")
        for v in persons_dict.values():
            for p in v:
                p.display()

    else:
        print("invalid filename")
else:
    print("error: not enough args")