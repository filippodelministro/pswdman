
def create_database():
    query = '''
    CREATE TABLE IF NOT EXISTS passwords (
        id INTEGER PRIMARY KEY,
        nameservice TEXT NOT NULL,
        password TEXT NOT NULL
    );
    '''
    return query

def print_all(name):
    query = "select * from {name}"

    return query