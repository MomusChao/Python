#19 If else: Scholarship

score=eval(input())
sco=0
if score>=95:
    sco=2000
elif score>=90 and score<=94:
    sco=1000
elif 80 <=score <=89:
    sco=500
else: 
    sco=0

print("Scholarship:",sco)
