# Gia Manning
# 06-23-2024
# P4HW1
# Ask user to enter for number of scores they would like to enter







def main():
    num_scores = int(input("Enter the number of scores you want to enter: "))
    
    scores = []
    for i in range(num_scores):
        while True:
            score = float(input(f"Enter score #{i+1}: "))
            if 0 <= score <= 100:
                scores.append(score)
                break
            else:
                print("Invalid score! Score must be between 0 and 100. Please try again.")
    
    print("\nScores entered:")
    for i, score in enumerate(scores, start=1):
        print(f"Score #{i}: {score}")

if __name__ == "__main__":
    main()
