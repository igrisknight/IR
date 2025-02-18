def levenshtein_distance(s1, s2):
    # Create a matrix to store distances
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the first row and column
    for i in range(m + 1):
        dp[i][0] = i  # Deletion cost
    for j in range(n + 1):
        dp[0][j] = j  # Insertion cost

    # Fill the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No operation needed
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + 1,    # Deletion
                    dp[i][j - 1] + 1,    # Insertion
                    dp[i - 1][j - 1] + 1  # Substitution
                )

    # Print the matrix with headers for clarity
    print("Levenshtein Distance Matrix:")
    
    # Print header row (s2 characters)
    header = "    " + "  ".join([" "] + list(s2))
    print(header)
    
    # Print each row with corresponding character from s1 (or a space for the 0-th row)
    for i in range(m + 1):
        row_label = " " if i == 0 else s1[i - 1]
        row_values = "  ".join(f"{dp[i][j]:2}" for j in range(n + 1))
        print(f"{row_label}  {row_values}")
    
    return dp[m][n]

# Example usage
if __name__ == "__main__":
    s1 = "kitten"
    s2 = "sitting"
    distance = levenshtein_distance(s1, s2)
    print(f"\nThe Levenshtein distance between '{s1}' and '{s2}' is: {distance}")
