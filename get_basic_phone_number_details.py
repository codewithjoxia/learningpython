## Get Basic Phone Number Details

## pip install phonenumbers
import phonenumbers
from phonenumbers import carrier, geocoder, timezone

phone_number = input("Enter your phone number in international format: ")

phone_number_details = phonenumbers.parse(phone_number)

time_zone = timezone.time_zones_for_number(phone_number_details)

carrier_ = carrier.name_for_number(phone_number_details, 'en')
region_ = geocoder.description_for_number(phone_number_details, 'en')


print ("Phone Number: " + phone_number)
print ("Timezone: " + str(time_zone))
print ("Carrier: " + carrier_)
print ("Region: " + region_)


#follow insta/@codewithjoxia
