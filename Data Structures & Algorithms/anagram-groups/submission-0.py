class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_groups = []
        result = []
        for str in strs:
            dict_aux = {}
            for char in str:
                dict_aux[char] = 1 if dict_aux.get(char) is None else dict_aux[char] + 1

            print(dict_aux)
            found_group = False
            for anagram_group in anagram_groups:
                if dict_aux == anagram_group[0]:
                    anagram_group[1].append(str)
                    found_group = True
                    break
            
            if not found_group:
                anagram_groups.append([dict_aux, [str]])

        return [anagram_group[1] for anagram_group in anagram_groups]


        # aux = [ [{'a': '2', 'c': 1}, ["caa", "aac"]] ] 