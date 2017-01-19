class BinarySearch(list):

    def __init__(self, a, b):
        self.a = a
        self.b = b
        count = b
        for x in range(a):
            self.append(count)
            count += b 
        self.length = a

    def search(self, c):
        l = 0
        r = self.length - 1

        count = 0
        print self
        print "Size {0}, Interval {1}, Top Value: {2}".format(self.a, self.b, self[r])

        if self[r] == c:
            return {'count': count, 'index': r}
        elif self[l] == c:
            return {'count': count, 'index': l}
        elif self[r] < c:
            return {'count': count, 'index': -1}
        elif self[l] > c:
            return {'count': count, 'index': -1}

        print "On each iteration:"
        print " Find the middle index and value"
        print " Check if value is sought value. If so:"
        print "     Return number of interations made and index where value was found"
        print " If not:"
        print "     Check if sought value is larger or smaller that value at current index. If larger:"
        print "         Set leftmost index to current index plus one and iterate"
        print "     If smaller:"
        print "         Set rightmost index to current index less one and iterate"

        while (l < r):
            count += 1
            m = (l + r)/2
            print "Iteration #:: {0} Left pointer: {1}, Right pointer: {2}, Middle index: {3}, Objective: {4}, Middle Value: {5}".format(count,l,r,m,c,self[m])
            if self[m] < c:
                l = m + 1
                if (l + 1) == r:
                    print "     Left and Right pointer are next to each other, check if final two [{0},{1}] match sought value.".format(self[l],self[r])
                    if self[l] == c:
                        return {'count': count, 'index': l}
                    elif self[r] == c:
                        return {'count': count, 'index': r}
                    else:
                        return {'count': count, 'index': -1}
            elif self[m] > c:
                r = m - 1
                if (l + 1) == r:
                    print "     Left and Right pointer are next to each other, check if final two [{0},{1}] match sought value.".format(self[l],self[r])
                    if self[l] == c:
                        return {'count': count, 'index': l}
                    elif self[r] == c:
                        return {'count': count, 'index': r}
                    else:
                        return {'count': count, 'index': -1}
            else:
                return {'count': count, 'index': m}    
        return {'count': count, 'index': -1}