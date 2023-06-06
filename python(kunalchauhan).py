input_str = input(str("Enter your string"))
print(f"Input-String = {input_str}")
def word_freq(input_str):
    counts = {}
    words = str.split(input_str)

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    highest_frequency = max(counts.values())
    for word in counts:
        if counts[word] == highest_frequency:
            return len(word)

print(f"Output - {word_freq(input_str)}")
 