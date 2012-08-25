CS 291: Scientific Software Engineering
=======================================

- - - - -

Introduction (Katzgraber2010)
-----------------------------

* Define your problem
* Choose a programming language
* Write the program: style and document as you go
* Keep your source pure: version control
* Unit testing
* Compilers
* Makefiles
* Debugging (gdb/valgrind/compiler options)
* Profiling
* Running on clusters
* Using other libraries
* Visualization

- - - - -

Defining the problem
--------------------

The single greatest problem I observe in student programmers is that
they do not really understand their problems. This is, perhaps,
natural as students are frequently implementing an algorithm to
increase their understanding. I would point out that you cannot hope
to make a computer do something that you yourself do not
understand. The first step in learning to engineer scientific software
is to understand well the data and algorithms which are involved.

- - - - -

Programming language choice
--------------------------

Many times students/researchers are looking for an easy way out. They
want to learn one language that will serve them for everything that
they do. There is no such language, many have different strengths and
also weaknesses. How do you decide?

### Traditional programming (C,C++,Fortran,Java)

* Does the application implement complex algorithms and/or data
structures where low level control of implementation details is
critical?
* Does the application manipulate large data-sets and thus the memory
has to be carefully controlled?
* Are you not likely to be changing the code once it is programmed?

### Scripting (bash,python,perl,matlab)

* Your application's main task is to connected existing components
* The application depends on manipulating text
* The design of the application is expected to change over its life
* The CPU-intensive parts of your application may be migrated to C or Fortran
* Your application is largely based on common objects

- - - - -

Style and Documentation
-----------------------

Just as in prose or poetry, computer codes should be written with
style. Depending on the language being used, there are guidelines
which should be followed which dictate aspects of coding such as:
spacing, parenthesis, variable and function names. As you write your
code it is also important to keep notes in the comments. If you are
implementing an algorithm from a book or paper, include equation and
page numbers. This will help you to recall later what it was that you
were doing. In many cases, it is better to use variable names and
orgranization which makes the intent of the code clear. Comments
should be used, however an excess of comments can be visually
distracting.

- - - - -

Version control
---------------

Version control systems are great for keeping track of changes you
make to your codes, even if you are the only person working on the
code. However, they are particularly useful when collaborating with
others and if you decide to make your codes available for open use.

* Tutorial for git
* Tutorial for mercurial

- - - - -

Unit testing
------------

Scientific codes require that the answer be correct. In fact, at
times, the answers for one run of the code might seem correct, but
another run at an increased resolution reveals sub-optimal
convergence. These can be very difficult errors to find and fix. The
idea of unit testing is to create a barrage of small tests that prove
basic functionality of your overall code. This way, you can have
confidence in these code portions which makes finding small errors far
simpler. Any time you make a change to the code, before you commit it
to the repository, you must first show that the change does not break
the unit tests.

* using makefiles to run unit tests
* built-in testing in python documentation

- - - - -

Compilers and Makefiles
-----------------------

We will discuss differences in compilers, but mostly focus on the GNU
compilers. We will highlight which flags are particularly useful for
debugging as well as performance.

The 'make' system is a tool for the automated compilation of
codes. They make the process more efficient by only compiling the
codes for which the source has changed. They also help make your codes
portable across different systems.

- - - - -

Performance analysis and debugging
----------------------------------

* How can I improve my code and find bottlenecks?
* How do I know my code is good?

- - - - -

Running on clusters
-------------------

* modules
* submission scripts and systems

- - - - -

Other scientific libraries
--------------------------

Building your software on top of other tools can save you a lot of
time and help you reach a larger audience.

* PETSc, TAO, SLEPc 
* Trilinos
* deal.II, Libmesh

- - - - -

Data visualization tools
------------------------

Scientific computing is not just about numbers--it is about
communication of ideas. It is perhaps unfortunate, but even scientists
are not exempt from the powerful effect of a pretty picture. Learning
to create them has a lot to do with understanding the formats that are
used and how to get your data into them. We will look at:

* matplotlib via python (similar to Matlab)
* vtk file format (mesh-based visualization)
* Paraview, VisIt
* potentially hdf5 pending interest and time

- - - - -


Aside: Making your MAC compute ready
------------------------------------

* Instructions are sufficient but maybe not necessary
* You will need administration access
* Upgrade to at least Lion
* Download Xcode, Preferences, Downloads, Command-line tools
* Download compilers from http://hpc.sourceforge.net/
* Download/compile/install mpich2

- - - - -

Aside: Wrapping legacy codes using python
-----------------------------------------

* Use f2py to call fortran/C code from within python


- - - - -

Aside: The role of software in science
--------------------------------------

The ability to implement algorithms efficienctly is under-appreciated
in academia. We will spend some time discussing this and reading
current opinions.
