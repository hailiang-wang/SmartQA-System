
from pandasql import sqldf, load_meat, load_births
import pandasql import *


pysqldf = lambda q: sqldf(q, globals())
meat = load_meat()
births = load_births()
print pysqldf("SELECT * FROM meat LIMIT 10;").head()