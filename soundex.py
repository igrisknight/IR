def soundex(name):
    # Soundex encoding rules
    soundex_dict = {
        "BFPV": "1", "CGJKQSXZ": "2", "DT": "3",
        "L": "4", "MN": "5", "R": "6",
        "AEIOUHWY": "0"
    }

    # Convert letters to their corresponding numbers
    def get_code(char):
        for key in soundex_dict:
            if char in key:
                return soundex_dict[key]
        return ""

    # Step 1: Convert to uppercase and keep first letter
    name = name.upper()
    first_letter = name[0]

    # Step 2: Convert remaining letters
    encoded = [get_code(char) for char in name[1:]]

    # Step 3: Remove consecutive duplicates
    filtered = [encoded[i] for i in range(len(encoded)) if i == 0 or encoded[i] != encoded[i - 1]]

    # Step 4: Remove '0's
    filtered = [num for num in filtered if num != "0"]

    # Step 5: Combine with the first letter and adjust length
    soundex_code = first_letter + "".join(filtered)
    soundex_code = soundex_code[:4].ljust(4, "0")  # Ensure length is 4

    return soundex_code

# Example usage
names = ["Robert", "Rupert", "Rubin", "Ashcraft", "Ashcroft", "Tymczak", "Pfister"]
for name in names:
    print(f"{name}: {soundex(name)}")
