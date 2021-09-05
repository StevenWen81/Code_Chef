def set_alarm(employed, vacation):
    ans = ""
    if employed==True:
        if vacation==True:
            ans = False
        else:
            ans = True
    else:
        if vacation==True:
            ans = False
        else:
            ans = False
    return ans