# factory.py

import openpyxl
import json
from dao.user_dao_mysql import UserDAOMySQL
from dao.user_dao_txt import UserDAOTxt
from dao.user_dao_xml import UserDAOXML
from dao.user_dao_mssql import UserDAOMSSQL
from dao.user_dao_excel import UserDAOExcel

def get_dao_from_config(config_path="config.json"):
    with open(config_path, "r") as f:
        config = json.load(f)

    dao_type = config["dao_type"].lower()

    if dao_type == "mysql":
        # ... (existing mysql implementation)
        mysql_conf = config["mysql"]
        return UserDAOMySQL(
            host=mysql_conf["host"],
            user=mysql_conf["user"],
            password=mysql_conf["password"],
            database=mysql_conf["database"],
            port=mysql_conf.get("port", 3306)
        )

    elif dao_type == "txt":
        # ... (existing txt implementation)
        txt_conf = config["txt"]
        return UserDAOTxt(txt_conf["filepath"])

    elif dao_type == "xml":
        # ... (existing xml implementation)
        xml_conf = config["xml"]
        return UserDAOXML(xml_conf["filepath"])
    
    elif dao_type == "mssql": 
        # ... (existing mssql implementation)
        mssql_conf = config["mssql"]
        return UserDAOMSSQL(
            host=mssql_conf["host"],
            user=mssql_conf["user"],
            password=mssql_conf["password"],
            database=mssql_conf["database"]
        )
    
    elif dao_type == "excel": # <-- NEW BLOCK
        excel_conf = config["excel"]
        return UserDAOExcel(excel_conf["filepath"])

    else:
        raise ValueError(f"Tipo de DAO desconocido: {dao_type}")
    
