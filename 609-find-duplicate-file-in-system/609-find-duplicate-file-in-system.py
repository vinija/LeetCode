class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = {}
        duplicateFiles=[]
        for filePath in paths:
            fileNames = filePath.split() #Split the path to filenames
            directoryPath = fileNames[0] #To take only the directory from the given filePath
            for file in fileNames[1:]: #traverse through each file
                fileName,fileContent = file[:file.index('(')],file[file.index('('):-1]#To get fileName and fileContent
                if fileContent not in dic:# if the content not in dic make an empty list for that particular key
                    dic[fileContent] = []
                dic[fileContent].append(directoryPath+'/'+fileName)#Just append the value of the key in the dictionary every key has a list of fileNames
        for value in dic.values():
            if len(value)>1: #Append only if the len the values in the Dictionary is > 1
                duplicateFiles.append(value)
        return duplicateFiles[::-1] #To generate the output as it is in the expected I have used [::-1]