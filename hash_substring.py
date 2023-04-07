# python3

def read_input():
    # acquire input from keyboard or file
    input_type = input().rstrip().lower()
    if input_type == "i":  # input from keyboard
        pattern = input().rstrip()
        text = input().rstrip()
    elif input_type == "f":  # input from file
        with open("tests/06", "r") as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
    else:
        raise ValueError("Invalid input type choice")
    return (pattern, text)

def print_occurrences(output):
    # control output
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # find occurrences using Rabin-Karp algorithm
    n = len(text)
    m = len(pattern)
    p = 31  # chosen prime number
    d = 256  # number of possible characters
    
    # Calculate hash value of pattern and first substring of text
    pattern_hash = 0
    substring_hash = 0
    h = 1
    for i in range(m-1):
        h = (h * d) % p
    for i in range(m):
        pattern_hash = (pattern_hash * d + ord(pattern[i])) % p
        substring_hash = (substring_hash * d + ord(text[i])) % p
    
    # Check for match in substrings
    occurrences = []
    for i in range(n-m+1):
        if pattern_hash == substring_hash:
            if text[i:i+m] == pattern:
                occurrences.append(i)
        if i < n-m:
            substring_hash = (d * (substring_hash - ord(text[i]) * h) + ord(text[i+m])) % p
    
    return occurrences

# launch functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))