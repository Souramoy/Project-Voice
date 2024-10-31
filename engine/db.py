import sqlite3
#connecting the data base 
conn = sqlite3.connect("glass.db")

cursor = conn.cursor()

#create the sys_command table 
query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

#insert elements in the table like name and path of the programs i want to open via glass 

# query = "INSERT INTO sys_command VALUES (null,'one note','C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.exe')"

# cursor.execute(query)
# conn.commit()

#creating the web_command table

query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

#insert web elements 
query = "INSERT INTO web_command VALUES (null,'amazon', 'https://www.amazon.in/?&ext_vrnc=hi&adgrpid=58355126069&hvpone=&hvptwo=&hvadid=486458712209&hvpos=&hvnetw=g&hvrand=13868695527380959186&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=20472&hvtargid=kwd-10573980&hydadcr=14453_2154373')"
cursor.execute(query)
conn.commit()