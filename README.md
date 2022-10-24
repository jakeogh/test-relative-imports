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

### Why:
```
$ scalene /usr/bin/test-relative-imports
Usage: python -m scalene.test-relative-imports [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  gui
Scalene: An exception of type FileNotFoundError occurred. Arguments:
(2, 'No such file or directory')
Traceback (most recent call last):
  File "/home/user/.local/lib/python3.10/site-packages/scalene/scalene_profiler.py", line 1885, in run_profiler
    exit_status = profiler.profile_code(
  File "/home/user/.local/lib/python3.10/site-packages/scalene/scalene_profiler.py", line 1652, in profile_code
    did_output = Scalene.output_profile()
  File "/home/user/.local/lib/python3.10/site-packages/scalene/scalene_profiler.py", line 789, in output_profile
    json_output = Scalene.__json.output_profiles(
  File "/home/user/.local/lib/python3.10/site-packages/scalene/scalene_json.py", line 333, in output_profiles
    with open(full_fname, "r", encoding="utf-8") as source_file:
FileNotFoundError: [Errno 2] No such file or directory: '/home/cfg/_myapps/test-relative-imports/<frozen importlib._bootstrap_external>'
```
