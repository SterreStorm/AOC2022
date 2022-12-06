
def start_of_packet(filename):
    with open(filename) as f:
        # obtain string
        for line in f:
            # split into proper substrings
            for i in range(13, len(line)):
                count = 0
                substring = line[i-13:i+1]
                # check if no double characters
                for j in range(len(substring)):
                    if substring.count(substring[j]) > 1:
                        count += 1
                # print location
                if count == 0:
                    print(i+1)
                    break


start_of_packet("input/day6full.txt")
