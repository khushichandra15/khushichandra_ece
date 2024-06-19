str=input("enter string : ")
pre=input("enter prefix to check : ")
suf=input("enter suffix to check : ")
if str.startswith(pre):
    print("it starts with the prefix {}".format(pre))
else:
    print("it does not with the prefix {}".format(pre))
if str.endswith(suf):
    print("it ends with the suffix {}".format(suf))
else:
    print("it does not end with the suffix {}".format(suf))