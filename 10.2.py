mails = dict()
for line in open( raw_input("Enter File Name:")):
    words = line.strip().split()
    if len(words) == 0 and len(words)<2:
        continue
    if words[0] == 'From':
        hours = words[5].split(':')
        if hours[0] not in mails:
            mails[hours[0]] = 1
        else:
            mails[hours[0]] += 1
mail_list = list()
for key,mail in mails.items():
    mail_list.append((key,mail))
mail_list.sort()
for key,val in mail_list:
    print key,val