class Solution:
    def encode(self, words: list[str]):

        encoded_msg = ""
        for word in words:
            encoded_msg += f"{len(word)}#" + word
        return encoded_msg

    def decode(self, encoded_msg: str):

        decoded_msg, i = [], 0

        while i < len(encoded_msg):
            j = i + 2
            i = int(encoded_msg[i]) + j
            word = encoded_msg[j:i]
            decoded_msg.append(word)

        return decoded_msg


def main():

    word_list = ["lint", "code", "love", "you"]

    S = Solution()

    encoded_msg = S.encode(word_list)
    print(encoded_msg)

    decoded_msg = S.decode(encoded_msg)
    print(decoded_msg)


if __name__ == "__main__":
    main()
