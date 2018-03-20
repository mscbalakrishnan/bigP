# Python program to mail merger
# Names are in the file names.txt
# Body of the mail is in body.txt

# open names.txt for reading
with open("names.txt",'r',encoding = 'utf-8') as names_file:

# open body.txt for reading
    with open("body.txt",'r',encoding = 'utf-8') as body_file:
   
# read entire content of the body
        
        # iterate over names
        for name in names_file:
            body = body_file.readline()
        
            print(name)
            print(body)
            mail = "Add "+name+body+"\n"
            print(mail)

                # write the mails to individual files
            with open("result"+".txt",'a',encoding = 'utf-8') as mail_file:
                   mail_file.write(mail)