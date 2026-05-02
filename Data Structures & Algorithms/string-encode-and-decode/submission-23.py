class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_string = ""
        for s in strs:
            encoded_string = f"{encoded_string}{len(s)}#{s}"

        return encoded_string

    def decode(self, s: str) -> List[str]:

        decoded_string = []
        while len(s) > 0:

            delimiter_index = s.find("#")
            string_length = int(s[0:delimiter_index])

            string = s[delimiter_index + 1 : delimiter_index + 1 + string_length]

            decoded_string.append(string)
            s = s[delimiter_index + 1 + string_length : len(s)]

        return decoded_string

