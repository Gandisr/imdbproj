import csv, imdb_line

with open('out.csv', 'w', newline='') as csvfile:
    fieldnames = ['Title', 'Year', 'Budget', 'Gross', 'IMDB_rating', 'Cast']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range (550, 650):
        line = imdb_line.Imdb_Line(i)
        d = line.getNewLine()
        print(d)
        if(d is not None):
            writer.writerow({k:v.encode('utf8') for k,v in d.items()})