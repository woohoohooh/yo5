from yoomoney import Client
from a.hello.models import Customers

token = "410012025117208.08C28F3D0A7311BD7665C722818F43EF0DF7BB7C3A552D7994A31B954C10BE7C12F61EC916DDFB751FBE9DA37C48C506964D30DAF428D94B52D8BCFF60AEB647BB73081B47A55A5679F631F5ACD181892D7F722CC130899818BFD8339E662F4E82C4E89BCA96B6FFDDA0FA8883F6024F3377763D19B1F86C457D09F009E5090B"

client = Client(token)

history = client.operation_history()

print("List of operations:")
print("Next page starts with: ", history.next_record)

def check():
    for operation in history.operations:
        print()
        print("Operation:",operation.operation_id)
        print("\tStatus     -->", operation.status)
        print("\tDatetime   -->", operation.datetime)
        print("\tTitle      -->", operation.title)
        print("\tPattern id -->", operation.pattern_id)
        print("\tDirection  -->", operation.direction)
        print("\tAmount     -->", operation.amount)
        print("\tLabel      -->", operation.label)
        print("\tType       -->", operation.type)

        with open('success.txt', 'a', encoding='1258') as f:
            f.write('cron works')
            f.write('\n')
