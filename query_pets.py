import sqlite3

def query_data(conn):
    # Query to get all people and their pets
    query = '''
        SELECT p.first_name, p.last_name, pet.name, pet.breed, pet.age, pet.dead
        FROM person AS p
        JOIN person_pet AS pp ON p.id = pp.person_id
        JOIN pet ON pp.pet_id = pet.id
    '''
    
    cursor = conn.execute(query)
    # Print out each owners details and their pets
    for row in cursor:
        print(f"Owner: {row[0]} {row[1]}, Pet: {row[2]}, Breed: {row[3]}, Age: {row[4]}, Deceased: {'Yes' if row[5] else 'No'}")

def main():
    # Connect to the database
    conn = sqlite3.connect('pets.db')  
    query_data(conn)  # Fetch and display the data
    conn.close()      # Close the connection

if __name__ == "__main__":
    print("Running query_data.py")
    main()
