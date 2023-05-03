import sqlite3
import os
import glob
import time

#"C:\\Users\\claypool\\Desktop\\v22.03.17\\results\\Experiment_anon_7ca34ee9-client-0008bad5fd176601.db"
def importdb():
    list_of_files = glob.glob("C:\\Users\\claypool\\Desktop\\v22.03.17\\results\\*")
    l = max(list_of_files, key=os.path.getctime)

    conn = sqlite3.connect(l)
    c = conn.cursor()
    output = c.execute("SELECT * FROM Client_Ping_Statistics;")
    #print(output)

    #for line in output.fetchall():
    #    print(line)
    print(output.fetchall()[-1])
    c.close()
    conn.close()

    #time.sleep(0.1)

while True:
    importdb()
