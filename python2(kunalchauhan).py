string = input("Enter your string")
print(f"Input string = {string}")


def valid_string(string):
    char_freq = {}
    for char in string:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    freq_list = list(char_freq.values())
    if all(freq == freq_list[0] for freq in freq_list):
        print(f"This is a valid string because frequencies are {char_freq}")
        return "YES"
    for i in range(len(string)):
        temp_freq_list = freq_list.copy()
        temp_freq_list[char_freq[string[i]]-1] -= 1
        if all(freq == temp_freq_list[0] for freq in temp_freq_list):
            print(f"This is a valid string because frequencies are {char_freq}")
            return "YES"
    print(f"This is not a valid string because frequencies are {char_freq}")
    return "NO"

print(valid_string(string))