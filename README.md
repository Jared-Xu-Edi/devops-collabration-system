# DevOps request web portal

## App running
run app:
```
python app.py
```

## App Access
127.0.0.1:5000

## DB Init/Migration
If you create a new DB, run
```
flask db init
```
If you change something in Model, run
```
flask db migrate -m "your comments"
```
and
```
flask db upgrade
```