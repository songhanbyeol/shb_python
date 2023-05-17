print("생각나는 영어단어 2개를 입력하세요!")
word1 = input("영어단어1 \n")
word2 = input("영어단어2 \n")

english_word = word1 + word2
lower_cast_strig = english_word.lower()
word_count = lower_cast_strig.count("a")

print(word_count)