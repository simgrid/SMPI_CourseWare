---
layout: page
title: About
description: Curricular information
top_level: true
---

<div class="ui container raised border segment">

<h3 class="ui header">
Target audience
</h3>

<div class="ui list bulleted">

<div class="ui item"> Students/Researchers/Practitioners who want to complement their learning with hands-on experience with distributed-memory programming, message-passing, MPI, and high performance computing</div>
<div class="ui item"> Instructors who want to provide students with compelling hands-on experiences as part of the coursework they develop</div>
</div>

</div>

<div class="ui container raised border segment">

<h3 class="ui header">
Prerequisites
</h3>

<div class="ui list bulleted">
<div class="ui item">Access to a Linux (virtual) machine</div>
<div class="ui item">Some Computer Science background (i.e., a few courses)</div>
<div class="ui item">Basic C programming skills (i.e., a 1-semester course)</div>
<div class="ui item">Elementary Linux command-line skills</div>
<div class="ui item">Access to MPI documentation/tutorials</div>
</div>

</div>




<div class="ui container raised border segment">

<h3 class="ui header">
Learning Objectives
</h3>

<b>The broad learning objective of SMPI CourseWare is to learn how to write efficient message-passing
programs that run on distributed-memory architectures, using the MPI standard.</b>

Specific learning objectives include:
<div class="ui list bulleted">
<div class="ui item"> Learn the fundamentals of the MPI API</div>
<div class="ui item"> Understand general distributed-memory programming and learn standard solutions</div>
<div class="ui item"> Learn how to implement distributed-memory programs, going from traditional "rigid" programs to more "dynamic" programs</div>
<div class="ui item"> Understand and experience performance trade-offs when implementing and executing distributed-memory programs on ranges of distributed-memory platforms</div>
</div>
</div>


<div class="ui container raised border segment">

<h3 class="ui header">
Approach
</h3>

While many curricular materials have been developed for teaching message-passing, MPI, and distributed-memory programming,
this CourseWare relies on the use of _simulation_, which has the following advantages:


<div class="ui list bulleted">
<div class="ui item"> No need to have access to a distributed-memory platform</div>
<div class="ui item"> Ability to run many experiments quickly and reproducibly on one's own computer</div>
<div class="ui item"> Ability to explore arbitrary "what if?" scenarios, in particular to experience performance trade-offs first-hand</div>
</div>

This CourseWare uses
<a href="http://simgrid.gforge.inria.fr/simgrid/latest/doc/group__SMPI__API.html">SMPI</a> (Simulated MPI),
which is provided as part of the <a href="http://simgrid.gforge.inria.fr">SimGrid</a> project. SMPI simulates the execution of unmodified MPI applications.
</div>
