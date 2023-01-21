from beanie import init_beanie
import motor.motor_asyncio
from celery import Celery
from celery.schedules import crontab
from server.utils import booking_helper
from server.models.booking_history import Booking
import asyncio


app = Celery()
app.config_from_object('server.settings.CONFIG_SETTINGS')


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
    db_name = client["evcapartment"]

    await init_beanie(database=db_name, document_models=[Booking])

    

    
async def async_function():
    # more async stuff...
    await init_db()
    booked_property = await Booking.find().to_list()
    for item in booked_property:
        if item.check_in_date == "monday1":
                new_check_in = await Booking.get(item.id)
                new_check_in.check_in_number = 1
                await new_check_in.save()  
                print("yes1")  
        if item.check_out_date == "friday1":
            new_check_out = await Booking.get(item.id)
            new_check_out.check_out_number = 1
            await new_check_out.save()
            print("yes2")
        
    
    


@app.task(name='tasks.add')
def add():
    # Does stuff but let's simplify it
    asyncio.run(async_function())
    
#Run with 
#celery -A tasks worker -B
