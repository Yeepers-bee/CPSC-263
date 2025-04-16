import csv
import os

def main():
    CSVFILE = "email.csv"
    FILE = "email_template.txt"
    
    # Check if files exist
    print(f"Checking for CSV file: {os.path.exists(CSVFILE)}")
    print(f"Checking for template file: {os.path.exists(FILE)}")
    
    email_list = []
    
    try:
        # Read CSV file
        with open(CSVFILE, 'r') as file:
            print("CSV file opened successfully")
            reader = csv.reader(file)
            rows = list(reader)
            print(f"Read {len(rows)} rows from CSV")
            
            if rows:
                print(f"First row has {len(rows[0])} cells")
                print(f"First row content: {rows[0]}")
            
            # Process accordingly based on your actual CSV structure
            # ... rest of the code as above
    except Exception as e:
        print(f"Error reading CSV: {e}")
        
    # Continue with the rest of your code...

if __name__ == "__main__":
    main()
