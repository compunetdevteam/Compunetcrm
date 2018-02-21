from decouple import config
from africastalking.AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException

# Specify your login credentials
username = config('AFRICAS_TALKING_API_USERNAME')
apikey = config('AFRICAS_TALKING_API_KEY')

# Please ensure you include the country code (+254 for Kenya in this case)
to = "+2348069324666"

message = "Just Testingv STuffs OUt For Compunet"

# Create a new instance of our awesome gateway class
gateway = AfricasTalkingGateway(username, apikey)

try:
    # Thats it, hit send and we'll take care of the rest.

    results = gateway.sendMessage(to, message)
    for recipient in results:
        print('number={0};status={1};messageId={2};cost={3}'.format(recipient['number'], recipient['status'],
              recipient['messageId'], recipient['cost']))
except AfricasTalkingGatewayException as e:
    print('Encountered an error while sending: {0}'.format(e))
