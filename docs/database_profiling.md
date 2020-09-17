# SQLAlchemy profiling
Slow database queries. Flask-SQLAlchemy has an option to record
statistics about database queries

```python
from flask_sqlalchemy import get_debug_queries

@main.after_app_request
def after_request(response):
    for query in get_debug_queries():
        if query.duration>=current_app.config['SLOW_DB_QUERY_THRESHOLD']:
            current_app.logger.warning('Slow query : %s\nParameters: %s\nDuration: %f\nContext:%s\n'%
            (query.statement,query.parameters,query.duration,query.context))
    return response           
```

Query statistics recorded by Flask-SQLAlchemy

<table>
  <tr>
    <td>statement</td>
    <td>The SQL statement</td>
  </tr>
  <tr>
    <td>parameters</td>
    <td>The parameters used with SQL statement</td>
  </tr>
  <tr>
    <td>start_time</td>
    <td>The time the query was issued</td>
  </tr>
  <tr>
    <td>end_time</td>
    <td>The time the query returned</td>
  </tr>
  <tr>
    <td>duration</td>
    <td>The duration of the query in seconds</td>
  </tr>
  <tr>
    <td>context</td>
    <td>A string that indicates the source code location where the query was issued</td>
  </tr>
</table>

To enable Flask-SQLAlchemy query statistics in production

```python
class Config:
    ....
    SQLALCHEMY_RECORD_QUERIES=True
    SLOW_DB_QUERY_THRESHOLD=0.5
```