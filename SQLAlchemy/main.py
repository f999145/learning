from queries.orm import SyncOrm
from queries.core import SyncCore
from database import engine
from models import MagnitCategory
import pandas as pd

# SyncOrm.create_tables([MagnitCategory.__table__])
# SyncOrm.insert_workers()

# SyncOrm.update_worker()
# SyncOrm.select_workers()

# df = pd.read_parquet('data/id_categories.gzip').convert_dtypes()

# df.to_sql(name='magnit_category', con=engine, if_exists='append', index=False, chunksize=20_000)

print(pd.read_sql_query(SyncOrm.select_magnit_category(), con=engine))
