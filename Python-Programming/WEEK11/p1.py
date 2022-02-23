#break continue and pass
#1jt19cs002@jyothyit.ac.in
#break exit control loop
email = input("enter the email:-")
for c in email:
    if(c=='@'):
        break
    print(c ,end="" " ")


# continue:skip the control loop
for d in email:
    if (d == '@'):
        print(d)
        continue
    print(d, end="" " ")



