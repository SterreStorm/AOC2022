
class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.directories = {}
        self.files = {}
        self.size = 0
        self.parent = parent
        self.calculated = False

    def add_directory(self, directory, parent):
        self.directories[directory] = Dir(directory, parent)

    def add_file(self, name, size):
        self.files[name] = File(name, size)

    def calculate_size(self):
        if not self.calculated:
            for file in self.files:
                self.size += int(self.files[file].return_size())
            for directory in self.directories:
                self.size += self.directories[directory].calculate_size()
            self.calculated = True

        return self.size

    def get_size(self):
        return self.size

    def get_parent(self):
        return self.parent


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)

    def return_size(self):
        return self.size


def parse_input(filename):
    # boom bouwen
    with open(filename) as f:
        root = Dir("/", None)
        currentdirectory = root
        for line in f:
            # parse commands
            if line.startswith("$"):
                if "cd" in line:
                    if ".." in line:
                        currentdirectory = currentdirectory.parent

                    else:
                        line = line.strip().replace("$ cd ", "")
                        if line == "/":
                            currentdirectory = root

                        else:
                            currentdirectory = currentdirectory.directories[line]

            elif line.startswith("dir"):
                line = line.strip().replace("dir ", "")
                currentdirectory.add_directory(line, currentdirectory)

            else:
                line = line.strip()
                size, name = line.split()
                currentdirectory.add_file(name, size)

        return root


def lekker_rekene(boom, minimal_needed, best_amt = None):
    size = boom.calculate_size()
    best = best_amt

    if best_amt == None or best_amt >= size > minimal_needed:
        print(f"new best at {size}")
        best = size

    for directory in boom.directories.values():
        best = lekker_rekene(directory, minimal_needed, best)

    return best

def anders_rekene(boom):
    total_space = 70000000
    filesize = 30000000
    space_left = total_space - boom.calculate_size()
    need_to_free = filesize - space_left

    best_amount = lekker_rekene(boom, need_to_free)

    print(best_amount)

boom = parse_input("input/day7full.txt")
anders_rekene(boom)


