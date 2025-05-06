import re
d="Both mobile numbers 123-456-7890 and 1121451617 are same"
p=r'\d{3}-?\d{3}-?\d{4}'
res=re.findall(p,d)
print(res)