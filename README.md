# FileEdit
File editing made easy.

## Usage

`f = File("test.txt")`
* Creates a new `File` object from the file "test.txt".
--------------------------------------------------------------------------------
`bf = ByteFile("test.docx")`
* Creates a new `ByteFile` object from the file "test.docx".
--------------------------------------------------------------------------------
`contents = f.contents`
* Returns a list where one element is one line of the file.
--------------------------------------------------------------------------------
`myvar = contents[3]`
* This stores the value of line 4 in `myvar` without the newline.
  (Python indexing system!)
--------------------------------------------------------------------------------
`anothervar = str(f)`
* This converts the whole file into a string, with each line separated by
  newlines.
* This does the same as:
`anothervar = "\n".join(f.contents)`
--------------------------------------------------------------------------------
`f.write("hello world")`
* This adds "hello world" to the end of the existing text.
--------------------------------------------------------------------------------
`f.write(["if you", "pass a list", "it will write", "multiple lines", 123])`
* This adds the following to the existing text:
    ```
    if you
    pass a list
    it will write
    multiple lines
    123
    ```
--------------------------------------------------------------------------------
`f.write("I am the new line 4, moving all text below me one line down", 3)`
`f.write("I am the new line 4, moving all text below me one line down", line=3)`
* This inserts the text at line 4, with the new text being the new line 4.
  (Python indexing system!)
--------------------------------------------------------------------------------
`f.overwrite("all the text is now replaced by me")`
* This does the same as:
```
f.clear()
f.write("all the text is now replaced by me")
```
--------------------------------------------------------------------------------
`f.overwrite("I am the new line 6, old line 6 is now gone", 5)`
`f.overwrite("I am the new line 6, old line 6 is now gone", line=5)`
* This replaces line 6 with the new text.
  Note: If you specify the line, you can only pass a string.
  Using a list or a tuple raises `InvalidArgument`.
  (Python indexing system!)
--------------------------------------------------------------------------------
`important_line_number = f.find("foo")`
* This stores the line number in which "foo" appears first.
  If "foo" cannot be found in the file, the function returns `None`.
--------------------------------------------------------------------------------
`some_line = f.contents[f.find("bar")]`
* This stores the whole line in which "bar" was found first.
--------------------------------------------------------------------------------
`f.replace("old", "new")`
* Every "old" that was in the file is now "new".
  If there is no occurrence of "old", nothing happens.
--------------------------------------------------------------------------------
`f.clear()`
* This clears the file.
--------------------------------------------------------------------------------
`del f`
* This deletes the file and the `File` object.
