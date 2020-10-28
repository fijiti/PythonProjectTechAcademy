# Datetime challenge Step 260

from datetime import datetime
import pytz

UTC = pytz.utc
timeZ_Portland = pytz.timezone('America/Los_Angeles')
timeZ_Ny = pytz.timezone('America/New_York')
timeZ_London = pytz.timezone('Europe/London')

dt_Portland = datetime.now(timeZ_Portland)
dt_Ny = datetime.now(timeZ_Ny)
dt_London = datetime.now(timeZ_London)

utc_Portland = dt_Portland.astimezone(UTC)
utc_Ny = dt_Ny.astimezone(UTC)
utc_London = dt_London.astimezone(UTC)

##print("UTC Format \t\t\t IST Format")
##print(utc_Portland.strftime('%Y-%m-%d %H:%M:%S %Z %z'), dt_Portland.strftime('%Y-%m-%d %H:%M:%S %Z %z'))
##print(utc_Ny.strftime('%Y-%m-%d %H:%M:%S %Z %z'), dt_Ny.strftime('%Y-%m-%d %H:%M:%S %Z %z'))
##print(utc_London.strftime('%Y-%m-%d %H:%M:%S %Z %z'), dt_London.strftime('%Y-%m-%d %H:%M:%S %Z %z'))


print("Time now in Portland, Oregon:", dt_Portland.strftime('%I:%M %p'))
if int(dt_Portland.strftime('%H')) >= 9 and int(dt_Portland.strftime('%H')) <= 17:
    print("Portland Branch is open!")
else:
    print("Portland Branch is closed! It is open 9AM to 5PM Portland time.")

print("\nTime now in New York:", dt_Ny.strftime('%I:%M %p'))
if int(dt_Ny.strftime('%H')) >= 9 and int(dt_Ny.strftime('%H')) <= 17:
    print("New York Branch is open!")
else:
    print("New York Branch is closed! It is open 9AM to 5PM New York time.")

print("\nTime now in London:", dt_London.strftime('%I:%M %p'))
if int(dt_London.strftime('%H')) >= 9 and int(dt_London.strftime('%H')) <= 17:
    print("London Branch is open!")
else:
    print("London Branch is closed! It is open 9AM to 5PM London time.")
