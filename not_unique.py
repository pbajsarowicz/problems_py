#zwraca nieunikalne wartosci 
def unique(data):
    return [x for x in data if data.count(x)>1]
 
if __name__ == "__main__":
    print str(unique([1, 2, 3, 1, 3]))
    print str(unique([1, 2, 3, 4, 5]))