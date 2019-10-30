def main():
    r = open(u'file/comp2.txt', 'w')
    l = open(u'file/comp1.txt', 'r').read().split()
    min=len(l[0])
    max=len(l[0])
    min_i=0
    max_i=0
    for i in range(len(l)):
        if len(l[i])>max:
            max=len(l[i])
            max_i=i
        if len(l[i])<min:
            min=len(l[i])
            min_i=i

    r.write('max:\t' + l[max_i]+'\n')
    r.write('min:\t' + l[min_i])

if __name__ == '__main__':
    main()
