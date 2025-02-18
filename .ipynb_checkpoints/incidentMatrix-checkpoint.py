import re

class IncidenceMatrix:
    def __init__(self, statements, keywords):
        self.statements = statements
        self.keywords = keywords
        self.matrix = self.create_incidence_matrix()

    def create_incidence_matrix(self):
        # Initialize the incidence matrix with zeros
        matrix = [[0 for _ in range(len(self.keywords))] for _ in range(len(self.statements))]
        
        for i, statement in enumerate(self.statements):
            for j, keyword in enumerate(self.keywords):
                if keyword in statement:
                    matrix[i][j] = 1  # Mark presence of keyword in statement
        
        return matrix

    def display_matrix(self):
        print("Incidence Matrix:")
        print("   " + " ".join(self.keywords))
        for i, statement in enumerate(self.statements):
            print(f"S{i+1}: " + " ".join(str(self.matrix[i][j]) for j in range(len(self.keywords))))

    def evaluate_query(self, query):
        # Split the query into parts based on AND and OR
        or_clauses = query.split("OR")
        found_statements = set()

        for or_clause in or_clauses:
            and_keywords = or_clause.split("AND")
            and_keywords = [keyword.strip() for keyword in and_keywords]

            # Check if all keywords in the AND clause are present
            for i in range(len(self.statements)):
                if all(self.matrix[i][self.keywords.index(keyword)] == 1 for keyword in and_keywords if keyword in self.keywords):
                    found_statements.add(self.statements[i])

        return list(found_statements)


# Example usage
if __name__ == "__main__":
    statements = [
        "The cat sat on the mat.",
        "Dogs are great companions.",
        "Cats and dogs can be friends.",
        "The quick brown fox jumps over the lazy dog."
    ]
    keywords = ["cat", "dog", "friends", "quick", "lazy"]

    incidence_matrix = IncidenceMatrix(statements, keywords)
    incidence_matrix.display_matrix()

    # Query for statements containing keywords with AND and OR conditions
    query_statement = "cat AND friends OR dog"
    result = incidence_matrix.evaluate_query(query_statement)
    print(f"Statements matching the query '{query_statement}': {result}")
