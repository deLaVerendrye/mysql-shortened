# mysql-shortened

Simple module to reduce that shortens the syntax of mysql-connector

## How to use

Clone or download the module and import it in your project

```
git clone https://github.com/studentOfYawn/mysql-shortened.git
```

Then install all dependencies listed in _requirements.txt_ file either using python virtual environments or not.

```
python -m pip install -r requirements.txt
```

If you already have the mysql-connector module, then there is no need to install requirements

## Create Connection

to create a connection to your database
you can use the Connection() Method

```
import mcsv

mydb = mcsv.Connection(
    host='localhost',
    user='root',
    password='',
)
```

** To check the connection you can use the CheckConnection() method
```
print(mydb.CheckConnection())
```
If the result is something like this:
```
<mysql.connector.connection.MySQLConnection object at 0x0000022CF330EF40>
```
It means you are connected

## Create Database
