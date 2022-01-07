# DevOps Request Web Portal

This is a Web App which logs all cases/requests created by user in a table view where you can search, sort etc.
There different role in the system which can update the status of these cases/requests in turn.
It's created in the purpose of boosting the collabration between dev and ops, or dev and devops, tracking the unplanned work etc.

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
