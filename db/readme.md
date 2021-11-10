Please install:
`pip install mysql-connector-python`

To insert data to database paste the following codes (please take the all data in `list_of_data` variable):

```
from data_to_db import TODatabase
query = TODatabase(list_of_data)
query.insert_data()
```