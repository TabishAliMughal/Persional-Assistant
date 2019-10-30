import sqlite3
def Data():
    con=sqlite3.connect("AllData.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Data (id INTEGER PRIMARY KEY,MainGoal text,SubGoal text,Task text,User text,StartingDate text,EndDate text)")
    con.commit()
    con.close()
def AddRecord(MainGoal,SubGoal,Task,User,StartingDate,EndDate):
    con=sqlite3.connect("AllData.db")
    cur=con.cursor()
    cur.execute("INSERT INTO Data VALUES(NULL,?,?,?,?,?,?)",(MainGoal,SubGoal,Task,User,StartingDate,EndDate))
    con.commit()
    con.close()
def ViewData():
    con=sqlite3.connect("AllData.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM Data")
    rows=cur.fetchall()
    con.close()
    return rows
def DeleteData(id):
    con=sqlite3.connect("AllData.db")
    cur=con.cursor()
    cur.execute("DELETE FROM Data WHERE id=?",(id,))
    con.commit()
    con.close()
def SearchData(MainGoal="",SubGoal="",Task="",User="",StartingDate="",EndDate=""):
    con=sqlite3.connect("AllData.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM Data WHERE Maingoal=? OR SubGoal=? OR Task=? OR User=? OR StartingDate=? OR EndDate=? ",(MainGoal,SubGoal,Task,User,StartingDate,EndDate))
    rows=cur.fetchall()
    con.close()
    return rows
def UpdateData(id,MainGoal="",SubGoal="",Task="",User="",StartingDate="",EndDate=""):
    con=sqlite3.connect("AllData.db")
    cur=con.cursor()
    cur.execute("UPDATE Data SET Maingoal=?,SubGoal=?,Task=?,User=?,StartingDate?,EndDate?,WHERE id=?",(MainGoal,SubGoal,Task,User,StartingDate,EndDate,id))
    con.commit()
    con.close()





Data()