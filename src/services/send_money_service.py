from src.db.query import Query
from src.logger import logger
from src.db.transaction import Transaction
from src.services.User.user_services import get_user_details

async def send_money(sender_id, receiver_id, amount):
    sender, receiver = await get_user_details(sender_id),  await get_user_details(receiver_id)
    sender, receiver = dict(sender[0]), dict(receiver[0])
    # logger.info(sender.get('balance'), amount)
    if sender.get("balance") and  int(sender.get("balance"))<int(amount):
        return {
            "response": "Insuffiscient balance in the account"
        }

    newsenderbalance = str(int(sender.get("balance")) - int(amount))
    newreceiverbalance = str(int(receiver.get("balance")) + int(amount))

    transaction_list = [
        (Query.update_user_balance, (newsenderbalance, sender_id)),
        (Query.update_user_balance, (newreceiverbalance, receiver_id))
    ]
    transaction_obj = await Transaction.get_instance()
    transaction_success = await transaction_obj.perform_tansaction(transaction_list)
    if(transaction_success):
        return {
            "response": "success"
        }
    return {
            "response": "failed"
        }





