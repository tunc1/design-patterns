class List:
    
    def __init__(self):
        self.__array=[]
    
    def add(self,item):
        self.__array.append(item)
    
    def remove(self,item):
        self.__array.remove(item)
    
    def get(self,index):
        return self.__array[index]
    
    def size(self):
        return len(self.__array)
    
    def __iter__(self):
        return ListIterator(self)
    
class ListIterator:
    
    def __init__(self,list):
        self.__index=0
        self.__list=list
    
    def __next__(self):
        if self.__index==self.__list.size():
            raise StopIteration
        else:
            self.__index+=1
            return self.__list.get(self.__index-1)