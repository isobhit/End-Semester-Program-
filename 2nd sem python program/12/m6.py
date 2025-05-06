import my_package as pkg

print("List operations:")
print(pkg.append1(10))
print(pkg.extend1([20, 30]))
print(pkg.pop())
print(pkg.remove1(20))

print("\nSet operations:")
print(pkg.adds2(5))
print(pkg.adds2(10))
print(pkg.slen2())
print(pkg.remove2(5))

print("\nDictionary operations:")
print(pkg.add3("a", 1))
print(pkg.add3("b", 2))
print(pkg.len3())
print(pkg.keys3())
print(pkg.values3())