# Base class representing a file or directory
class File():
    def __init__(self, name, size):
        # Initialize file attributes (name, size, etc.)
        self.name = name
        self.size = size
        # Determine if the file is a directory (directories don't have a dot in their name)
        self.isDirectory = False if '.' in name else True
        # Initialize children (for directories)
        self.children = []
        # Extract the file extension, if any
        self.extension = name.split(".")[1] if '.' in name else ""

    # String representation of the file (just the name)
    def __repr__(self):
        return "{" + self.name + "}"

# Base filter class for filtering files
class filter():
    def __init__(self):
        pass

    # The apply method is meant to be overridden in child classes
    def apply(self, file):
        pass

# Child class of filter, filters files based on their size
class minSizeFilter(filter):
    def __init__(self, size):
        self.size = size  # Set the minimum size filter

    # Check if the file's size is greater than the filter's size
    def apply(self, file):
        return file.size > self.size

# Child class of filter, filters files based on their extension
class extensionFilter(filter):
    def __init__(self, extension):
        self.extension = extension  # Set the extension filter

    # Check if the file's extension matches the filter's extension
    def apply(self, file):
        return file.extension == self.extension

# Class representing a filesystem, which holds filters and applies them to files
class filesystem():
    def __init__(self):
        self.filters = []  # List to store the filters

    # Add a filter to the filesystem (only accepts objects of type filter)
    def add_filter(self, given_filter):
        # Validate that the provided filter is an instance of the filter class
        if isinstance(given_filter, filter):
            self.filters.append(given_filter)

    # Apply OR filtering (files that match any of the filters)
    def apply_OR_filtering(self, root):
        def dfs(root, result):
            if root.isDirectory:
                # If it's a directory, recursively check its children
                for child in root.children:
                    dfs(child, result)
            else:
                # If it's a file, apply all filters
                for f in self.filters:
                    # If any filter applies, add the file to the result and stop
                    if f.apply(root):
                        result.append(root)
                        print(result)
                        return  # Stop after first match
        result = []
        dfs(root, result)  # Start DFS from the root
        return result  # Return the filtered result

    # Apply AND filtering (files that match all filters)
    def apply_AND_filtering(self, root):
        def dfs(root, result):
            if root.isDirectory:
                # If it's a directory, recursively check its children
                for child in root.children:
                    dfs(child, result)
            else:
                # If it's a file, apply all filters
                for f in self.filters:
                    # If any filter fails, stop the process
                    if not f.apply(root):
                        return
                result.append(root)  # Add the file to the result if it passed all filters
                print(result)
                return  # Stop once a valid file is found
        result = []
        dfs(root, result)  # Start DFS from the root
        return result  # Return the filtered result


        
f1 = File("root_300", 300)

f2 = File("fiction_100", 100)
f3 = File("action_100", 100)
f4 = File("comedy_100", 100)
f1.children = [f2, f3, f4]

f5 = File("StarTrek_4.txt", 4)
f6 = File("StarWars_10.xml", 10)
f7 = File("JusticeLeague_15.txt", 15)
f8 = File("Spock_1.jpg", 1)
f2.children = [f5, f6, f7, f8]

f9 = File("IronMan_9.txt", 9)
f10 = File("MissionImpossible_10.rar", 10)
f11 = File("TheLordOfRings_3.zip", 3)
f3.children = [f9, f10, f11]

f11 = File("BigBangTheory_4.txt", 4)
f12 = File("AmericanPie_6.mp3", 6)
f4.children = [f11, f12]


greater5_filter = minSizeFilter(5)
txt_filter = extensionFilter("txt")


my_linux_find = filesystem()
my_linux_find.add_filter(greater5_filter)
my_linux_find.add_filter(txt_filter)

print(my_linux_find.apply_OR_filtering(f1))
print(my_linux_find.apply_AND_filtering(f1))
                    

            
    