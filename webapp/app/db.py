import psycopg2

#Name               :               Nisha Yadav
#Function Name      :               create_db_connection
#Functionality      :               Create database connection

def create_db_connection():
    conn_args = {
            "user": "postgres",
            "password": "Password@123",
            "host": "127.0.0.1",
            "port": "5432",
            "database": "h5db",
        }
    conn = psycopg2.connect(**conn_args)
    
    return conn