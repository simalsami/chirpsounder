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

def update_tx_code(conn, file):
        # for i in glob.glob('/home/nishayadav/Myprojects/lfm_va/*'):
        table_name = None
        cursor = conn.cursor()
        i = file.split("/")[-1]
        print("File under tax code functions:-", file)
        if i.startswith("par"):
            table_name = 'table_par_file'
            cursor.execute(
            f"update {table_name} set tx_cva_rx_w2naf = true where split_part(par_filename, '/', 2) = '{i}'",

        )
        elif i.startswith("lfm"):
            table_name = 'table_lfm_file'
            cursor.execute(
            f"update {table_name} set tx_cva_rx_w2naf = true where split_part(lfm_filename, '/', 2) = '{i}'",

        )
        
            print("file is:- ", file)
        

        conn.commit()
        print("Done...")


def get_virginia_lfm_ionograms(conn, folder_name):
    query = f"select lfm_filename from table_lfm_file tlf where tlf.tx_cva_rx_w2naf is true and lfm_filename like '%{folder_name}%'"

    print(query)
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    data = [i[0] for i in data]
    data = enumerate(data)
    return data