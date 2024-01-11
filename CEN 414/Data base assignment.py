import cx_Oracle

conStr = 'system/carefree@localhost:1521/xepdb1'

# Create a connection object
conn = cx_Oracle.connect(conStr)

# Get a cursor object from the connection
cur = conn.cursor()

# Insert table rows
sqlTxt = 'insert into "CEN434".STUDENT_INFO (MATNO, NAME, PROGRAMME, ROOMNO, AGE) values (:1, :2, :3, :4, :5)'
cur.execute(sqlTxt, ('20CF940202', 'Xavier Stalling', 'ENGLISH', 'B210', '16'))

# Insert multiple rows
dataTuples = [
    ('20CF940302', 'Idowu Eniola', 'ENGLISH', 'C210', '17'),
    ('20CK940302', 'Towoju Joy', 'ICE', 'F408', '18'),
    ('20BC940302', 'Odetola Faith', 'ENGLISH', 'B110', '21')
]
cur.executemany(sqlTxt, dataTuples)

# Update table rows
sqlTxt = 'update "CEN434".STUDENT_INFO set NAME=:1 where NAME=:2'
cur.execute(sqlTxt, ("Oluwafemi Tireni", "AJIBOLA STANLEY"))

# Delete a record
# Uncomment this section if you want to use it and replace the placeholder with the correct value
# sqlTxt = 'delete from "CEN434".STUDENT_INFO where MATNO=:1'
# cur.execute(sqlTxt, ('20CF940302',))

conn.commit()
# Call the Connection.commit() method to apply the changes to the database.

cur.close()
# Close the cursor object to avoid memory leaks

conn.close()
# Close the connection object as well
