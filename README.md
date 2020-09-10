# FileEdit
File editing made easy.

## Usage

f = File("test.txt")
* Creates a new `File` object from the file `"test.txt"`.
--------------------------------------------------------------------------------
cont = f.contents
* Returns a list where one element is one line of the file.
--------------------------------------------------------------------------------
myvar = cont[3]
* This stores the value of line 3 in `myvar` (without the newline).
--------------------------------------------------------------------------------
f.write("hello world")
* This adds `"hello world"` to the end of the existing text.
--------------------------------------------------------------------------------
f.write(["if you", "pass a list", "it will write", "multiple lines"])
* This adds the following to the existing text:

    ```
    if you
    
    pass a list
    
    it will write
    
    multiple lines
    ```
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
  Using a list or a tuple raises `InvalidArgument`.
--------------------------------------------------------------------------------
important_line = f.find("foo")
* This stores the line number in which "foo" appears first.
  If `"foo"` cannot be found in the file, the function returns `None`.
--------------------------------------------------------------------------------
f.replace("old", "new")
* Every `"old"` that was in the file is now `"new"`.
  If there is no occurrence of `"old"`, nothing happens.
--------------------------------------------------------------------------------
f.replace("old", "new", 7)
f.replace("old", "new", line=7)
* Every `"old"` that was in line 7 is now `"new"`.
  If there is no occurrence of `"old"`, nothing happens.
--------------------------------------------------------------------------------
f.clear()
* This clears the file.
--------------------------------------------------------------------------------
del f
* This deletes the file and the `File` object.
