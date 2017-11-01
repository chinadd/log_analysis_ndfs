#! /usr/bin/env python
import psycopg2


DB_name = "news"

query1 = "select * from toparticle limit 3;"
query2 = "select * from topauthor;"
query3 = "select * from log_error_view where \"Error\" > 1;"

def connect(database_name="news"):
    try:
        db = psycopg2.connect(dbname=DB_name)
        cursor = db.cursor()
        return db, cursor
    except:
        print("<error message>")

def get_query_results(query):
    db, cursor = connect()
    cursor.execute(query)
    results = cursor.fetchall()
    db.close()
    return results

"""top 3 popular articles"""

def pop_article():
    results = get_query_results(query1)
    print "Most popular articles : "
    for row in results:
        print row[0], "-", row[1], "views"



""" popularity of authors"""


def pop_author():
    results = get_query_results(query2)
    print "Most popular authors"
    for row in results:
        print row[0], "-", row[1], "views"


""" error rate >1% """


def error_date():
    results = get_query_results(query3)
    print "Days with more than 1% errors:"
    for row in results:
        print row[0], "-", row[1], "%"

if __name__ == '__main__':
    pop_article()
    print "----------------------------------------"
    pop_author()
    print "----------------------------------------"
    error_date()
