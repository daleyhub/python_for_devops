# Passing secrets as environment variables.
# In order to hide a secret, such as password/apitoken, 
# on the CLI use export password="dele" or  export apitoken="awadakerikeri"
# where 'dele' and 'awadakerkeri' are the password and apitoken respectively
# and then use import os ('os' i the python module used to read env vars) 
# and print(os.getenv("apitoken")) or 
# print(os.getenv(password)) to call and pass it.

import os

password = os.getenv("password")
print(password)

apitoken = os.getenv("apitoken")
print(apitoken)