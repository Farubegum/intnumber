sam = int(input())
if (( sam%400 == 0)or (( sam%4 == 0 ) and ( sam%100 != 0))):
    print("%d \n yes" %sam)
else:
    print("%d \n no" %sam)
