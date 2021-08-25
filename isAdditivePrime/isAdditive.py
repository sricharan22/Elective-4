def prime(k):
    if(k < 2):
        return False
    elif(k == 2):
        return True
    elif(k % 2 == 0):
        return False
    else:
        for i in range(3,int((k**0.5)),2):
            if(k % i == 0):
                return False 
        return True

def additive(k):
    sum=0
    temp=k
    while(temp > 0):
        a = temp % 10
        temp = temp // 10
        sum += a
    if(sum == 2 or sum == 3 or sum == 5):
        return True
    elif(sum < 10):
        return False
    else:
        return additive(sum)

def isadditive(n):
    if(prime(n) == True):
        if(additive(n) == True):
            return True
        else:
            return False
    else:
        return False