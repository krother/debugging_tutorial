
# Debugging Python Code

**Debug a series of bugs with a variety of debugging tools**

Debugging is a daily activity of any programmer. Frequently, it is assumed that programmers can debug. However, programmers often have to deal with existing code that simply does not work. This tutorial attempts to change that by introducing concepts for debugging and corresponding programming techniques.

In this tutorial, participants will learn strategies for systematically debugging Python programs. We will work through a series of examples, each with a different kind of bug and with increasing difficulty. The training will be interactive, combining one-person and group activities, to improve your debugging skills in an entertaining way.


## Course Contents

* Syntax Error against Runtime exceptions
* Get file and directory names right
* Debugging with the scientific method
* Inspection of variables with `print`
* Introspection functions
* Using an interactive debugger
* logging

## Duration

1.5-3 hours

## Prerequisites

* Basic knowledge of Python 3

## Preparations

* install Python 3
* install IPython
* install ipdb (`pip install ipdb`)
* clone/download/unzip this repository

## What is in the files?

* `twenty_questions/` - exercise for rehearsing basic debugging techniques
* `proteins/` - debugging exercise for biologists.
* `slides/` - presentation for Jupyter notebook.
* `solution/` - correct version of the program.

## Lesson Plan

If you want to deliver the tutorial yourself, consider the following agenda:

| time | activity | comment |
|------|----------|---------|
|  0'  | explain problem: guess an animal! | |
|  1'  | point to download link | participants may need time |
|  2'  | **motivate the training** | [4MAT-method](http://www.janesunley.com/The-4mat-System) |
|      | WHY: the bigger your program grows, the more important debugging becomes | |
|       | WHAT: show tutorial overview | |
|       | HOW: we will fix a program with many bugs | |
|       | WHAT ELSE: book raffle | |
| | | |
| 5' | **Part I: Basic Debugging Techniques** | |
| | bugfix `twenty_questions/` | slowly walk through bugs |
| | | |
| 40' | Part II: Interactive debugger | |
| | walk through the issue of `mean != 1.0` | see buglist |
| | | |
| 70' | part III: log files | |
| | extend the code by logging | |
| | | |
| 90' | part IV: delta debugging | |
| | run example together | |
| | | |
| 120' | Part IV: Code Review | |
| | participants review the example in `nuke_door/` together | |
| | | |
| 140' | collect other debugging techniques | Q & A |
| 150' | collect feedback and pick book winners | |
| 160' | buffer time | |


## Compiling the slides

    jupyter nbconvert debugging.ipynb --to slides --post serve


## License

(c) Dr. Kristian Rother

The material in this tutorial, unless stated otherwise, is available under the conditions of the Creative Commons Attribution Share-alike License 4.0. See [www.creativecommons.org](http://www.creativecommons.org) for details.

## Contact

krother@academis.eu


## Acknowledgements

This tutorial was made possible by help from: Janick Mathys, Veit Schiele, Susanne Eiswirt, Marie Pilz, José Quesada, Chris Armbruster, Thomas Lotze, Magdalena Rother

## Not covered by the tutorial

* typical pandas table bugs (missing or extra headers, column types)
* error from inside 3rd party libraries
* invalid NAN values
* fixing Heisenbugs and race condition
* Unicode issues
* catching Exceptions
* automated testing
* bugs with wrong filenames, permissions
* mypy


## Trivia

The first computer bug: http://www.computerhistory.org/tdih/September/9/

How patches got their name: https://www.bram.us/wordpress/wp-content/uploads/2017/01/patch.jpg
