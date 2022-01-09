def InsertionSort(elements):
    for i in range(1, len(elements)):

        anchor = elements[i]
        j = i-1

        while(j >= 0 and anchor < elements[j]):
            elements[j+1] = elements[j]
            j = j-1
        elements[j+1] = anchor


# elements = [11,9,29,7,2,15,28]
# print(InsertionSort(elements))

if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]
    InsertionSort(elements)
    print(elements)        

