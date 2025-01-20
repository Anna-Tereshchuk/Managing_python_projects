import db

def test_create_schema(database):
    # Call the create_schema function to initialize the database schema
    db.create_schema(database)
    
    # Ensure the 'logs' table exists
    cur = database.cursor()
    cur.execute('SELECT * FROM logs')  # This should not raise an error if the table exists

    # Test idempotence: Ensure that running create_schema again does not cause an error
    db.create_schema(database)
