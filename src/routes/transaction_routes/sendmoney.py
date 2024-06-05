from fastapi import APIRouter, FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from src.exceptions.exception_decorators import handle_exceptions_decorator
from src.logger import logger
from src.db.connect import Database
from src.models.money_transfer_model import MoneyTranferModel
from src.services.send_money_service import send_money

send_money_router: APIRouter = APIRouter()


@send_money_router.post("/")
@handle_exceptions_decorator
async def send_money_route(
    transferparams: MoneyTranferModel
):
    return await send_money(transferparams.sender_id, transferparams.receiver_id, transferparams.amount)

