from app import sms_gateway, app
from AfricasTalkingGateway import AfricasTalkingGatewayException

"""
def send_mail(recipient):
	recipent = 'stvnkrs@gmail.com'#hard code for testing
	msg = Message('Hello', 
		sender = 'yourId@gmail.com', 
		recipients = [recipient])
	msg.body = "Hello Flask message sent from Flask-Mail"
	print (mail.send(msg))
"""

def send_sms(phone, msg):
	# Any gateway errors will be captured by our custom Exception class below, 
	# so wrap the call in a try-catch block
	try:
	    # Thats it, hit send and we'll take care of the rest.
	    
	    results = sms_gateway.sendMessage(phone, msg)
	    
	    for recipient in results:
	        # status is either "Success" or "error message"
	        print 'number=%s;status=%s;messageId=%s;cost=%s' % (recipient['number'],
	                                                            recipient['status'],
	                                                            recipient['messageId'],
	                                                            recipient['cost'])
	except AfricasTalkingGatewayException, e:
	    print 'Encountered an error while sending: %s' % str(e)