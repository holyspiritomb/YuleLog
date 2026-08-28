# YuleLog

**Have yourself a Merry Terminal Yule Log ✨**

![Python 3.10](https://badgen.net/static/Python/3.10/blue?icon=python)
![Python 3.11](https://badgen.net/static/Python/3.11/blue?icon=python)
![Python 3.13](https://badgen.net/static/Python/3.13/blue?icon=python)
![Python 3.14](https://badgen.net/static/Python/3.14/blue?icon=python)
![Dockerfile provided](https://badgen.net/static/Dockerfile/provided/blue?icon=docker)

![logo](https://github.com/holyspiritomb/YuleLog/blob/main/yule_log/yule-log.jpg)

## Overview

Yule Log Fireplace with a retro twist!

 - Restart the snowfall by pressing enter.

 - Press `x` to stop the program.

Tested with Python 3.10, 3.11, 3.13 and 3.14 on Termux and Linux.

- **Made with Asciimatics!**

- **WORKS BEST IN FULL SCREEN**

## Installation / Usage

To install:

### With [pipx](https://pipx.pypa.io/stable/) (recommended):

```bash
git clone https://github.com/holyspiritomb/YuleLog.git
cd YuleLog
pipx install .
```
or (in editable mode):

```bash
git clone https://github.com/holyspiritomb/YuleLog.git
cd YuleLog
pipx install -e .
```

### In a [virtualenv](https://docs.python.org/3/library/venv.html):

```bash
git clone https://github.com/holyspiritomb/YuleLog.git
cd YuleLog
python -m venv .venv
source .venv/bin/activate
pip install -r requirements
python setup.py install
```

### For a containerized install with Docker:

```bash
git clone https://github.com/holyspiritomb/YuleLog.git
cd YuleLog
# if desired, edit the dockerfile to change TOP_TEXT and BOTTOM_TEXT
./docker-build.sh
./docker-run.sh
```

## Examples

To run directly from the command line (if installed via pipx):

```bash
YuleLog
```

With customized text:

```bash
TOP_TEXT="HELLO" BOTTOM_TEXT="WORLD" YuleLog
```

With no text:

```bash
TOP_TEXT="" BOTTOM_TEXT="" YuleLog
```

## Changes

Version 0.1.0:
 - Dropped support of python2, as python2 is EOL
 - Upgraded deps for currently supported python versions
 - Changed default text to YULE LOG
 - Made text customizable using `TOP_TEXT` and `BOTTOM_TEXT` environment variables
 - Brought setup.py up to current standards
 - Removed unneeded code from dockerfile
 - Added environment vars to dockerfile for text customization

Version 0.0.3:
 - Fix broken deps

Version 0.0.2:
 - Fixed Fire not showing issue (#1)

Version 0.0.1:
 - First release



## Credits & thanks

 - Asciimatics - https://github.com/peterbrittain/asciimatics
 - Scott Doucet for the original program

## Created by

- Scott Doucet, 2016
- Modified by Hezekiah Michael, 2026
