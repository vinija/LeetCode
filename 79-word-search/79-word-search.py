class Solution:
    def __init__(self):
        self.found = False                                          # This variable to track final return value

    def exist(self, board: [[str]], word: str) -> bool:
        if not word or not board:
            return False

        for i in range(len(board)):                                 # Let this for loop get the first matching letter
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    self.found = self.dfs(board, i, j, word[1:])    # Passing the first matching indices and remaining letters to dfs
        return self.found


    def dfs(self, arr, i, j, word):

        if not word:                                                # Base case: reached the end of the word string
            self.found = True
            return self.found

        temp = arr[i][j]                                            # Store the arr value temporarily for later reassignment
        arr[i][j] = '#'                                             # Mark the cell visited for the current set of (i,j)

        for I, J in (i+1,j), (i-1,j), (i,j+1), (i,j-1):             # Scan left,right,below & above (i,j) for the next letter
            if 0 <= I < len(arr) and 0 <= J < len(arr[0]) and arr[I][J]==word[0]:
                self.dfs(arr, I, J, word[1:])                       # If the next letter is found, go for the further next until base case

        arr[i][j]=temp                                              # In case, word is not found for (i,j) we need the board in original form to check for next set of (i,j) from exist function
        return self.found