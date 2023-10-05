from yoomoney import Client

token = "410012025117208.08C28F3D0A7311BD7665C722818F43EF0DF7BB7C3A552D7994A31B954C10BE7C12F61EC916DDFB751FBE9DA37C48C506964D30DAF428D94B52D8BCFF60AEB647BB73081B47A55A5679F631F5ACD181892D7F722CC130899818BFD8339E662F4E82C4E89BCA96B6FFDDA0FA8883F6024F3377763D19B1F86C457D09F009E5090B"

client = Client(token)

user = client.account_info()

print("Account number:", user.account)
print("Account balance:", user.balance)
print("Account currency code in ISO 4217 format:", user.currency)
print("Account status:", user.account_status)
print("Account type:", user.account_type)

print("Extended balance information:")
for pair in vars(user.balance_details):
    print("\t-->", pair, ":", vars(user.balance_details).get(pair))

print("Information about linked bank cards:")
cards = user.cards_linked

if len(cards) != 0:
    for card in cards:
        print(card.pan_fragment, " - ", card.type)
else:
    print("No card is linked to the account")
