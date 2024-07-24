def generateParenthesis(n):
    result = []
    def appendResult(left=0, right=0, string=''):
	    if len(string) == n * 2:
	    	result.append(string)
	    	return 
	    if left < n:
	    	appendResult(left + 1, right, string + '(')
	    if right < left:
	    	appendResult(left, right + 1, string + ')')
    appendResult()
    return result

print(generateParenthesis(3))