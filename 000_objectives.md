---
layout: page
title: Objectives
description: Learning objectives and approach
---
### Target audience

* Students/Researchers/Practitioners who want to complement their learning with hands-on experience with distributed-memory programming, message-passing, MPI, and high performance computing
* Instructors who want to provide students with compelling hands-on experiences as part of the coursework they develop

### Learning objectives

**The broad learning objective of SMPI CourseWare is to learn how to write efficient message-passing
programs that run on distributed-memory architectures, using the MPI standard.**


Specific learning objectives include:

* Learn the fundamentals of the MPI API
* Understand general distributed-memory programming and learn standard solutions
* Learn how to implement distributed-memory programs, going from traditional "rigid" programs to more "dynamic" programs
* Understand and experience performance trade-offs when implementing and executing distributed-memory programs on ranges of distributed-memory platforms

### Approach

While many curricular materials have been developed for teaching message-passing, MPI, and distributed-memory programming,
this CourseWare relies on the use of _simulation_, which has the following advantages:

* No need to have access to a distributed-memory platform
* Ability to run many experiments quickly and reproducibly on one's own computer
* Ability to explore arbitrary "what if?" scenarios, in particular to experience performance trade-offs first-hand

This CourseWare uses [SMPI](http://simgrid.gforge.inria.fr/simgrid/latest/doc/group__SMPI__API.html) (Simulated MPI),
which is provided as part of the [SimGrid](http://simgrid.gforge.inria.fr) project. SMPI simulates the execution of unmodified MPI applications.
