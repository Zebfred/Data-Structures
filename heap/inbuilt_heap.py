import heapq

H = [21,1,45,78,3,5]
# Use heapify to rearrange the elements
heapq.heapify(H)
print(H)

#inserting
import heapq
H = [21,1,45,78,3,5]
# Covert to a heap
heapq.heapify(H)
print(H)
# Add element
heapq.heappush(H,8)
print(H)

#removing 
import heapq

H = [21,1,45,78,3,5]
# Create the heap

heapq.heapify(H)
print(H)

# Remove element from the heap
heapq.heappop(H)

print(H)
