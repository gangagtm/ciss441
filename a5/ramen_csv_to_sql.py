


import csv            # import csv python module  
import sqlite3

DB_FILE= 'ramen_ratings.db'
conn= sqlite3.connect(DB_FILE)

def create_ramen_ratings_table():
    cur= conn.cursor()
    str_sql = """
        CREATE TABLE ratings (
            Review int primary key autoincrement,
            Brand char(50),
            Variety char(50),
            Style char(50),
            Country char(50),
            Stars float
        );
         """

    cur.execute(str_sql)
    conn.commit()



def main():
    create_ramen_ratings_table()
    row_count=0  # count var for if logic and showing row num on print statement

    # open csv file as that can be ref from csv_fi
    with open('ramen-ratings.csv', 'r') as csv_fi:
        reader=csv.DictReader(csv_fi)  # use the csv.DictReader method to convert to a reader object

        for ramenrating_row_dic in reader:  #loop over the reader object 
            row_count +=1
            if row_count <=10:
                print( "{0:>7}    Brand: {1:<30}                 Country: {2:<20}       Rating: {3}".format(row_count, 
                    ramenrating_row_dic["Brand"], ramenrating_row_dic["Country"], ramenrating_row_dic["Stars"]))

    conn.close()

if __name__== "__main__":
    main()
