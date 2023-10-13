def is_anagram(str1, str2):
    # Remove spaces and convert strings to lowercase for accurate comparison
    clean_str1 = str1.replace(" ", "").lower()
    clean_str2 = str2.replace(" ", "").lower()

    # Check if the sorted characters of both strings are the same
    return sorted(clean_str1) == sorted(clean_str2)


# Example usage
word1 = "Listen"
word2 = "Silent"
if is_anagram(word1, word2):
    print(f"{word1} and {word2} are anagrams.")
else:
    print(f"{word1} and {word2} are not anagrams.")
