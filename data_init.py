import psycopg2

def insert_dummy_person(conn, name, age, phone_number, payment_mode):
    sql = "INSERT INTO person (name, age, phone_number, payment_mode) VALUES (%s, %s, %s, %s)"
    with conn.cursor() as cur:
        cur.execute(sql, (name, age, phone_number, payment_mode))
    conn.commit()

def insert_dummy_address(conn, street, city, postal_code):
    sql = "INSERT INTO address (street, city, postal_code) VALUES (%s, %s, %s)"
    with conn.cursor() as cur:
        cur.execute(sql, (street, city, postal_code))
    conn.commit()

def insert_dummy_review(conn, person_id, stars, comment):
    sql = "INSERT INTO review (person_id, stars, comment) VALUES (%s, %s, %s)"
    with conn.cursor() as cur:
        cur.execute(sql, (person_id, stars, comment))
    conn.commit()

if __name__ == "__main__":

    conn = psycopg2.connect(dbname='dms', user='stacy', password='stacy', host='localhost', port='5432')

    # Insert dummy data
    insert_dummy_person(conn, 'stacy njehia', 30, '0798631879', 'Credit Card')
    insert_dummy_person(conn, 'israel njehia', 33, '0798631879', 'Cash')
    
    insert_dummy_address(conn, 'Kikuyu', 'Nairobi', '235698-2154')
    insert_dummy_address(conn, 'Homabay', 'Kisumu', '336898-6980')

    insert_dummy_review(conn, 1, 5, 'Great service!')    
    insert_dummy_review(conn, 1, 4, 'Cool ambience!')
    conn.close()


