import random
import time

def main():
    user1 = get_level()
    score = 0
    operation = get_op()
    streak = 0
    start_time = time.time()

    for i in range(10):
        score, streak = generate_integer(level = user1, operation = operation, score = score, streak = streak)
        end_time = time.time()
        total_time = round(end_time - start_time, 2)

    print(f"Score: {score}")
    print(f"Total time taken: {total_time} seconds!")
    save_score(score, user1, operation, total_time)

def get_op():
    ops = { "A" : "Addition" , "S" : "Subtraction" , "M" : "Multiplication", "D" : "Division"}
    while True:
        try:
            innet = input("operation : ").upper()
            if innet in ops:
                print(f"You have chosen : {ops[innet]}")
                return innet
            print("Enter the correct operation")
        except ValueError:
            pass
        



def get_level():
    while True:
        try:
            iret = int(input("Level: "))
            if iret in [1, 2, 3, 4, 5]:
                 return iret
        except ValueError:
            pass

def generate_integer( level, operation, score, streak):
     if level == 1:
        start, end = 0, 9
     elif level == 2:
        start, end = 10, 99
     elif level == 3:
        start, end = 100,999
     elif level == 4:
        start, end = 1000,9999
     else:
        start, end = 10000, 99999

     if operation   == "S":
        inet1 = random.randint(start, end)
        inet2 = random.randint(start, end)
        correct = inet1 - inet2
     elif operation == "A":
        inet1 = random.randint(start, end)
        inet2 = random.randint(start, end)
        correct = inet1 + inet2
     elif operation == "M":
        inet1 = random.randint(start, end)
        inet2 = random.randint(start, end)
        correct = inet1 * inet2
     else :
        inet1 = random.randint(start, end)
        inet2 = random.randint(start, end)
        correct = inet1 / inet2


     tries = 0
     

     while True:
        try:
            if operation == "S":
                final = int(input(f"{inet1} - {inet2} = "))
            elif operation == "A":
                final = int(input(f"{inet1} + {inet2} = "))
            elif operation == "M":
                final = int(input(f"{inet1} * {inet2} = "))
            else:
                final = int(input(f"{inet1} // {inet2} = "))

            if final != correct:
                print("EEE")
                tries += 1
                streak = 0
                if tries == 3:
                    print(f"Correct Answer = {correct}")
                    return score, 0
                continue
            else:
                score += 1
                if tries == 0:
                    print("Correct!")   
                    streak += 1
                    if streak >= 3:
                        print("🔥 STREAK BONUS! +2 Points")
                        score += 2
                else:
                    score += 1
                return score, streak

        except ValueError:
            print("EEE")
            tries += 1
            streak = 0
            if tries == 3:
                print(f"Correct Answer = {correct}")
                return score, 0
            continue
def save_score(score, level, operation, total_time):
    with open("scores.txt", "a") as file:
        file.write(f"Level: {level} | Op: {operation} | Final Score: {score}\n| Time Taken: {total_time}s\n")
    print("Score saved to scores.txt! 📝")

    

if __name__ == "__main__":
    main()

def is_valid_op(op):
    return op.upper() in ["A", "S", "M", "D"]
def is_valid_level(level):
    return level in [1, 2, 3, 4, 5]
def is_valid_score(score):
    return isinstance(score, int) and score >= 0


