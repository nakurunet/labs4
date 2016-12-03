def find_missing(a,b):
        if a==[] or b==[]:
                return 0
        e = list(set(a).symmetric_difference(set(b)))
        if e!=[]:
                f=sum(e)
                return f
        else: return 0
