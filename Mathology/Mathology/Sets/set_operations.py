class Set:
    def __init__(self):
        pass
    
    def union(self,*sets):
        if type(sets[0])==tuple or type(sets[0])==list:
            k=[]
            for i in sets:
                for j in i:
                    k.append(j)
            sets=k.copy()
        if len(sets)>1:
            result = set()
            for s in sets:
                for element in s:
                    result.add(element)
            return result
        else:
            return sets[0]

    def intersection(self,*sets):
        if type(sets[0])==tuple or type(sets[0])==list:
            k=[]
            for i in sets:
                for j in i:
                    k.append(j)
            sets=k.copy()
        if len(sets)>1:
            len_dict = dict()
            result = set()
            for s in sets:
                len_dict[(len(s))]=s
            min_len = min(len_dict.keys())
            for element in len_dict.get(min_len):
                result.add(element)
            for element in result.copy():
                for s in sets:
                    if element not in s:
                        if element in result:
                            result.remove(element)
            if len(result)==0:
                return {}
            return result
        else:
            return sets[0]
    
    def difference(self,*sets):
        if type(sets[0])==tuple or type(sets[0])==list:
            k=[]
            for i in sets:
                for j in i:
                    k.append(j)
            sets=k.copy()
        sets = list(sets)
        A = sets[0]
        result = set()
        if len(sets)>1:
            sets.pop(0)
            sets=tuple(sets)
            union_set = self.union(sets)
            for element in A:
                if element not in union_set:
                    result.add(element)
            if len(result)==0:
                return {}
            return result
        else:
            return A
    
    def cartesianProduct(self,*sets):
        if type(sets[0])==tuple or type(sets[0])==list:
            k=[]
            for i in sets:
                for j in i:
                    k.append(j)
            sets=k.copy()
        sets = list(sets)
        n = len(sets)
        if n>1:
            result = []
            k=1
            counter = 1
            while len(sets)>1:
                set1 = sets[k-1]
                set2 = sets[k]
                if counter==1:
                    for i in set1:
                        for j in set2:
                            pair = [i,j]
                            result.append(pair)
                    sets[k]=result
                    sets.pop(k-1)
                else: 
                    rcopy=[]  
                    for j in set2:
                        for i in set1:
                            temp=i.copy()
                            temp.append(j)
                            rcopy.append(temp)
                    result = rcopy
                    sets[k]=result
                    sets.pop(k-1)
                counter+=1
            result_set = set()
            for element in result:
                result_set.add(tuple(element))
            if len(result_set)==0:
                return {}
            return result_set
        else:
            return sets[0]
    
    def cardinality(self,set):
        return len(set)
    
    def powerSet(self,set):
        pass