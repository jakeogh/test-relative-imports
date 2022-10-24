This repo is intended to reproduce a error I am encountering while trying to create a project that I can test without first installing. Prior to this, I would always install the module (via emerge) and then test it. I would like to also be able to run the code directly from it's repo `python test_relative_imports.py`.

### Reproduce Error:
```
$ git clone https://github.com/jakeogh/test-relative-import
$ cd test-relative-import
$ python test_relative_imports/test_relative_imports.py
Traceback (most recent call last):
  File "/home/cfg/_myapps/test-relative-imports/test_relative_imports/test_relative_imports.py", line 10, in <module>
    from .cli.gui import gui
ImportError: attempted relative import with no known parent package

```

### Install:
(not necessary to reproduce the error, this just shows that it "works" in the conventional way)

```
$ git clone https://github.com/jakeogh/test-relative-import
$ cd test-relative-import
$ sudo ebuild dev-python/test-relative-import/test-relative-import-9999.ebuild merge

$ test-relative-imports
Usage: test-relative-imports [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  gui

$ test-relative-imports gui
clitest()
gui()

```

