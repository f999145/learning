from database import engine, sync_session
from models import metadata_obj, WorkersOrm, ResumesOrm, Base, Workload, MagnitCategory
from sqlalchemy import select, func


class SyncOrm:
    @staticmethod
    def create_tables(tables: list|None):
        engine.echo=False
        Base.metadata.drop_all(engine, tables=tables)
        Base.metadata.create_all(engine, tables=tables)
        engine.echo=True

    @staticmethod
    def insert_workers():
        worker_bobr = WorkersOrm(username='Bobr')
        worker_volk = WorkersOrm(username='Volk')
        with sync_session() as sess:
            sess.add_all([worker_bobr, worker_volk])
            sess.commit()


    @staticmethod
    def select_workers():
        with sync_session() as session:
            # один работник
            # worker_id = 1
            # worker_jack = session.get(WorkersOrm, worker_id)
            # worker_jack = session.get(WorkersOrm, {'id':worker_id})
            query = select(WorkersOrm)
            result = session.execute(query)
            # workers = result.all()
            workers = result.scalars().all()
            print(f'{workers=}')
            

    
    @staticmethod
    def update_worker(worker_id: int = 2, new_username: str = 'Misha'):
        with sync_session() as session:
            worker_michael = session.get(WorkersOrm, worker_id)
            worker_michael.username = new_username
            session.commit()



    @staticmethod
    def insert_resumes():
        with sync_session() as session:
            resume_jack_1 = ResumesOrm(
                title="Python Junior Developer", compensation=50000, workload=Workload.fulltime, worker_id=1)
            resume_jack_2 = ResumesOrm(
                title="Python Разработчик", compensation=150000, workload=Workload.fulltime, worker_id=1)
            resume_michael_1 = ResumesOrm(
                title="Python Data Engineer", compensation=250000, workload=Workload.parttime, worker_id=2)
            resume_michael_2 = ResumesOrm(
                title="Data Scientist", compensation=300000, workload=Workload.fulltime, worker_id=2)
            session.add_all([resume_jack_1, resume_jack_2, 
                             resume_michael_1, resume_michael_2])
            session.commit()

    @staticmethod
    def select_magnit_category():
        with sync_session() as session:
            query = (
                select(MagnitCategory)
                .limit(10)
            )
            # result = session.execute(query)
            return query
            