
#!/usr/bin/python
import MySQLdb
import time
import datetime

# Open database connection
db = MySQLdb.connect(host="localhost", user="root", passwd="devilsecret", db="day_time")

# Continuously append data
while(True):
	id = 20
	#date = time.strftime("%d/%m/%Y")
	day = time.strftime("%d")
	clock = time.strftime("%H:%M")


#setup cursor
	c = db.cursor()

#insert to table
	c.execute("INSERT INTO day_time (id, day, clock) VALUES (%s, %s, %s)",(id, day, clock))
	db.commit()

 #show table
	c.execute("SELECT id, day, clock FROM day_time")

##Iterate 
	#for row in c.fetchall() :
      #data from rows
    #day = str(row[0])
    #clock = str(row[1])

      #print 
      	#print "This Person's name is " + day + " " + clock

	print("Insert Success")
	time.sleep(1)

# close the connection
#db.close ()
