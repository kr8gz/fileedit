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
bf = ByteFile("test.docx")
* Creates a new ByteFile object from the file "test.docx".
--------------------------------------------------------------------------------
contents = f.contents
* Returns a list where one element is one line of the file.
--------------------------------------------------------------------------------
myvar = contents[3]
* This stores the value of line 4 in myvar without the newline.
  (Python indexing system!)
--------------------------------------------------------------------------------
anothervar = str(f)
* This converts the whole file into a string, with each line separated by
  newlines.
* This does the same as:
anothervar = "\\n".join(f.contents)
--------------------------------------------------------------------------------
f.write("hello world")
* This adds "hello world" to the end of the existing text.
--------------------------------------------------------------------------------
f.write(["if you", "pass a list", "it will write", "multiple lines", 123])
* This adds the following to the existing text:
    if you
    pass a list
    it will write
    multiple lines
    123
--------------------------------------------------------------------------------
f.write("I am the new line 4, moving all text below me one line down", 3)
f.write("I am the new line 4, moving all text below me one line down", line=3)
* This inserts the text at line 4, with the new text being the new line 4.
  (Python indexing system!)
--------------------------------------------------------------------------------
f.overwrite("all the text is now replaced by me")
* This does the same as:
f.clear()
f.write("all the text is now replaced by me")
--------------------------------------------------------------------------------
f.overwrite("I am the new line 6, old line 6 is now gone", 5)
f.overwrite("I am the new line 6, old line 6 is now gone", line=5)
* This replaces line 6 with the new text.
  Note: If you specify the line, you can only pass a string.
  Using a list or a tuple raises InvalidArgument.
  (Python indexing system!)
--------------------------------------------------------------------------------
important_line_number = f.find("foo")
* This stores the line number in which "foo" appears first.
  If "foo" cannot be found in the file, the function returns None.
--------------------------------------------------------------------------------
some_line = f.contents[f.find("bar")]
* This stores the whole line in which "bar" was found first.
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

    def __repr__(self):

        return "\n".join(self.contents)
      
    def update_contents(self):

        with open(self.name, "r") as f:
            self.contents = f.readlines()
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
                if l < 0:
                    raise InvalidArgument(f"{l} is not a valid line number")
            except ValueError:
                raise InvalidArgument(f"{l} is not a valid line number")
            line = l
        
        if type(text) in [tuple, list]:
            
            with open(self.name, "w") as f:
                if line:
                    self.contents = self.contents[:line] + text + self.contents[line:]
                f.writelines([line + "\n" for line in self.contents])
                if not line:
                    f.writelines([str(line).strip("\n") + "\n" for line in text])
                
            self.update_contents()

        else:

            with open(self.name, "w") as f:
                if line:
                    self.contents.insert(line, str(text))
                f.writelines([line + "\n" for line in self.contents])
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
                if l < 0:
                    raise InvalidArgument(f"{l} is not a valid line number")
            except ValueError:
                raise InvalidArgument(f"{l} is not a valid line number")
            line = l
        
        if type(text) in [tuple, list]:
            
            with open(self.name, "w") as f:
                if line:
                    raise InvalidArgument(f"Cannot insert {type(text)} into line")
                else:
                    f.writelines([str(line).strip("\n") + "\n" for line in text])
                
            self.update_contents()

        else:

            with open(self.name, "w") as f:
                if line:
                    self.contents[line] = str(text)
                    f.writelines([line + "\n" for line in self.contents])
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
                if l < 0:
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
                f.writelines([line.strip("\n") + "\n" for line in self.contents])
        else:
            with open(self.name, "w") as f:
                f.writelines([line.replace(str(old), str(new)) + "\n" for line in self.contents])

        self.update_contents()

    def clear(self):
        
        with open(self.name, "w"):
            pass
        self.contents = ""


class ByteFile:

    def __init__(self, path):

        if not os.path.isfile(path):
            try:
                with open(path, "wb+"):
                    pass
            except OSError:
                raise InvalidFileName(path)
        
        self.name = path
        self.contents = ""

        self.update_contents()

    def __del__(self):

        os.remove(self.name)

    def __repr__(self):

        return b"\n".join(self.contents)
      
    def update_contents(self):

        with open(self.name, "rb") as f:
            self.contents = f.readlines()
            self.contents = [line.strip(b"\n") for line in self.contents]

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
                if l < 0:
                    raise InvalidArgument(f"{l} is not a valid line number")
            except ValueError:
                raise InvalidArgument(f"{l} is not a valid line number")
            line = l
        
        if type(text) in [tuple, list]:
            
            with open(self.name, "wb") as f:
                if line:
                    self.contents = self.contents[:line] + text + self.contents[line:]
                f.writelines([line + b"\n" for line in self.contents])
                if not line:
                    f.writelines([str(line).strip(b"\n") + b"\n" for line in text])
                
            self.update_contents()

        else:

            with open(self.name, "wb") as f:
                if line:
                    self.contents.insert(line, str(text))
                f.writelines([line + b"\n" for line in self.contents])
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
                if l < 0:
                    raise InvalidArgument(f"{l} is not a valid line number")
            except ValueError:
                raise InvalidArgument(f"{l} is not a valid line number")
            line = l
        
        if type(text) in [tuple, list]:
            
            with open(self.name, "wb") as f:
                if line:
                    raise InvalidArgument(f"Cannot insert {type(text)} into line")
                else:
                    f.writelines([str(line).strip(b"\n") + b"\n" for line in text])
                
            self.update_contents()

        else:

            with open(self.name, "wb") as f:
                if line:
                    self.contents[line] = str(text)
                    f.writelines([line + b"\n" for line in self.contents])
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
                if l < 0:
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
            with open(self.name, "wb") as f:
                self.contents[line] = self.contents[line].replace(str(old), str(new))
                f.writelines([line.strip(b"\n") + b"\n" for line in self.contents])
        else:
            with open(self.name, "wb") as f:
                f.writelines([line.replace(str(old), str(new)) + b"\n" for line in self.contents])

        self.update_contents()

    def clear(self):
        
        with open(self.name, "wb"):
            pass
        self.contents = ""
