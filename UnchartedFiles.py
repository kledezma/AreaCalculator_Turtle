## Try Catch
## Truncate & Seek

sent_message =  'Hola esto es secretisimo'

try:
    with open('mensajito.txt','w') as file:
        file.write(sent_message)
finally:
    print("Termino")


try:
    with open('mensajito.txt','r+') as file:
       originalmsg = file.read()
       print(originalmsg)
       file.seek(0)
       unsent_message = 'This message has been unsent.'
       file.truncate(len(unsent_message))
       file.write(unsent_message)
finally:
    print("Termino")
