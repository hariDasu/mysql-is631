import pymysql


def __connect__():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='password', db='zips')
    cur = conn.cursor()
    return cur

def query1():
    cur=__connect__()
    sql='''SELECT state, SUM(pop) AS totalPop
           FROM zipCodes
           GROUP BY state
           HAVING totalPop >= (10*1000*1000)'''
    cur.execute(sql);
    res='''<table class='table table-bordered table-hover'> 
            <tr><th>State</th>
                <th>Population</th></tr>'''
    for row in cur:
        res+="<tr><td>"+row[0]+"</td><td>"+str(row[1])+"</td>"
    return res


def query2():
    cur=__connect__()
    sql1=""" (SELECT state, SUM(pop) as totalPop FROM zipCodes GROUP BY state)"""
    sql2="SELECT state, MIN(pop) from zipCodes having state="+sql1
    sql=sql2
    print  sql
    cur.execute(sql);
    res='''<table class='table table-bordered table-hover'> 
            <tr><th>State</th>
                <th>Population</th></tr>'''
    for row in cur:
        res+="<tr><td>"+row[0]+"</td><td>"+str(row[1])+"</td>\n"
    return res

    
def query3():
    cur=__connect__()
    sql='''SELECT state,SUM(pop) FROM zipCodes GROUP BY state'''
    cur.execute(sql);
    res='''<table class='table table-bordered table-hover'> 
            <tr><th>State</th>
                <th>Population</th></tr>'''
    for row in cur:
        res+="<tr><td>"+row[0]+"</td><td>"+str(row[1])+"</td>"
    return res

if __name__=="__main__":
   print(query2())
    
