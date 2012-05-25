#!/usr/bin/python2.7

class OrderedDictionary:

    def __init__(self, d={}, **data):
        self._keys = []
        self._values = []
        if(type(d) not in (dict, OrderedDictionary)):
            raise TypeError("the dictionary entered is not valid - either regular dictionary or OrderedDictionary object is expected")
        for key in d:
            self[key] = d[key] #in the ord-dict add an entry at the key 'key' and give the value at 'key' in d 

        for key in data:
            self[key]= data[key]

    def __repr__(self):
        string = "{"
        first_time = True
        for key, value in self.items():
            if not first_time:
                string += ", " # adding coma to separate entries
            else:
                first_time = False
            string += repr(key) + ": " + repr(value)
        string += "}"
        return string

    def __str__(self):
        return repr(self)

    def __len__(self):
        return len(self._keys)

    def __contains__(self,key):
        return key in self._keys
       
    def __getitem__(self,key):
        if key not in self._keys:
            raise KeyError("The key {0} isn't in the dictionary".format(cle))
        else:
            ind = self._keys.index(key)
        return self._values[ind]

    def __setitem__(self, key, value):
        if key in self._keys:
            ind = self._keys.index(key)
            self._values[ind] = value
        else:
            self._keys.append(key)
            self._values.append(value)

    def __delitem__(self,key):
        if key not in self._keys:
            raise KeyError("The key {0} is not in the dictionary".format(key))
        else:
            ind = self._keys.index(key)
            del self._keys[ind]
            del self._values[ind]

    def __iter__(self):
        return iter(self._keys)

    def __add__(self,other):
        if type(other) is not type(self):
            raise TypeError("Can't add up {0} et {1}".format(type(self), type(other)))
        else:
            new_dict = OrderedDictionary()
            # copy self in new_dict
            for key,value in self.items():
                new_dict[key] = value
            # copy other
            for key,value in other.items():
                new_dict[key] = value

            return new_dict

    def items(self):
        for i, key in enumerate(self._keys):
            val = self._values[i]
            yield (key, val)

    def keys(self):
        return list(self._keys)

    def values(self):
        return list(self._values)







