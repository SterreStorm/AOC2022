
def start_of_packet(filename):
    with open(filename) as f:
        # obtain string
        for line in f:
            for i in range(13, len(line)):
                count = 0
                substring = line[i-13:i+1]
                for j in range(len(substring)):
                    if substring.count(substring[j]) > 1:
                        count += 1
                if count == 0:
                    print(i+1)
                    break


start_of_packet("input/day6full.txt")
