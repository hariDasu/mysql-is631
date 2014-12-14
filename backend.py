import pymysql
from pprint import PrettyPrinter

pp=PrettyPrinter(indent=4)


def __connect__():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='password', db='zips')
    cur = conn.cursor()
    return cur

def __connectEmps__():
    conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='password',db='employees')
    cur=conn.cursor()
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
    sql=""" (SELECT state, AVG(pop) as avgPop FROM zipCodes GROUP BY state)"""
    cur.execute(sql);
    res='''<table class='table table-bordered table-hover'> 
            <tr><th>State</th>
                <th> Average City Population</th></tr>'''
    for row in cur:
        res+="<tr><td>"+row[0]+"</td><td>"+str(row[1])+"</td>\n"
    return res

    
def query3():
    cur=__connect__()
    sql1='''SELECT 
    t.state,t.city,t.pop
FROM 
    zipCodes  t
  JOIN
    ( SELECT state
           , MAX(pop) AS Population 
      FROM zipCodes
      GROUP BY state
    ) maxp  
        ON  maxp.state = t.state
        AND maxp.Population = t.pop'''
    
    sql2='''SELECT 
    t.state,t.city,t.pop
FROM 
    zipCodes  t
  JOIN
    ( SELECT state
           , MIN(pop) AS Population 
      FROM zipCodes
        GROUP BY state
         ) minp  
        ON  minp.state = t.state
        AND minp.Population = t.pop
        '''

    sql=sql1+" UNION ALL "+sql2
    cur.execute(sql);
    res='''<table class='table table-bordered table-hover'> 
            <tr><th>State</th>
                <th>City</th>
                <th>Population</th></tr>'''
    for row in cur:
        res+="<tr><td>"+str(row[0])+"</td><td>"+str(row[1])+"</td>"+"<td>"+str(row[2])+"</td></tr>"
    return res 

def query4():
    cur=__connect__()
    sql='''SELECT state, city From zipCodes where city='SPRINGFIELD' GROUP BY state'''
    cur.execute(sql)
    res='''<table class='table table-bordered table-hover'> 
            <tr><th>State</th>
                <th>City</th></tr>'''
    for row in cur:
        res+="<tr><td>"+str(row[0])+"</td><td>"+str(row[1])+"</td></tr>"
    return res


def empQuery1():
    cur=__connectEmps__()
    sql='''SELECT first_name,last_name,salary from salaries JOIN employees ON salaries.emp_no=employees.emp_no WHERE salaries.to_date='9999-01-01' ORDER BY salary DESC LIMIT 20'''
    cur.execute(sql)
    res='''<table class='table table-bordered table-hover'> 
            <tr><th>First Name</th>
                <th>Last Name </th>
                <th>Salary</th></tr>'''
    for row in cur:
        res+="<tr><td>"+str(row[0])+"</td><td>"+str(row[1])+"</td><td>"+str(row[2])+"</td></tr>"
    return res

def empQuery2():
    cur=__connectEmps__()
    sql='''select first_name,last_name,salary,dept_name from salaries join employees on salaries.emp_no=employees.emp_no join dept_emp on employees.emp_no=dept_emp.emp_no join departments on dept_emp.dept_no=departments.dept_no WHERE salaries.to_date='9999-01-01' AND departments.dept_name='Development' ORDER BY salaries.salary DESC LIMIT 10;'''
    cur.execute(sql)
    res='''<table class='table table-bordered table-hover'> 
            <tr><th>First Name</th>
                <th>Last Name </th>
                <th>Salary</th>
                <th>Department</th></tr>'''
    for row in cur:
        res+="<tr><td>"+str(row[0])+"</td><td>"+str(row[1])+"</td><td>"+str(row[2])+"</td><td>"+str(row[3])+"</td></tr>"
    return res


def empQuery3():
    cur=__connectEmps__()
    sql='''select first_name,last_name,birth_date from employees order by birth_date asc limit 10'''
    cur.execute(sql)
    res='''<table class='table table-bordered table-hover'> 
            <tr><th>First Name</th>
                <th>Last Name </th>
                <th>Birth Date</th></tr>'''
    for row in cur:
        res+="<tr><td>"+str(row[0])+"</td><td>"+str(row[1])+"</td><td>"+str(row[2])+"</td></tr>"
    return res


def empQuery4():
    cur=__connectEmps__()
    sql='''select first_name, last_name, salary, dept_name from departments join dept_manager on departments.dept_no=dept_manager.dept_no join employees on dept_manager.emp_no=employees.emp_no join salaries on employees.emp_no= salaries.emp_no where salaries.to_date='9999-01-01' order by salaries.salary desc limit 10'''
    cur.execute(sql)
    res='''<table class='table table-bordered table-hover'> 
            <tr><th>First Name</th>
                <th>Last Name </th>
                <th>Salary</th>
                <th>Department</th></tr>'''
    for row in cur:
        res+="<tr><td>"+str(row[0])+"</td><td>"+str(row[1])+"</td><td>"+str(row[2])+"</td><td>"+str(row[3])+"</td></tr>"
    return res

if __name__=="__main__":
   pp.pprint(empQuery1())
    
