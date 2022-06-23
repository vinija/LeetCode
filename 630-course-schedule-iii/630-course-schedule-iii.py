class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
		#sorts the course according to the 2nd index of all elements in the list
        courses.sort(key = lambda x:x[1])
        #print(courses) #to visualize the code after sorting it
        maxHeap = [] # to store the negative values of the courses of index to understand more watch the image attached you will get more clarification
		# to count the courses and to add the total Sum
        cnt,totSum = 0,0 
		#traverse the loop upto length of the courses
        for i in range(len(courses)): 
			#push the negative value of the courses[i][0] into maxHeap
            heappush(maxHeap,-1*courses[i][0])
			#calculate the total number of courses to total Sum and increment the count by 1
            totSum += courses[i][0]
            cnt += 1
            #print(maxHeap) #Just to see the elements present in max heap
			#if total sum exceeds before the loop ends then heap comes into action to find the exact count
            if totSum > courses[i][1]:
				#Now negative value in the heap gets poped out and added to the total Sum and the count is decremented by 1.
                totSum += heappop(maxHeap)
                cnt -= 1
        return cnt