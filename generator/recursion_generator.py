def powerset(seq):
    """
    Returns all the subsets of this set. This is a generator.
    """
    if len(seq) <= 0:
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item
            
print([ i for i in powerset([1,2,3,4])])
# 제네레이터의 첫 yeild부터 차례대로 print한다는 의미