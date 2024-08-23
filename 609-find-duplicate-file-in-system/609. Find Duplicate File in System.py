from typing import List
from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_paths = defaultdict(list)

        #Parse each path
        for path in paths:
            #Split the input string into directory and files
            parts = path.split(" ")
            directory = parts[0]

            for file_info in parts[1:]:
                file_name, file_content = file_info.split("(")
                file_content = file_content[:-1] #removing the trailing )

                #form the full path and map it to the content
                full_path = f"{directory}/{file_name}"
                content_to_paths[file_content].append(full_path)
        duplicates = [paths for paths in content_to_paths.values() if len(paths) > 1]
        return duplicates

        