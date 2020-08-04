class Global_settings():

    #Bases de datos
    DB_DRIVER = "DRIVER={PostgreSQL Unicode};"
    DB_HOST = "192.168.1.106"
    DB_PORT = "5432"
    DB_USER = "PAP"
    DB_PASS = "PRIME"
    DB_DATABASE_MS = "DB_PAP_MS"
    DB_DATABASE_PS = "DB_PAP_PS"


    url_ = "http://192.168.1.105:5003/orchestrator/topology"
    url_base = "http://192.168.1.105:4200/home"
    #http://192.168.1.105:4200/home/external-system

    headers_ = {
        "Transaction-Id": "718df8f8-64d9-43fa-8cf7-4af2232387PC",
        "User-Id": "qa",
        "Owner": "PAP",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
