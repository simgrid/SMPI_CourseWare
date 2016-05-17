---
layout: page
title: About
description: Learning objectives and approach
---


<div class="ui container raised border segment">

<h3 class="ui header">
Target audience
</h3>

<ul class="ui list">

<li class="ui item"> Students/Researchers/Practitioners who want to complement their learning with hands-on experience with distributed-memory programming, message-passing, MPI, and high performance computing</li>
<li class="ui item"> Instructors who want to provide students with compelling hands-on experiences as part of the coursework they develop</i>
</ul>

</div>


<div class="ui container raised border segment">

<h3 class="ui header">
Learning Objectives
</h3>

<b>The broad learning objective of SMPI CourseWare is to learn how to write efficient message-passing
programs that run on distributed-memory architectures, using the MPI standard.</b>

Specific learning objectives include:
<ul class="ui list">
<li class="ui item"> Learn the fundamentals of the MPI API</li>
<li class="ui item"> Understand general distributed-memory programming and learn standard solutions</li>
<li class="ui item"> Learn how to implement distributed-memory programs, going from traditional "rigid" programs to more "dynamic" programs</li>
<li class="ui item"> Understand and experience performance trade-offs when implementing and executing distributed-memory programs on ranges of distributed-memory platforms</li>
</ul>
</div>


<div class="ui container raised border segment">

<h3 class="ui header">
Approach
</h3>

While many curricular materials have been developed for teaching message-passing, MPI, and distributed-memory programming,
this CourseWare relies on the use of _simulation_, which has the following advantages:


<ul class="ui list">
<li class="ui list"> No need to have access to a distributed-memory platform</li>
<li class="ui list"> Ability to run many experiments quickly and reproducibly on one's own computer</li>
<li class="ui list"> Ability to explore arbitrary "what if?" scenarios, in particular to experience performance trade-offs first-hand</li>
</ul>

This CourseWare uses
<a href="http://simgrid.gforge.inria.fr/simgrid/latest/doc/group__SMPI__API.html">SMPI</a> (Simulated MPI),
which is provided as part of the <a href="http://simgrid.gforge.inria.fr">SimGrid</a> project. SMPI simulates the execution of unmodified MPI applications.
</div>