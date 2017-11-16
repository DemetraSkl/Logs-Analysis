#!/usr/bin/env python2
#
# news DB query program source code

import datetime
import psycopg2

DBNAME = "news"


def get_article_info(query):
    conn = psycopg2.connect(database=DBNAME)
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result


# each method returns a list of tuples
def get_pop_articles():
    """Returns most popular three articles of all time"""
    query_1 = "select articles.title, count(*) as views "\
              "from articles join log "\
              "on log.path like concat('/article/',articles.slug) "\
              "group by articles.title "\
              "order by views desc "\
              "limit 3;"
    pop_art = get_article_info(query_1)
    print "Top three articles:"
    for i in pop_art:
        print i[0], "--", i[1], "views"
    return None


def get_pop_authors():
    """Returns list of authors in order of popularity"""
    query_2 = "select authors.name, count(*) as views "\
              "from articles join log "\
              "on log.path like concat(\'%\',articles.slug) "\
              "join authors "\
              "on articles.author = authors.id "\
              "group by authors.name "\
              "order by views desc;"
    pop_auth = get_article_info(query_2)
    print '\n'
    print "Author popularity:"
    for i in pop_auth:
        print i[0], "--", i[1], "views"
    return None


def get_error_days():
    """Returns days when more than 1 percent of requests led to errors"""
    query_3 = "select er.day, "\
              "100 * (cast(er.error_requests as float) / "\
              "cast(ar.total_requests as float)) "\
              "as error_percentage "\
              "from (select date_trunc(\'day\',time) as day, "\
              "count(*) as error_requests from log "\
              "where status=\'404 NOT FOUND\' group by day) er "\
              "inner join (select date_trunc(\'day\',time) as day, "\
              "count(*) as total_requests from log group by day) ar "\
              "on ar.day = er.day "\
              "where 100 * (cast(er.error_requests as float) / "\
              "cast(ar.total_requests as float)) > 1;"
    err_days = get_article_info(query_3)
    print '\n'
    print "Days with greater than 1 percent error:"
    for i in err_days:
        print i[0].date(), "--", round(i[1], 2), "percent errors"
    return None

if __name__ == "__main__":
    get_pop_articles()
    get_pop_authors()
    get_error_days()
