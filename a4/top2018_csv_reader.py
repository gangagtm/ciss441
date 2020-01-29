import csv            # import csv python module
top2018_spotify=[]    # create an empty list var
row_count=0           # count var for if logic and showing row num on print statement

# open csv file as that can be ref from csv_fi
with open('top2018.csv', 'r') as csv_fi:
    reader=csv.DictReader(csv_fi)  # use the csv.DictReader method to convert to a reader object

    for top2018_row_dic in reader:  #loop over the reader object 
        row_count +=1
        top2018_spotify.append(top2018_row_dic)
        if row_count <=10:
            print( "{0:>7}    Name: {1:<30}                 Artists: {2:<20}       Danceability: {3}".format(row_count, top2018_row_dic["name"], top2018_row_dic["artists"], top2018_row_dic["danceability"]))
            

print("Found this many rows:" + str(len(top2018_spotify)))
