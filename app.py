from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)






@app.route('/')
def mine():
    conn = sqlite3.connect('swissdb.db')
    cursor = conn.cursor()
    print("Opened database successfully")
    groupByStatus = "SELECT DISTINCT Status,COUNT(Status) from parts group by Status"
    groupByEngineer ="SELECT count(PartName), CreatedBy FROM parts,Enginner on parts.Engineerid=Enginner.Engineerid GROUP BY CreatedBy"
    groupByApprover="SELECT count(parts.PartName),Approver.Approver FROM parts INNER JOIN Approver ON parts.Approverid=Approver.Approverid GROUP by Approver"
    #groupByApprover1AndStatus="SELECT COUNT(field2),field2 from (SELECT field2,field5 from db where field5= 'Engineeer 1') group by field2";

    statusList=["approved","underQuery","Draft","inprogress"]
    groupByStatusData =[]
    groupByEngineerData = []
    groupByApproverData=[]
    topeng=["Engineer1","Engineer2","Engineer3","Engineer4","Engineer5"]
    groupByApprover1AndStatusData={}
    for row, n, in cursor.execute(groupByStatus):
        groupByStatusData.append(n)

    for row, n, in cursor.execute(groupByEngineer):
       groupByEngineerData.append(row)



    for n, row in cursor.execute(groupByApprover):
        groupByApproverData.append(n)

    #for  row, n, in cursor.execute(groupByApprover1AndStatus):
        #groupByApprover1AndStatusData.update({n:row})









    topEngineer = [x for y, x in sorted(zip(groupByEngineerData, topeng)  ) ]
    highestStatus=sorted(groupByStatusData,reverse=True)[0];

    #i=0
    #for i in range(0,len(groupByStatusData)-1):
       # if groupByStatusData[i] == highestStatus:
        #    part=statusList[i]
         #   break

    return render_template('index.html', groupByStatusData=groupByStatusData,groupByEngineerData=groupByEngineerData,groupByApproverData=groupByApproverData,groupByApprover1AndStatusData=groupByApprover1AndStatusData,highestStatus=highestStatus,topEngineer=topEngineer)



if __name__ == '__main__':
    mine()
