
import copy
import csv


def main():
    CSVFILE = "email.csv"
    FILE = "email_template.txt"
    email_list = []
    template: str = ''

    # Read CSV file
    with open(CSVFILE, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

                
        for row in rows:
            name = row[0].title()
            email = row[2].lower()
            temp = [name, email]
            email_list.append(temp)

    #file.close()
    with open(FILE, 'r') as file_txt:
        template = file_txt.read()
    #file.close()
        for person in email_list:
            
            name = person[0]
            email = person[1]
            email_template = template
            email_template = email_template.replace("{first_name}", name)
            email_template = email_template.replace("{email}", email)
            print(email_template)
            print("-" * 50)
    
              
              
              
if __name__ == "__main__":
    main()
              
              
              
              
    
            
        
