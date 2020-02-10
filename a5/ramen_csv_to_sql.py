"""
What: Moving data from CSV into SQLite db.
When: Feb 9th 2020
Who: Ganga Gautam
"""

import csv            # import csv python module  
import sqlite3        # import sqlite3 module

DB_FILE= 'ramen_ratings.db'      # create database file
conn= sqlite3.connect(DB_FILE)   # connect to database file

def create_ramen_ratings_table(): 
    """ This method will create ratings table if it does not exist. """

    # creates a sql cursor and executes it 
    cur= conn.cursor()    
    str_sql = """
        CREATE TABLE if not exists ratings (
            Review_id integer primary key,
            Brand char(50) ,
            Variety char(50) ,
            Style char(50),
            Country char(50) ,
            Stars float 
        );
         """

    cur.execute(str_sql)
    conn.commit()

def open_csv_insert_into_db(): 
    """ This method will open the csv file and load into the ratings table. """
    
    cur= conn.cursor()
    row_count=0  # count var for if logic 

    # open csv file as that can be ref from csv_fi
    with open('ramen-ratings.csv', 'r') as csv_fi:
        reader=csv.DictReader(csv_fi)  # use the csv.DictReader method to convert to a reader object

        for ramenrating_row_dic in reader:  #loop over the reader object 
            row_count +=1

            r_brand= ramenrating_row_dic["Brand"]
            r_country= ramenrating_row_dic["Country"]
            r_stars= ramenrating_row_dic["Stars"]

            sql_str_insert_with_param= """
                INSERT INTO ratings
                    (Brand, Country, Stars)
                VALUES
                    (?, ?, ?)
                """
            data_tuple= (r_brand, r_country, r_stars)
            cur.execute(sql_str_insert_with_param, data_tuple)
            conn.commit()

            #print the first ten rows
            if row_count <=10: 
                 print( "{0:>7}    Brand: {1:<20}    Country: {2:<15}   Rating: {3}".format(row_count, 
                    r_brand, r_country, r_stars))
    cur.close()
                
def main():
    create_ramen_ratings_table()
    open_csv_insert_into_db()

    conn.close() #close connection to database

if __name__== "__main__":    
    main()                  # call the main method
