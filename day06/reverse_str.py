# reversing a string in python
# str[start:stop:step]

trial = "reversal"
new_trial = trial[::-1]
print(new_trial)


def str_reverse(str):
    if len(str)==0:
        return str
    else: 
        return str_reverse(str[1:]) + str[0]

print(str_reverse("reversal"))