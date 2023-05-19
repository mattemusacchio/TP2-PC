def merge_sort(lista):
    def merge(lista1,lista2):
        i,j=0,0
        result = []
        while(i < len(lista1) and j < len(lista2)):
            if lista1[i] < lista2[j]:
                result.append(lista1[i])
                i += 1
            else:
                result.append(lista2[j])
                j += 1
        result += lista1[i:]
        result += lista2[j:]
        return result
    if len(lista) < 2:
        return lista
    else:
        medio = len(lista)//2
        lista1_ord = merge_sort(lista[:medio])
        lista2_ord = merge_sort(lista[medio:])
        return merge(lista1_ord,lista2_ord)
    
print(merge_sort([8,9,2,3,5,1,2,3,4,4]))