from src.db.connect import Database
from src.db.query import Query
from src.logger import logger
import json
from src.db.transaction import Transaction

async def get_user_details(user_id):
    db_instance = await Database.get_instance()
    user = await db_instance.fetch(Query.user_select_query, user_id)
    return user


async def get_all_users():
    db_instance = await Database.get_instance()
    users_list = await db_instance.fetch(Query.get_all_users_query)
    return users_list
