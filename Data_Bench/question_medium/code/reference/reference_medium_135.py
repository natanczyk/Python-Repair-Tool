from typing import List

"""
1487. Making File Names Unique

create n folders in your file system such that, at the ith minute, U will create a folder with the name names[i].

Since 2 files cannot have the same name,
if you enter a folder name that was previously used, the system will have a suffix addition to its name in the form of (k), where, k is the smallest positive integer such that the obtained name remains unique.

Return an arr of str of length n where ans[i] is the actual name the system will assign to the ith folder when you create it.


EX:
["pes","fifa","gta","pes(2019)"]
O/P -> ["pes","fifa","gta","pes(2019)"]

EX:
["gta","gta(1)","gta","avalon"]
o/p: ["gta","gta(1)","gta(2)","avalon"]

Ex:
["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"]
o/p: ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece(4)"]
"""


class Solution:
    """
    if it's already in the seen dictionary,
    append a suffix k to the name until a unique name is found.

    Time: O(n^2) in the worst case where all file names are the same
    space: O(n)
    """
    def getFolderNames(self, names: List[str]) -> List[str]:

        ans = []  # stores unique file names
        seen = {}

        for name in names:
            if name not in seen:
                ans.append(name)
                seen[name] = 1
            else:
                k = seen[name]
                # creating variants
                while True:
                    new_name = name + '(' + str(k) + ')'
                    if new_name not in seen:
                        ans.append(new_name)
                        seen[new_name] = 1
                        break
                    else:
                        k += 1

                # save the latest version of variant so to avaoid above while
                # loop calculation
                seen[name] = k
            

        return ans