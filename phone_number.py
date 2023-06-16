def alph2num(str_part):
##    MAP_TABLE=(("ABC",'2'),("DEF",'3'),("GHI",'4'),
##               ("JKL",'5'),("MNO",'6'),("PQRS",'7'),
##              ("TUV",'8'),("WXYZ",'9'))
    MAP_TABLE={"A":"2", "B":"2", "C":"2",
               "D":"3", "E":"3", "F":"3",
               "G":"4", "H":"4", "I":"4",
               "J":"5", "K":"5", "L":"5",
               "M":"6", "N":"6", "O":"6",
               "P":"7", "Q":"7", "R":"7", "S":"7",
               "T":"8", "U":"8", "V":"8",
               "W":"9", "X":"9", "Y":"9","Z":"9" }
       
    num_part=""

    for ch in str_part:
        if ch.islower():
            ch=ch.upper()
            
        num_part += MAP_TABLE[ch];
    return num_part

org_num=input("전화번호를 입력하세요 : ")
mixed_phone=org_num.split('-')

merged_phone = []
merged_str = ""

for part in mixed_phone:
    if part.isalpha():
        merged_str += part
    else :
        merged_phone.append(part)

merged_phone.append(merged_str)

converted_number = []

for part in merged_phone:
    if part.isalpha():
        chg_number = alph2num(part)
        converted_number.append(chg_number[0:3])
        converted_number.append(chg_number[3:7])
    else :
        converted_number.append(part)

real_phone_number = '-'.join(converted_number)
print("실제 전화번호는 %s 입니다."% real_phone_number)


        
