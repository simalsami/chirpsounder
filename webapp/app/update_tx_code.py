import psycopg2

#Name               :               Nisha Yadav
#Function Name      :               create_db_connection
#Functionality      :               Create database connection

def create_db_connection():
    conn_args = {
            "user": "postgres",
            "password": "Welcome@123",
            "host": "127.0.0.1",
            "port": "5432",
            "database": "h5db",
        }
    conn = psycopg2.connect(**conn_args)
    
    return conn
    
#Name               :               Nisha Yadav
#Function Name      :               update_virginia_tx_code
#Functionality      :               Updating TX_CODE_VA field in DB

def update_virginia_tx_code(conn, lfm_file):
        # for i in glob.glob('/home/nishayadav/Myprojects/lfm_va/*'):
        i = lfm_file.split("/")[-1]
        cursor = conn.cursor()
        print("file is:- ", lfm_file)
        cursor.execute(
            f"update table_lfm_file set TX_CODE_VA = true where split_part(lfm_filename, '/', 2) = '{i}'",

        )

        conn.commit()
        print("Done...")