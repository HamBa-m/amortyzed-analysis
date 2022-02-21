#prob A
def inverse(T):
    S = list(T)
    i = 0
    j = len(S) - 1
    while i < j:
        S[i],S[j] = S[j],S[i]
        i += 1
        j -= 1
    return X
    
s = input()
x = reverse(s)
for e in x:
    print(z, end="")

#prob B
def remove_duplicates(A):
    p = 0
    q = 1
    n = len(A)
    M =[]
    while q < n:
    	if A[p] != A[q]:
    		M.append(A[p])
    		p = q
    	q += 1
    M.append(A[q - 1])
    return M
    
s = list(map(int,input().split()))
t = remove_duplicates(s)
for e in t:
	print(e, end=" ")
#prob C
def findSum(A, k):
    i = 0
    n = len(A)
    j = n - 1
    while i != j:
    	if A[i] + A[j] == k : return (A[i],A[j])
    	elif A[i] + A[j] > k : j -= 1
    	else : i += 1
    return -1

k = int(input())
A = list(map(int,input().split()))
print(findSum(A,k))

#prob D
def maxArea(A):
    i = 0
    n = len(A)
    j = n - 1
    mx = 0
    while i < j:
    	s = min(A[i],A[j]) * (j - i)
    	if s > mx : mx = s
    	if A[i] >= A[j]: j -= 1
    	else : i += 1
    return mx

A = list(map(int,input().split()))
print(maxArea(A))

#prob E
def maxSubarray(A, k):
	n = len(A)
	s = sum(A[0:k])
	i = 0
	j = k
	mx = s
	while j < n :
		s -= A[i]
		s += A[j]
		if s > mx : mx = s
		j += 1
		i += 1
	return mx

k = int(input())
A = list(map(int,input().split()))
print(maxSubarray(A,k))

#prob F
def minWindow(S, T):
	i = 0
	j = 0
	n = len(S)
	start = 0
	minimum = len(S) + 1
	match = 0
	need = dict()
	for e in T:
		if need.get(e,"-1") == "-1" : need[e] = 0
		need[e] += 1
	k = len(need)
	window = dict()
	while j < n :
		if need.get(S[j],"-1") != "-1" :
			if window.get(S[j],"-1") == "-1" : window[S[j]] = 0
			window[S[j]] += 1
			if window[S[j]] == need[S[j]] : match += 1
		j += 1
		while match == k:
			if j - i < minimum :
				start = i
				minimum = j - i
			if need.get(S[i],"-1") != "-1" :
				window[S[i]] -= 1
				if window[S[i]] < need[S[i]] : match -= 1 
			i += 1
	if minimum > n : return ""
	return S[start:start+minimum]

s = input()
t = input()
print(minWindow(s,t))