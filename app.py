import sys
from config import DB_DETAILS

def main():
    """Program takes at least one argument"""
    env = sys.argv[1] #Provide the app.py file location
    dbDetails = DB_DETAILS[env]
    print(dbDetails)

if __name__ == '__main__':
    main()