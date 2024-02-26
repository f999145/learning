from sqlalchemy import text, select, insert, update
from database import engine
from models import metadata_obj



class SyncCore:
    @staticmethod
    def create_tables():
        metadata_obj.create_all(engine)

    @staticmethod
    def get_version():
        with engine.connect() as conn:
            res = conn.execute(text("Select @@version"))
            print(res.first())

    @staticmethod
    def get_col_type():
        with engine.connect() as conn:
            res = conn.execute(text("""
                                    SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH
                                    FROM INFORMATION_SCHEMA
                                    """))
            print(res.first())

    @staticmethod
    def view_table():
        with engine.connect() as conn:
            res = conn.execute(text("select * from workers"))
            print(res.all())

    # @staticmethod
    # def insert_workers():
    #     with engine.connect() as conn:
    #         stmt = insert(workers_table).values(
    #             [
    #                 {'username': 'Jack'},
    #                 {'username': 'Michael'},
    #             ]
    #         )
    #         conn.execute(stmt)
    #         conn.commit()

    # @staticmethod
    # def select_workers():
    #     with engine.connect() as conn:
    #         query = select(workers_table)
    #         result = conn.execute(query)
    #         workers = result.all()
    #         print(f'{workers=}')

    
    # @staticmethod
    # def update_worker(worker_id: int = 2, new_username: str = 'Misha'):
    #     with engine.connect() as conn:
    #         # stmt = text("UPDATE workers Set username=:username WHERE id=:id")
    #         # stmt = stmt.bindparams(username=new_username, id=worker_id)
    #         stmt = (
    #                 update(workers_table)
    #                 .values(username=new_username)
    #                 # .where(workers_table.c.id==worker_id)
    #                 .filter_by(id=worker_id)
    #                     )
    #         conn.execute(stmt)
    #         conn.commit()


            