   

from huey import SqliteHuey
from huey import crontab


huey = SqliteHuey(filename='/tmp/demo.db')


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


@huey.periodic_task(crontab(minute='*/1'))
def add():
    asyncio.run(async_function())
    print('This task runs every one minutes')
  


#Run with 
#huey_consumer.py tasks.huey
