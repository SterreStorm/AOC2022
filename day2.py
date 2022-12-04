
def rock_paper_scissors(filename):
    total_score = 0
    with open(filename) as inp:
        for line in inp:
            opponent, self = line.split()
            #loss
            if self == "X":
                if opponent == "A":
                    total_score += 3
                elif opponent == "B":
                    total_score += 1
                else:
                    total_score += 2

            # draw een biertje
            elif self == "Y":
                total_score += 3
                if opponent == "A":
                    total_score += 1
                elif opponent == "B":
                    total_score += 2
                else:
                    total_score += 3

            # win
            elif self == "Z":
                total_score += 6
                if opponent == "A":
                    total_score += 2
                elif opponent == "B":
                    total_score += 3
                else:
                    total_score += 1


        print(f"Your total score is {total_score}")


rock_paper_scissors("day2full.txt")
