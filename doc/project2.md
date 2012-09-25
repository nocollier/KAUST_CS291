Project 2
=========

- - - - -

The assignment
--------------

Take a code project and apply what we have learned to improve its
organization and reliability. You are free (and encouraged) to use
your own codes for this project. To make grading simpler, I am
requiring that you use git for version control. Note that you do not
need to upload this repository to an online hosting site. I ask that
you zip the folder with the code project (and repository) inside and
submit this as deliverable.

The code project must require the use of a compiler (e.g. fortran, c,
c++). While you can certainly apply software engineering principles to
scripted languages, in this project I want to test your ability to
compile projects. If you do not have such a code project, check out
the course repository for examples which you can use.

### Due date: 9 October 2012, in my email inbox by 11:59pm 

- - - - -

Suggested procedure
-------------------

1. Initialize a repository for the repository and checkin the code as
it is currently
2. Add a makefile to the project which compiles the necessary components
3. Add two sets of compile options, one for debugging and one for
optimized builds
4. Add a target which will compile the code for profiling and generate
a datafile with profile information (the '-pg' options and using
gprof)
5. Create at least one unit test for the code and add it to the
makefile as a target

- - - - - 

Why this project?
-----------------

The second project will ask you to use all the skills we have
developed up to this point.

1. version control 
2. makefiles
3. debugging
4. performance analysis
5. unit tests
6. code organization

- - - - -

Grading
-------

The second project will ask you to use all the skills we have
developed up to this point. No report is needed, I will grade you
entirely by looking for the following criteria in your repository.

### version control

Did you commit at each stage of your project? Did you make small
commits that add functionality to the code? Did you use meaningful
comments at each commit? Do you track files that you should (like
source code, makefiles, etc.)? Do you track files you should not (.o
files, executables)?

### makefiles

Did you construct a makefile which works? Is it simple to read and
adjust? Did you make use of implicit rules? Did you make use of key
macros (like CC, FFLAGS, CFLAGS)?

### debugging

Does the code execute successfully? Does the code have memory errors?
Did you use debug compiler flags to identify potential errors in the
code?

- - - - -

Grading
-------

### performance

Did you setup a profiling target to your makefile which generates the
gprof 'flatfile' containing profiling information? Did you identify
bottlenecks in your code? Did you look to see if you can improve them?

### unit tests

Did you add at least one test code to the repository? Is there a
target which runs all your tests? Is it simple to verify if code
changes have violated any tests?

### code organization

Did you add a README file to explain what the code does and how one
compiles and uses the code? Did you specify which libraries the user
will need to have installed? Is this easy to setup in the makefile? 

- - - - -

http://software-carpentry.org/
==============================

- - - - -

DAZZLE ME WITH YOUR MAD SKILLZ
==============================

- - - - -

For next class
--------------

http://dirkgorissen.com/2012/09/13/the-research-software-engineer/#more-689

