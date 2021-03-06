import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
  name = 'fileedit',         # How you named your package folder (MyLib)
  packages = ['fileedit'],   # Chose the same as "name"
  version = '2.2',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'File editing made easy.',   # Give a short description about your library
  long_description_content_type="text/markdown",
  long_description=long_description,
  author = 'kr8gz',                   # Type in your name
  author_email = 'kr8gz@gmx.at',      # Type in your E-Mail
  url = 'https://github.com/kr8gz/FileEdit',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/kr8gz/fileedit/archive/2.2.tar.gz',    # I explain this later on
  keywords = ['file', 'editing', 'fileedit', 'files', 'edit', 'data'],   # Keywords that define your package best
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
  ],
  python_requires='>=3.8',
)
