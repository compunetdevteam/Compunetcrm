from decouple import config
from africastalking.AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException

# Specify your login credentials
username = config('AFRICAS_TALKING_API_USERNAME')
apikey = config('AFRICAS_TALKING_API_KEY')


def send_sms_api(to, message,fro=None):
    # Create a new instance of our awesome gateway class
    gateway = AfricasTalkingGateway(username, apikey)
    result = {}
    try:
        number = '+234' + to[1:]
        results = gateway.sendMessage(number, message, from_=fro)
        for recipient in results:
            result['number'] = recipient['number']
            result['status'] = recipient['status']
            result['messageId'] = recipient['messageId']
            result['cost'] = recipient['cost']
        return result
    except AfricasTalkingGatewayException as e:
        return e

