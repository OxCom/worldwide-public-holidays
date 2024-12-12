# Worldwide public holidays
The small service to provide API on top of Python [holidays](https://github.com/vacanza/holidays) library

## Example
```bash
curl -D- "http://127.0.0.1:8123/holidays?country=DE&year=2025&state=Hessen"
HTTP/1.1 200 OK
Server: gunicorn
Date: Thu, 12 Dec 2024 08:04:53 GMT
Connection: keep-alive
Content-Type: application/json
Content-Length: 439

{
  "holidays":[
    {"date":"2025-01-01","name":"Neujahr"},
    {"date":"2025-04-18","name":"Karfreitag"},
    {"date":"2025-04-21","name":"Ostermontag"},
    {"date":"2025-05-01","name":"Erster Mai"},
    {"date":"2025-05-29","name":"Christi Himmelfahrt"},
    {"date":"2025-06-09","name":"Pfingstmontag"},
    {"date":"2025-10-03","name":"Tag der Deutschen Einheit"},
    {"date":"2025-12-25","name":"Erster Weihnachtstag"},
    {"date":"2025-12-26","name":"Zweiter Weihnachtstag"}
  ]
}
```