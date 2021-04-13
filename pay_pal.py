import paypalrestsdk
from paypalrestsdk import Payment

paypalrestsdk.configure({
  'mode': 'sandbox', #sandbox or live
  'client_id': 'AS-H-1HZOPZOYRUNC5dlHsrzIaA02Tp6DBa1FT95qvwfurmJgLa3VIz9yZwy3LGuUecTn0tP-GbeDmqf',
  'client_secret': 'EJJ6gBtbnU265SCMrlTwRqeE5j-YK5wcku7A7K3l-Rq1qZ-ytcBpeTTT9euyoc4T0KNILanGffOAFG2k' })
business = { 'mode':'sandbox',
'client_id': 'AS-H-1HZOPZOYRUNC5dlHsrzIaA02Tp6DBa1FT95qvwfurmJgLa3VIz9yZwy3LGuUecTn0tP-GbeDmqf', 
'client_secret' : 'EJJ6gBtbnU265SCMrlTwRqeE5j-YK5wcku7A7K3l-Rq1qZ-ytcBpeTTT9euyoc4T0KNILanGffOAFG2'
} 
# Create payment object
payment = Payment({
  "intent": "sale",

  # Set payment method
  "payer": {
    "payment_method": "paypal"
  },

  # Set redirect URLs
  "redirect_urls": {
    "return_url": "http://localhost:3000/process",
    "cancel_url": "http://localhost:3000/cancel"
  },

  # Set transaction object
  "transactions": [{
    "amount": {
      "total": "10.00",
      "currency": "USD"
    },
    "description": "test"
  }]
})

print(payment)
print(payment.create())
if payment.create():
  # Extract redirect url
  for link in payment.links:
    if link.method == "REDIRECT":
      # Capture redirect url
      print('redirect')
      redirect_url = payment.redirect_urls.return_url
      print(redirect_url)

      # Redirect the customer to redirect_url
else:
  print("Error while creating payment:")
  print(payment.error)


# Payment ID obtained when creating the payment (following redirect)
payment = Payment.find("PAY-28103131SP722473WKFD7VGQ")

# Execute payment with the payer ID from the create payment call (following redirect)
if payment.execute({"payer_id": "DUFRQ8GWYMJXC"}):
  print("Payment[%s] execute successfully" % (payment.id))
else:
  print(payment.error)