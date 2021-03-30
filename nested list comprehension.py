increasing_pairs = [(x,y) for x in range(0,10) for y in range(x+1,10)]
print(increasing_pairs)

s = None
assert s == None,"not pythonic way"
assert s is None,"pythonic way"