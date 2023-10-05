from yoomoney import Authorize

Authorize(
    client_id="75D0F16AD87E6C6C497DE152DCF15965D1CFC8FD73C3244A411E5EC7ABBA65DB",
    redirect_uri="https://uniqvpn.com/ru/success/",
    scope=["account-info",
           "operation-history",
           "operation-details",
           "incoming-transfers",
           "payment-p2p",
           "payment-shop",
           ]
          )
