import mongoengine as me
import time
import os
import pymongo as pm


def connect_db(db_name):

    start_time = time.time()
    uri = os.environ.get('MONGODB_URI')
    if uri is None:
        raise RuntimeError("MONGODB_URI not found in environment.")

    me.connect(host=uri, db=db_name)
    client = pm.MongoClient(os.environ.get('MONGODB_URI'))
    db = client[db_name]

    print(f"Connected to database \"{db_name}\" in {time.time() - start_time} seconds.")
    return db

class Database:
    def __init__(self, db_name):
        self.db = connect_db(db_name)

    def run_migrations(self):
        """
        This is run every time the bot starts.
        """

        # find the database version
        try:
            version = DbSettings.objects.get().database_version
        except me.DoesNotExist:
            setting = DbSettings(database_version=1)
            setting.save()
            version = 0

        # run migrations
        if version == 0:
            self.v1()
            version = 1

        if version == 1:
            self.v2()
            version = 2

        print("Ran migrations.")

    def v1(self):
        DbSettings.objects.get().update(database_version=1)

    def v2(self):
        self.db["users"].update_many({}, {"$set": {"name":None}})
        self.db["resumes"].update_many({}, {"$set": {"user":None}})
        DbSettings.objects.get().update(database_version=2)


class User(me.Document):

    name = me.StringField(required=True, primary_key=True)

    meta = {'collection': 'users'}


class Resume(me.Document):

    content = me.StringField()
    user = me.ReferenceField(User, reverse_delete_rule=me.CASCADE)

    meta = {'collection': 'resumes'}


class JobPosting(me.Document):

    description = me.StringField(required=True)
    user = me.ReferenceField(User, reverse_delete_rule=me.CASCADE)

    meta = {'collection': 'job_postings'}







class DbSettings(me.Document):
    database_version = me.IntField()

    meta = {
        'collection': 'db_settings',
        'max_documents': 1,
    }


