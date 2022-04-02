def is_palindrome_1(s):
    try:
        s = s.replace(" ","")
        x = s.casefold()
        if x == x [::-1] :
            return True
        else:
            return False
    except:
        print("pleas enter a valid input")



def is_palindrome_2(s):
    try:
        s=s.replace(" ","")
        x = s.casefold()
        y = reversed(x)
        z = "".join(y)
        print(y)
        if x == z:
            return True
        else:
            return False
    except:
            print("pleas enter a valid input")




def find_nth_occurrence(substring, string, occurrence = 1):
    try:
        indx = -1
        for i in range(0, occurrence):
            indx = string.find(substring, indx + 1)
        return indx
    except:
        print("pleas check your inputs")    



def solve(a,b):
    try:
        if a == b: return True
        elif "*" not in a: return False
        else:
            index   = a.find('*')
            left    = a[:index]
            right   = a[-1:index]
            asterix = b
            asterix = asterix.replace(left,"").replace(right,"")
            x       = left + asterix + right
            return x == b
    except:
        print("someting wrong happend")


