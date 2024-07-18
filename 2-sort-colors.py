class Solution:

    def sortColors(self, nums):
        start = 0
        end = len(nums)-1

        def swap_elements(a,b,elements):
            elements[a], elements[b] = elements[b], elements[a]
            return elements


        def partition_array_sort(elements, start, end):
            pivot_index = start
            pivot = elements[pivot_index]

            while start < end:
                while elements[start] <= pivot and start < len(elements)-1:
                    start +=1
                
                while elements[end] > pivot:
                    end -=1
                if(start<end):
                    swap_elements(start, end, elements)
            
            swap_elements(pivot_index, end, elements)
            
            return end
        def quicksort(elements, start, end):
            if(start<end):
                swap_index = partition_array_sort(elements, start, end)
                quicksort(elements,start, swap_index-1)
                quicksort(elements, swap_index+1, end )
            return elements
        
        quicksort(nums, start, end)
        return nums
            
sol = Solution()
list = [0,2,2,2,0,2,1,1]
print(sol.sortColors(list))
