import sqlite3

def load_data(conn):
    # Sample data for persons
    persons = [
        (1, 'James', 'Smith', 41),
        (2, 'Diana', 'Greene', 23),
        (3, 'Sara', 'White', 27),
        (4, 'William', 'Gibson', 23)
    ]   
    # Sample data for pets
    pets = [
        (1, 'Rusty', 'Dalmation', 4, 1),
        (2, 'Bella', 'AlaskanMalamute', 3, 0),
        (3, 'Max', 'CockerSpaniel', 1, 0),
        (4, 'Rocky', 'Beagle', 7, 0),
        (5, 'Rufus', 'CockerSpaniel', 1, 0),
        (6, 'Spot', 'Bloodhound', 2, 1)
    ]
    # Sample data for person_pet
    person_pets = [
        (1, 1),
        (1, 2),
        (2, 3),
        (2, 4),
        (3, 5),
        (4, 6)
    ]
    
    # Insert data into the person table
    conn.executemany('INSERT INTO person VALUES (?, ?, ?, ?)', persons)
    # Insert data into the pet table
    conn.executemany('INSERT INTO pet VALUES (?, ?, ?, ?, ?)', pets)
    conn.executemany('INSERT INTO person_pet VALUES (?, ?)', person_pets)

def main():
    # Connect to the database
    conn = sqlite3.connect('pets.db')  
    load_data(conn)  # Load the data
    conn.commit()    # Commit the changes
    conn.close()     # Close the connection

if __name__ == "__main__":
    print("Loading data into pets.db")
    main()

