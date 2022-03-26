# mysql-shortened


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
you can use the Connection() function

```
import mcsv as mysql

mydb = mysql.Connection(
    host='localhost',
    user='root',
    password='',
)
```

**To check the connection you can use the CheckConnection() function**
```
print(mydb.CheckConnection())
```
If the result is something like this:
```
<mysql.connector.connection.MySQLConnection object at 0x0000022CF330EF40>
```
It means you are connected


## Queries
To make queries to the database, you can use the query() function
```
import mcsv as mysql

mydb = mysql.Connection(
    host='localhost',
    user='root',
    password='',
    Database='mydatabasee'
)

query = mydb.query('SELECT * FROM users')

print(query)

```
**When you use SELECT in query() it will return the results, If you are using it to INSERT or CREATE it will return 0 if successful**

## queryMultiple
The queryMultiple() method can be use to INSERT multiple data at once
```
mydb = mysql.Connection(
    host='localhost',
    user='root',
    password='',
    Database='mydatabasee'
)

query = mydb.queryMultiple(
    'INSERT INTO users (name, adress) VALUES (%s, %s)',
    [
        ('John', 'HIGHWAY 21'),
        ('William', 'Central st 954'),
        ('Betty', 'Green Grass 1')
    ]
    )

print(query)
```
