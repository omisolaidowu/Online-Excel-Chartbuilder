from json import JSONEncoder

import json
import datetime

class DateTimeEncoder(JSONEncoder):
        #Override the default method
        def default(self, obj):
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()


# DateTimeEncoder().encode(employee)

# print("Encode DateTime Object into JSON using custom JSONEncoder")

# print(employeeJSONData)