import csv

def save_as_csv( jobs ):
    f = open('output.csv', 'w')
    writer = csv.writer(f)
    writer.writerow(['title', "company", 'location', 'link'])
    for job in jobs:
        writer.writerow( job.values() )
    return f
