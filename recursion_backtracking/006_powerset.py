
## time complexity :n**2 * 2**n
## space complexity : n · 2ⁿ
# | Space Type                                  | Complexity    |
# | ------------------------------------------- | ------------- |
# | Recursion stack                             | **O(n)**      |
# | Temporary active string copies (if counted) | **O(n²)**     |
# | Result list (returned output)               | **O(n · 2ⁿ)** |



# recursion tree

        #                         ("",0)
        #                       /         \
        #              Exclude             Include 'a'
        #             ("",1)               ("a",1)
        #            /      \             /        \
        #    Exclude        Include   Exclude      Include
        #     ("",2)         ("b",2)   ("a",2)      ("ab",2)
        #    /     \         /    \     /    \        /     \
        # ""      "c"      "b"   "bc"  "a"  "ac"   "ab"   "abc"
# res = # ""      "c"      "b"   "bc"  "a"  "ac"   "ab"   "abc"
# thus we sort, ["", "a", "ab", "abc", "ac", "b", "bc", "c"]
to get: 
class Solution:
    def __init__(self):
        self.res = []
    def rec(self, s, ind, output):
        if ind>=len(s):
            self.res.append(output)
            return
        self.rec(s,ind+1,output)
        #  new list passed everytime
        self.rec(s,ind+1,output+s[ind])
        
	def powerSet(self, s):
	    self.rec(s,0,"") 
	    self.res.sort() # -> sorting the list 2^nlog2^n and sorting the internal string each comparison takes O(n) => (2^nlog2^n) * n =  n*2*nlog2 * n = n**2 * 2**n
		return self.res


       #                   ""
       #        /-----------|-----------\
       #       a            b            c
       #    /-----\          \            \
       #  ab       ac         bc           -
       #  |         |          |
       # abc        -          -
#  time complexity: O(n* 2**n)
#  space complexity:O(n · 2ⁿ)
# | Space Type                        | Complexity    |
# | --------------------------------- | ------------- |
# | Recursion stack (Auxiliary Space) | **O(n)**      |
# | string concatenation              | **O(n)**      |
# | Output list                       | **O(n · 2ⁿ)** |
# | Total space including output      | **O(n · 2ⁿ)** |

# directly performs lexographical: ["", "a", "ab", "abc", "ac", "b", "bc", "c"]

class Solution:
    def __init__(self):
        self.res = []
    def rec(self,s,start,output):
        self.res.append(output)
        for i in range(start,len(s)):
            self.rec(s,i+1,output+s[i]) # Each call may spend up to: O(n) on string concatenation.
    def powerSet(self, s):
        # if initial string not sorted
        s = "".join(sorted(s))
        self.rec(s,0,"")
        return self.res

