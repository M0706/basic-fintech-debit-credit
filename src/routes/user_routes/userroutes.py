import json
from fastapi import APIRouter
from src.logger import logger
from src.db.connect import Database
from src.models.user_model import UserIdModel
from src.services.User.user_services import get_user_details, get_all_users
from src.exceptions.exception_decorators import handle_exceptions_decorator

user_router: APIRouter = APIRouter()


@user_router.post("/getuserdetails")
@handle_exceptions_decorator
async def get_user(
    params: UserIdModel
):
    logger.info("reached user route")
    user_id = params.user_id
    return await get_user_details(user_id)

@user_router.post("/get_all_users")
@handle_exceptions_decorator
async def get_user():
    return await get_all_users()

