class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        top=0
        bottom= len(matrix)-1

# doing binary search among rows to know which row woll contain the element
        while(top<=bottom):
            row=(top+bottom)//2

            if(target > matrix[row][-1]):
                top=row+1
            elif (target < matrix[row][0]):
                bottom=row-1
            else:
                break
        
        if not(top<=bottom):
            return False
        # iterating in the row found using binary search and searching the element
        row=(top+bottom)//2

        l,r=0,len(matrix[0])-1

        while(l<=r):
            mid=(l+r)//2
            if(matrix[row][mid]> target):
                r=mid-1
            elif(matrix[row][mid]<target):
                l=mid+1
            else:
                return True
        return False
        
