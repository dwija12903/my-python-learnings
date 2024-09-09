# using sql lite
# we want to create a application where we have employees and want to update and delete employees from database
import sqlite3
from employee import Employee 

# conn = sqlite3.connect('employee.db') 
conn = sqlite3.connect(':memory:')
# above method starts from fresh start with db, using this is the best 
#connect methods creates file if it does not exists or else connect the file if it exists

# cursor is created to execute sql commands
c = conn.cursor()

# once table is created we can execute the command again as it wills how error that table already exists
c.execute("""CREATE TABLE employees (
          first text,
          last text,
          pay integer
          ) """) 

c.execute("INSERT INTO employees VALUES ('krishiv','panchal',70000)")
c.execute("SELECT * FROM employees WHERE last='panchal'")
print(c.fetchone()) #gives only one result
print(c.fetchmany(5)) #gives 5 result or else none in list 
print(c.fetchall()) #return all the remaining rows after cursor or else empty list

def insert_emp(emp):
    with conn: #from this we are using context manager and we dont need to commit it 
        c.execute("INSERT INTO employees VALUES (:first,:last,:pay)",{'first':emp.first,'last':emp.last,'pay':emp.pay})
def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last",{'last': lastname})
    return c.fetchall()
def update_pay(emp,pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})
def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})


emp_1=Employee('John','Doe',80000)
emp_2=Employee('Jane','Doe',90000)
print(emp_1.first) #it is printed simply
# ways to print variables into string, execute things
c.execute("INSERT INTO employees VALUES(?,?,?)",(emp_1.first,emp_1.last,emp_1.pay))
conn.commit()
c.execute("INSERT INTO employees VALUES(:a,:b,:c)",{'a': emp_2.first,'b':emp_2.last,'c':emp_2.pay})
conn.commit()

c.execute("select * from employees where last=?",('panchal',))
print(c.fetchall())
c.execute("select * from employees where last= :last",{'last': 'Doe'})
print(c.fetchall())

update_pay(emp_2,952000)
remove_emp(emp_1)
emps=get_emps_by_name('Doe')
print(emps)

conn.commit()
conn.close()