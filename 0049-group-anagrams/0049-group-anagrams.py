class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        i = 0
        map = {}
        result = []

        i = 0
        while i < len(strs):
            if tuple((sorted(strs[i]))) in map:
                map[tuple((sorted(strs[i])))].append(strs[i])
                i += 1
            else:
                map[tuple((sorted(strs[i])))] = [strs[i]]
                i += 1

        for group in map.values():
            result.append(group)
        return result

                
            
        