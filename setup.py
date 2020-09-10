from distutils.core import setup
setup(
  name = 'fileedit',         # How you named your package folder (MyLib)
  packages = ['fileedit'],   # Chose the same as "name"
  version = '1.13',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'File editing made easy.',   # Give a short description about your library
  long_description_content_type="text/markdown",
  long_description = """
# FileEdit
File editing made easy.

## Usage

`f = File("test.txt")`
* Creates a new `File` object from the file `"test.txt"`.
--------------------------------------------------------------------------------
`cont = f.contents`
* Returns a list where one element is one line of the file.
--------------------------------------------------------------------------------
`myvar = cont[3]`
* This stores the value of line 3 in `myvar` (without the newline).
--------------------------------------------------------------------------------
`f.write("hello world")`
* This adds `"hello world"` to the end of the existing text.
--------------------------------------------------------------------------------
`f.write(["if you", "pass a list", "it will write", "multiple lines"])`
* This adds the following to the existing text:

    ```
    if you    
    pass a list
    it will write    
    multiple lines
    ```
--------------------------------------------------------------------------------
`f.write("I am the new line 4, moving all text below me one line down", 4)`

`f.write("I am the new line 4, moving all text below me one line down", line=4)`
* This inserts the text at line 4, with the new text being the new line 4.
--------------------------------------------------------------------------------
`f.overwrite("all the text is now replaced by me")`
* This does the same as:

```
f.clear()
f.write("all the text is now replaced by me")
```

--------------------------------------------------------------------------------
`f.overwrite("I am the new line 6, old line 6 is now gone", 6)`

`f.overwrite("I am the new line 6, old line 6 is now gone", line=6)`
* This replaces line 6 with the new text.
  Note: If you specify the line, you can only pass a string.
  Using a list or a tuple raises `InvalidArgument`.
--------------------------------------------------------------------------------
`important_line = f.find("foo")`
* This stores the line number in which "foo" appears first.
  If `"foo"` cannot be found in the file, the function returns `None`.
--------------------------------------------------------------------------------
`f.replace("old", "new")`
* Every `"old"` that was in the file is now `"new"`.
  If there is no occurrence of `"old"`, nothing happens.
--------------------------------------------------------------------------------
`f.replace("old", "new", 7)`

`f.replace("old", "new", line=7)`
* Every `"old"` that was in line 7 is now `"new"`.
  If there is no occurrence of `"old"`, nothing happens.
--------------------------------------------------------------------------------
`f.clear()`
* This clears the file.
--------------------------------------------------------------------------------
`del f`
* This deletes the file and the `File` object.
""",
  author = 'kr8gz',                   # Type in your name
  author_email = 'kr8gz@gmx.at',      # Type in your E-Mail
  url = 'https://github.com/kr8gz/FileEdit',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/kr8gz/fileedit/archive/1.13.tar.gz',    # I explain this later on
  keywords = ['file', 'editing', 'fileedit', 'files', 'edit', 'data'],   # Keywords that define your package best
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
