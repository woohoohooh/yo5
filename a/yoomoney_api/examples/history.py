from django.http import request
from yoomoney import Client
from hello.models import Success

st = ''
dt = ''
ad = ''
ch = False

token = "410012025117208.08C28F3D0A7311BD7665C722818F43EF0DF7BB7C3A552D7994A31B954C10BE7C12F61EC916DDFB751FBE9DA37C48C506964D30DAF428D94B52D8BCFF60AEB647BB73081B47A55A5679F631F5ACD181892D7F722CC130899818BFD8339E662F4E82C4E89BCA96B6FFDDA0FA8883F6024F3377763D19B1F86C457D09F009E5090B"

client = Client(token)

history = client.operation_history()

print("List of operations:")
print("Next page starts with: ", history.next_record)

def check():
    global ad
    global st
    global dt
    global ch
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
        ad = operation.operation_id
        st = operation.status
        dt = operation.datetime
        looks = Success.objects.filter(otion=ad)
        aa = str(looks)
        a1 = aa.find(': ')
        a2 = aa.find('>')
        a3 = aa[a1+2:a2]
        if a3 != ad:
            ch = True
            add = Success(otion=operation.operation_id)
            add.save()

