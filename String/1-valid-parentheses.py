def isValid( s):
        if len(s) == 0 or len(s)%2 !=0:
            return False
        result = False
        dictionary = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        list = []
        for i in s:
            if i in dictionary:
                list.append(i)
            else:
                if(len(list)==0):
                     return False
                last = list[-1]
                elem = dictionary.get(last,0)
                if elem ==i:
                    list.pop()
                else:
                    break
                
        if len(list) ==0:
            result = True
        return result

s = "()[]{}"

print(isValid(s))