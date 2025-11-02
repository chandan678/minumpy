class MiniArray:
    def __init__(self, data):
        self.data = list(data)
    
    def __repr__(self):
        return str(self.data)
    
    def __add__(self, other):
        if isinstance(other, MiniArray):
            return MiniArray([x + y for x, y in zip(self.data, other.data)])
        else:
            return MiniArray([x + other for x in self.data])
    
    def __mul__(self, other):
        if isinstance(other, MiniArray):
            return MiniArray([x * y for x, y in zip(self.data, other.data)])
        else: 
            return MiniArray([x * other for x in self.data])
    
    def __sub__(self, other):
        if isinstance(other, MiniArray):
            return MiniArray([x - y for x, y in zip(self.data, other.data)])
        else:
            return MiniArray([x - other for x in self.data])
    
    def __truediv__(self, other):
        # will implement this using a python for loop for now,
        # to be changed later when scaling up
        result = []
        if isinstance(other, MiniArray):
            for x, y in zip(self.data, other.data):
                try:
                    result.append(x/y)
                except:
                    result.append(float('inf'))
        else:
            for x in self.data:
                try:
                    result.append(x/other)
                except:
                    result.append(float('inf'))
        return MiniArray(result)
    
    def __rmul__(self, other):
        return self * other
    
    def __radd__(self, other):
        return self + other
    
    def __rsub__(self, other):
        return MiniArray([other - x for x in self.data])
    
    def __rtruediv__(self, other):
        result = []
        if isinstance(other, MiniArray):
            for x, y in zip(self.data, other.data):
                try:
                    result.append(y/x)
                except:
                    result.append(float('inf'))
        else:
            for x in self.data:
                try:
                    result.append(other/x)
                except:
                    result.append(float('inf'))
        return MiniArray(result)



if __name__ == "__main__":
    this_array = MiniArray([1, 3, 4, 6])
    that_array = MiniArray([5, 6, 7, 0])

    print(this_array + that_array)
    print(this_array * that_array)
    print(this_array - that_array)
    print(this_array / that_array)
    print(3 * this_array)
