from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)



@app.route('/')
def mine():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    print("Opened database successfully")
    groupByStatus = "SELECT DISTINCT field2,COUNT(field2) from db group by field2"
    groupByEngineer ="SELECT DISTINCT field5,COUNT(field5) from db group by field5"
    groupByApprover="SELECT DISTINCT field6,COUNT(field6) from db group by field6"
    groupByApprover1AndStatus="SELECT COUNT(field2),field2 from (SELECT field2,field5 from db where field5= 'Engineeer 1') group by field2";

    statusList=["approved","underQuery","Draft","inprogress"]
    groupByStatusData =[]
    groupByEngineerData = []
    groupByApproverData=[]
    topeng=["Engineer1","Engineer2","Engineer3","Engineer4","Engineer5"]
    groupByApprover1AndStatusData={}
    for row, n, in cursor.execute(groupByStatus):
        groupByStatusData.append(n)

    for row, n, in cursor.execute(groupByEngineer):
        groupByEngineerData.append(n)


    for n, row in cursor.execute(groupByApprover):
        groupByApproverData.append(row)

    for  row, n, in cursor.execute(groupByApprover1AndStatus):
        groupByApprover1AndStatusData.update({n:row})





    groupByApproverData.remove(groupByApproverData[0])
    groupByEngineerData.remove(groupByEngineerData[0])
    groupByStatusData.remove(groupByStatusData[3])
    print(groupByEngineerData)

    Z = [x for y, x in sorted(zip(groupByEngineerData, topeng)  ) ]
    print(Z)
    highestStatus=sorted(groupByStatusData,reverse=True)[0];
    print(highestStatus)

    i=0
    for i in range(0,len(groupByStatusData)-1):
        if groupByStatusData[i] == highestStatus:
            part=statusList[i]
            break

    return render_template('index.html', groupByStatusData=groupByStatusData,groupByEngineerData=groupByEngineerData,groupByApproverData=groupByApproverData,groupByApprover1AndStatusData=groupByApprover1AndStatusData,highestStatus=highestStatus,part=part,Z=Z)



if __name__ == '__main__':
    mine()
