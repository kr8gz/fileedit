import os

print("""
Thank you for using FileEdit! Type fileedit_help() for help.
-------------------------------------------------------------------------------
""")


# FUNCTIONS ----------------------------------------------------------------------------------------

def fileedit_help():
    print("""
Here are all the things you can do with FileEdit:

f = File("test.txt")
* Creates a new File object from the file "test.txt".
--------------------------------------------------------------------------------
cont = f.contents
* Returns a list where one element is one line of the file.
--------------------------------------------------------------------------------
myvar = cont[3]
* This stores the value of line 3 in myvar without the newline.
--------------------------------------------------------------------------------
f.write("hello world")
* This adds "hello world" to the end of the existing text.
--------------------------------------------------------------------------------
f.write(["if you", "pass a list", "it will write", "multiple lines"])
* This adds the following to the existing text:
    if you
    pass a list
    it will write
    multiple lines
--------------------------------------------------------------------------------
f.write("I am the new line 4, moving all text below me one line down", 4)
f.write("I am the new line 4, moving all text below me one line down", line=4)
* This inserts the text at line 4, with the new text being the new line 4.
--------------------------------------------------------------------------------
f.overwrite("all the text is now replaced by me")
* This does the same as:
f.clear()
f.write("all the text is now replaced by me")
--------------------------------------------------------------------------------
f.overwrite("I am the new line 6, old line 6 is now gone", 6)
f.overwrite("I am the new line 6, old line 6 is now gone", line=6)
* This replaces line 6 with the new text.
  Note: If you specify the line, you can only pass a string.
  Using a list or a tuple raises InvalidArgument.
--------------------------------------------------------------------------------
important_line = f.find("foo")
* This stores the line number in which "foo" appears first.
  If "foo" cannot be found in the file, the function returns None.
--------------------------------------------------------------------------------
f.replace("old", "new")
* Every "old" that was in the file is now "new".
  If there is no occurrence of "old", nothing happens.
--------------------------------------------------------------------------------
f.clear()
* This clears the file.
--------------------------------------------------------------------------------
del f
* This deletes the file and the File object.
""")
    

# ERRORS -------------------------------------------------------------------------------------------

class InvalidFileName(Exception):

    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return f"{self.arg} is not a vaild file name."

class InvalidArgument(Exception):

    def __init__(self, message=""):
        self.message = message

    def __str__(self):
        return self.message
    

# CLASSES ------------------------------------------------------------------------------------------

class File:

    def __init__(self, path):

        if not os.path.isfile(path):
            try:
                with open(path, "w+"):
                    pass
            except OSError:
                raise InvalidFileName(path)
        
        self.name = path
        self.contents = ""

        self.update_contents()

    def __del__(self):

        os.remove(self.name)
      
    def update_contents(self):

        with open(self.name, "r") as f:
            self.contents = f.readlines()
            self.contents.insert(0, "")
            self.contents = [line.strip("\n") for line in self.contents]

    def write(self, text, *args, **kwargs):

        self.update_contents()

        line = None

        if args or kwargs:
            if args:
                l = args[0]
            elif "line" in kwargs:
                l = kwargs['line']
            if type(l) not in [str, int]:
                raise InvalidArgument(f"{l} is not a valid line number")

            try:
                l = int(l)
                if l < 1:
                    raise InvalidArgument(f"{l} is not a valid line number")
            except ValueError:
                raise InvalidArgument(f"{l} is not a valid line number")
            line = l
        
        if type(text) in [tuple, list]:
            
            with open(self.name, "w") as f:
                if line:
                    self.contents = self.contents[:line] + text + self.contents[line:]
                f.writelines([line + "\n" for line in self.contents[1:]])
                if not line:
                    f.writelines([line.strip("\n") + "\n" for line in text])
                
            self.update_contents()

        else:

            with open(self.name, "w") as f:
                if line:
                    self.contents.insert(line, str(text))
                f.writelines([line + "\n" for line in self.contents[1:]])
                if not line:
                    f.write(str(text))
                
            self.update_contents()

    def overwrite(self, text, *args, **kwargs):

        self.update_contents()

        line = None

        if args or kwargs:
            if args:
                l = args[0]
            elif "line" in kwargs:
                l = kwargs['line']
            if type(l) not in [str, int]:
                raise InvalidArgument(f"{l} is not a valid line number")

            try:
                l = int(l)
                if l < 1:
                    raise InvalidArgument(f"{l} is not a valid line number")
            except ValueError:
                raise InvalidArgument(f"{l} is not a valid line number")
            line = l
        
        if type(text) in [tuple, list]:
            
            with open(self.name, "w") as f:
                if line:
                    raise InvalidArgument(f"Cannot insert {type(text)} into line")
                else:
                    f.writelines([line.strip("\n") + "\n" for line in text])
                
            self.update_contents()

        else:

            with open(self.name, "w") as f:
                if line:
                    self.contents[line] = str(text)
                    f.writelines([line + "\n" for line in self.contents[1:]])
                else:
                    f.write(str(text))
                
            self.update_contents()

    def find(self, to_find):

        self.update_contents()

        if type(to_find) not in [str, int, float]:
            raise InvalidArgument(f"{type(to_find)} cannot be searched for")
        if "\n" in str(to_find):
            raise InvalidArgument("The string to find must not contain a newline")

        for line in self.contents:
            if str(to_find) in line:
                return self.contents.index(line)
                break
        else:
            return None

    def replace(self, old, new, *args, **kwargs):

        self.update_contents()
        
        line = None

        if args or kwargs:
            if args:
                l = args[0]
            elif "line" in kwargs:
                l = kwargs['line']
            if type(l) not in [str, int]:
                raise InvalidArgument(f"{l} is not a valid line number")

            try:
                l = int(l)
                if l < 1:
                    raise InvalidArgument(f"{l} is not a valid line number")
            except ValueError:
                raise InvalidArgument(f"{l} is not a valid line number")
            line = l

        if type(old) not in [str, int, float]:
            raise InvalidArgument(f"{type(old)} cannot be searched for")
        if type(new) not in [str, int, float]:
            raise InvalidArgument(f"Cannot replace text with {type(new)}")
        if "\n" in str(old):
            raise InvalidArgument("The string to find must not contain a newline")
        if "\n" in str(new):
            raise InvalidArgument("The string to replace with must not contain a newline")

        if line:
            with open(self.name, "w") as f:
                self.contents[line] = self.contents[line].replace(str(old), str(new))
                f.writelines([line.strip("\n") + "\n" for line in text])
        else:
            with open(self.name, "w") as f:
                f.writelines([line.replace(str(old), str(new)) + "\n" for line in self.contents])

        self.update_contents()

    def clear(self):
        
        with open(self.name, "w"):
            pass
        self.update_contents()
