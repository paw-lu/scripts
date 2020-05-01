"""How to query Snowflake given that it lives in https://companyname.snowflakecomputing.com/."""
import os

import pandas as pd
import snowflake.connector

with snowflake.connector.connect(
    provider="snowflake",
    user=os.environ["SNOWFLAKE_USERNAME"],
    password=os.environ["SNOWFLAKE_PASSWORD"],
    database="database_name",
    account="companyname",
) as ctx:
    print(pd.read_sql("SELECT current_version()", con=ctx))
