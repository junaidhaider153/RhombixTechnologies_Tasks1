# ============================================
# FIBONACCI GENERATOR - Rhombix Technologies
# ============================================

def fibonacci_generator(n):
    """
    Generate Fibonacci sequence up to n terms
    
    Parameters:
    n (int): Number of Fibonacci terms to generate
    
    Returns:
    list: Fibonacci sequence
    """
    sequence = []
    
    if n <= 0:
        return sequence
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    # Initialize first two terms
    sequence = [0, 1]
    
    # Generate remaining terms
    for i in range(2, n):
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
    
    return sequence

def fibonacci_recursive(n):
    """
    Alternative recursive approach for Fibonacci
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci_recursive(n-1)
        seq.append(seq[-1] + seq[-2])
        return seq

def main():
    """Main program execution"""
    print("=" * 50)
    print("FIBONACCI SEQUENCE GENERATOR")
    print("=" * 50)
    
    try:
        # Get user input
        n = int(input("Enter the number of Fibonacci terms to generate: "))
        
        if n <= 0:
            print("Please enter a positive integer!")
            return
        
        # Generate sequence
        fib_sequence = fibonacci_generator(n)
        
        # Display results
        print(f"\nFirst {n} Fibonacci terms:")
        print("-" * 30)
        
        for i, term in enumerate(fib_sequence, 1):
            print(f"Term {i:2}: {term}")
        
        print("\nSequence Summary:")
        print(f"Full sequence: {fib_sequence}")
        print(f"Sum of all terms: {sum(fib_sequence)}")
        
        # Additional feature: Check if a term is prime
        print("\nPrime numbers in the sequence:")
        for term in fib_sequence:
            if term > 1:
                is_prime = all(term % i != 0 for i in range(2, int(term**0.5) + 1))
                if is_prime:
                    print(f"✓ {term} is prime")
    
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()