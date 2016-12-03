class BinarySearch(list):
    def __init__(self, a, b):
        super(BinarySearch,self)__init__()
        self.length = a # no. of elements in the list
        self.step = b #diff between el1 and el2 -intervals

    def search(self, val):
        dic={} #{count : index}
        count=0 #count no. of iterates
        index=0 #index of val
        last = self.length - 1 # last element
        found = False
        #binary search algorithm implementation       
        while index <= last and not found:
            middle = (index + last)//2
            count=count+1
            if self[middle] == val:
                found = True
            else:
                if val < self[middle]:
                    last = middle-1
                else:
                    index = middle+1
                   
        dic = {count:index}
        return dic

