def convertToTitle(num ,finalstr =''):
    def getcol(columnNumber,finalstr):
            quotient= columnNumber//26
            remainder = columnNumber%26
            if(remainder !=0):
                char = chr(ord('@')+remainder)
                finalstr +=char
            else:
                finalstr +='Z'
                quotient -=1
            if(quotient<=26 and quotient>=1):
                char = chr(ord('@')+quotient)
                finalstr += char
                quotient =0
            if(quotient==0):
                reverse = finalstr[::-1]
                return reverse
            else:
                return getcol(quotient, finalstr)
    getstr = getcol(num,finalstr)
    return getstr

print(convertToTitle(28))
