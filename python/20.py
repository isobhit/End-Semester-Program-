import re
d="programming language-python"
p="python$"
res=re.search(p,d,re.IGNORECASE)
if res:
    print("Ends with python")
else:
    print("Doesn't ends with python")