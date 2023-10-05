from yoomoney import Client

token = "410012025117208.08C28F3D0A7311BD7665C722818F43EF0DF7BB7C3A552D7994A31B954C10BE7C12F61EC916DDFB751FBE9DA37C48C506964D30DAF428D94B52D8BCFF60AEB647BB73081B47A55A5679F631F5ACD181892D7F722CC130899818BFD8339E662F4E82C4E89BCA96B6FFDDA0FA8883F6024F3377763D19B1F86C457D09F009E5090B"

client = Client(token)

details = client.operation_details(operation_id="749546408458358088")

properties = [i for i in details.__dict__.keys() if i[:1] != '_']

max_size = len(max(properties, key=len))

for prop in properties:
    print(prop, " " * (max_size - len(prop)), "-->", str(details.__getattribute__(prop)).replace('\n', ' '))