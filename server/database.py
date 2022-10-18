import os
from dotenv import load_dotenv


from beanie import init_beanie
import motor.motor_asyncio

from server.sorries import Sorry

load_dotenv()
MONGODB_URI = os.environ['MONGODB_URI']

async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        MONGODB_URI
    )

    await init_beanie(database=client.sorryApp, document_models=[Sorry])

