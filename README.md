# Python-to-Assembly Transpiler  

![Build Status](https://github.com/MatchingSocks/py2asm/actions/workflows/tests.yml/badge.svg)
![Lint Status](https://github.com/MatchingSocks/py2asm/actions/workflows/lint.yml/badge.svg)
![Format Status](https://github.com/MatchingSocks/py2asm/actions/workflows/format.yml/badge.svg)




# Py2asm
An overly-ambitious project to write a Python to Assembly Language transpiler. Wish me luck.

### Overview
Python is regularly recognized as the most widely used high level programming language in the world. With its realtively easy to learn syntax and 3rd party ecosystem, it's no surprise why Python is chosen for an endless amount of use cases with the tradeoff being performance. I'm a firm beliver that Python can be as fast as you are willing to push it using any number of optimization methods supported with clean performant code. However, most of these methods involve translating Python into another lower level language like C which is then converted into some intermediate representation and then compiled into machine code.

Py2asm aims to cut to the intermediate representation (AST) and then convert AST to assembly with pre and post optimization checks built in.


Check back for more updates or maybe think about contributing yourself!