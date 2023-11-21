import cx_Oracle
conStr='system/carefree@localhost:1521/xepdb1'
#create a connection object
conn=cx_Oracle.connect(conStr)
#get a cursor object from the connection
cur = conn.cursor()

#insert table rows
sqlTxt='insert into "CEN434".STUDENT_INFO (MATNO, NAME, PROGRAMME, ROOMNO, AGE)  values (:1, :2, :3, :4, :5)'
cur.execute(sqlTxt,('20CF940202','Xavier Stalling','ENGLISH', 'B210', '16'))

#insert multiple rows
dataTuples=[('20CF940302','Idowu Eniola','ENGLISH', 'C210', '17'),('20CK940302','Towoju Joy','ICE', 'F408', '18'),('20BC940302','Odetola Faith','ENGLISH', 'B110', '21')]
sqlTxt='insert into "CEN434".STUDENT_INFO (MATNO, NAME, PROGRAMME, ROOMNO, AGE)  values (:1, :2, :3, :4, :5)'
cur.executemany(sqlTxt, dataTuples)

#update table rows
sqlTxt='update "CEN434".STUDENT_INFO set NAME=:1 where NAME=:2'
cur.execute(sqlTxt,("Oluwafemi Tireni","AJIBOLA STANLEY"))
#cur.execute executes the statement 
#name1 replaces name2 in the table

#delete a record
#def delete_student(MATNO, ROOMNO):
#sqlTxt='delete from "CEN434".STUDENT_INFO where MATNO=:1'
#cur.execute(sqlTxt,("20CF940302"))


conn.commit()
# call the Connection.commit() method to apply the changes to the database. If you forget to call the Connection.commit() method, you will see that the change will not take effect.
cur.close()
#close the cursor object to avoid memory leaks
conn.close()
#close the connection  object also