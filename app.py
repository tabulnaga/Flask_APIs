from flask import Flask
import requests
import json
import cx_Oracle
from pandas.io import sql


app = Flask(__name__)

conn = cx_Oracle.connect('TAREK/tarek@196.204.234.29:1521/TABS',threaded=True)
subcur = conn.cursor()
cur = conn.cursor()



def PrepareData ():
    
    L_sSelect ="""
    Select * from EMP_LOG
    """
       
       
    Subsdatadf = sql.read_sql(L_sSelect,con=conn) 
        
        
    return Subsdatadf    

@app.route('/GetEmp/<string:id>')
def GetEmp(id):
    Subsdf=PrepareData()
    json_dict=Subsdf.reset_index().to_json(orient='records')
    L_sSubParamJson = json.loads(json_dict)
    #print (L_sSubParamJson)
    return L_sSubParamJson

    

if __name__ == '__main__':
  app.run(port=5000,debug=True)