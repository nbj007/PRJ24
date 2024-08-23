import sqlite3
conn=sqlite3.connect("HospitalDB.db")

print("DATABASE CONNECTION SUCCESSFUL")

print("PATIENT TABLE CREATED SUCCESSFULLY")         

print("CONTACT_NO TABLE CREATED SUCCESSFULLY")

print("EMPLOYEE TABLE CREATED SUCCESSFULLY")

print("TREATMENT TABLE CREATED SUCCESSFULLY")

print("MEDICINE TABLE CREATED SUCCESSFULLY")


print("ROOM TABLE CREATED SUCCESSFULLY")

conn.execute("Drop table if EXISTS APPOINTMENT")
c = conn.cursor()
c.execute("""create table appointment
            (
             PATIENT_ID int(20) not null,
             EMP_ID varchar(10) not null,
             AP_NO varchar(10) primary key,
             AP_TIME time,
             AP_DATE date,
             description varchar(100),
             FOREIGN KEY(PATIENT_ID) references PATIENT(PATIENT_ID),
             FOREIGN KEY(EMP_ID) references employee(EMP_ID));""")
print("APPOINTMENT TABLE CREATED SUCCESSFULLY")
conn.commit()
conn.close()
