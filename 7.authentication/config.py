db = {
    'user'     : 'root',
    'password' : 'test1234',
    'host'     : 'localhost',
    'port'     : 3306,
    'database' : 'miniter'
}

DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"
JWT_SECRET_KEY = 'N0_hack'
