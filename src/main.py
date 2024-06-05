from fastapi import FastAPI
from src.routes.transaction_routes.sendmoney import send_money_router
from src.routes.user_routes.userroutes import user_router
from src.logger import logger
from src.db.connect import Database

# Create an instance of FastAPI
app = FastAPI()

app.include_router(send_money_router, prefix = "/send_money")
app.include_router(user_router)

# Define a route
@app.post("/health")
async def read_root():
    return {"message": "App is reachable"}

# Event handler to connect to the database when the application starts
@app.on_event("startup")
async def startup_db_client():
    logger.info("connecting to the db")
    await Database.get_instance()
    logger.info("connected to the db")

# Event handler to disconnect from the get_connection(connection_string) when the application stops
@app.on_event("shutdown")
async def shutdown_db_client():
    await get_connection(DATABASE_URL).disconnect()
