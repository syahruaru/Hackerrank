if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    #print(type(arr))
    list1 = list(arr)
    #print(list1)
    max_ = max(list1)
    #print(max_)
    list2 =  set(list1)
    list2.remove(max_)
    print(max(list2))
    
