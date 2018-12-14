""" Credits:
    CODE LAGOS 5.0
    https://www.cdc.gov/diseasesconditions/az/a.html
    MR. ABAYOMI PYTHON FACILITATOR IKD.
    COLLEGUE CODE LAGOS 5.0
    ANU CODE LAGOS 5.0
    I AM OLATOYE SEGUN SAMUEL
"""
import pymysql
connection = pymysql.connect(host = 'localhost', user = 'root', password = '', database = 'medics')
a = connection.cursor()


print("THIS PROGRAM IS USED TO ASSISTING IN PREDICTING A SICKNESS THROUGH THE SYMPTOMS AND PROVIDE AN HANDY CURE. YOU ARE TO SEARCH BY SYMPTOMS, SICKNESS OR CURE")
print("Search by (a). Symptoms (b). Cure (c). Sickness (d). All")
criteria = input()
if(criteria.lower() == "d" or criteria.lower() == "all"):
    #FETCH DATA BY CRITERIA FROM DATA BASE BY SUPPLYING WHAT TO SEARCH USING ARRAY
    sql = 'SELECT sickness from `medic_table`;'
    a.execute(sql)
    countrow = a.execute(sql)
    print("Number of rows :", countrow)
    data = a.fetchall()
    print(data)
    
    #for row in data:
        #print "%s, %s" % (row[cure], row[sickness], row[symptoms])
    
    
    
