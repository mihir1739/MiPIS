import vonage
def sendsms(number,location,name):
    '''
    Used by the Sever App to send SMS to the client number provided in the database.
    '''
    client = vonage.Client(key="9d6d25c3", secret="mi0qCJ3lus411MWd")
    sms = vonage.Sms(client)
    data = {
        "from": "Vonage APIs",
        "to": "91"+number, #use 8660602806 for default testing...
        "text": f"Mr/Miss {name} was last seen at {location}.Please make required amends.Regards MiPIS"
    }
    file = open("errr.txt","w")
    file.write("91"+number)
    responseData = sms.send_message(data)
    if responseData["messages"][0]["status"] == "0":
        return True
    else:
        file = open("error.txt","a")
        file.write(f"Message failed with error: {responseData['messages'][0]['error-text']}")
        return False

# def sendsms(number,location,name):
#     data = {
#         "from": "Vonage APIs",
#         "to": "91"+number,
#         "text": f"Mr/Miss {name} was last seen at {location}.Please make required amends.Regards MiPIS"
#     }
#     file = open("error.txt","w")
#     file.write(data['from'])
#     file.write(data['text'])
#     return True