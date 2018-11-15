


<div class="container ui raised segment">
<h3 class="ui header">Overview</h3>

  <p class="ui">This topic focuses on getting you started with SMPI (Simulated MPI)
  so that you are ready for the modules in the next topics. Simply read through the
  4 tabs below:
  </p>
</div>


<div class="ui pointing secondary menu">
  <a class="item active" data-tab="first">Installing SimGrid</a>
  <a class="item " data-tab="second">Platform XML</a>
  <a class="item" data-tab="third">Hello World</a>
  <a class="item" data-tab="fourth">Limitations</a>
</div>




<!-------------------------------------------------->
<!-------------------------------------------------->
<!-------------------------------------------------->
<!-------------------------------------------------->



<div class="ui tab segment active" data-tab="first">

<p class="ui">
<b>
  This CourseWare was tested with <a href="http://simgrid.gforge.inria.fr/">SimGrid</a>
  version 3.13 (small changes <i>may</i> be needed with other versions).
  </b>
</p>

<p class="ui">
  On a <b>recent Debian/Ubuntu (virtual) machine</b>, you can retrieve SimGrid directly from the
  package manager: <code>sudo apt-get install simgrid</code>
  Do not forget to check that you obtained a sufficiently recent version, e.g., by doing <code>apt-cache show libsimgrid-dev</code>.
  If the version you obtain this way is too old, we recommend you to manually install simgrid and to follow the instructions bellow.
</p>

<hr/>
<p class="ui">
  For other systems, please refer to the <a href="http://simgrid.gforge.inria.fr/download.html">Download page</a>
  that have all the information you need. But just to be sure, here is
  a typical way to compile the version you want on a Linux (virtual) box:
</p>

<div class="ui list bulleted">
  <div class="ui item">Install the dependencies: <code>sudo apt-get install g++ libboost-all-dev</code></div>
  <div class="ui item">Download the .tar.gz of the latest stable version from the <a href="http://simgrid.gforge.inria.fr/download.html">Download page</a></div>
  <div class="ui item">Extract the archive: <code>tar -xvf SimGrid-x.x.x.tar.gz</code></div>
  <div class="ui item">Go to the extracted directory: <code>cd SimGrid-x.x.x</code></div>
  <div class="ui item">Generate all makefiles: <code>cmake -DCMAKE_INSTALL_PREFIX=/usr/local -Denable_smpi=on -Denable_documentation=off</code><br> (Assuming you want to install in <code>/usr/local/</code>)</div>
  <div class="ui item">Build: <code>make</code></div>
  <div class="ui item">Run the tests (for the paranoid): <code>make check</code></div>
  <div class="ui item">Install libraries and executables: <code>sudo make install</code></div>
</div>

<p class="ui">
  Assuming your path includes <code>/usr/local/bin</code> (which it should), you now can invoke two new
  commands: <b><code>smpicc</code></b> and <b><code>smpirun</code></b>.
</p>

<hr/>
<p class="ui">
  If you are not a superuser on your system, then you have to install SimGrid in your home directory, say in a directory
  called <code>local</code>, with the modified <code>cmake</code>
  invocation. The binaries are then available as
  <code>~/bin/smpicc</code> and <code>~/bin/smpirun</code>.
</p>

<div class="ui list">
  <div class="ui item"><code>cmake -DCMAKE_INSTALL_PREFIX=$HOME/local/ -Denable_smpi=on -Denable_documentation=off</code></div>
</div>
</div>



<!-------------------------------------------------->
<!-------------------------------------------------->
<!-------------------------------------------------->
<!-------------------------------------------------->



<div class="ui tab segment " data-tab="second">

<p class="ui">
SMPI simulates the execution of MPI applications by relying on the fast and accurate simulation
core provided by <a href="http://simgrid.gforge.inria.fr">SimGrid</a>. The SMPI
  user (you!) must describe simulated platforms (i.e., sets of simulated hosts and network links, with
  some performance characteristics).  The SimGrid documentation provides ample information
  on platform descriptions, which are written in XML.  Below we simply show a series of examples,
  which should be sufficient for our purpose. Note that platform files are typically provided
  in each pedagogic module, but you may have to modify them.
</p>

<div class="ui divider"></div>

<p class="ui">
  <b>A simple 3-host example:</b> At the most basic level, you can describe your simulated platform
  as a graph of hosts and network links. For instance:
</p>

<p style="text-align:center;" class="ui">
  <img align="center" src="../topic_getting_started/3_hosts.jpg" width="240">
</p>


<div class="ui accordion">
  <div class=" title">
    <i class="dropdown icon"></i>
  See the XML platform description file...
  </div>
  <div class=" content">
    <div class="ui container segment">
    {% highlight XML %}
{% include_relative topic_getting_started/3_hosts.xml %}
    {% endhighlight %}
    </div>
  </div>
</div>

<p class="ui">
  In the above XML, note the way in which hosts, links, and routes are defined. Note that all hosts are defined
  with a <code>power</code> (i.e., compute speed in Gflops), and links with a <code>latency</code> (in us)
  and <code>bandwidth</code> (in Mbit/sec). Other units are possible and written as expected.
  By default, routes are symmetrical. See more information on the
  <a href="http://simgrid.gforge.inria.fr">SimGrid Web site</a>.
</p>

<p class="ui">
  This XML file is intended for SimGrid v3.21 or earlier. To
  use it with more recent versions, you may have to convert it using the
  <code>simgrid_update_xml</code> program, as follows:
</p>
<div class="ui list">
  <div class="ui item"><code>simgrid_update_xml 3_hosts.xml</code></div>
</div>


<div class="ui divider"></div>


<p class="ui">
  <b>A homogeneous cluster with a crossbar switch:</b> A very common parallel computing platform is a homogeneous
  cluster in which hosts are interconnected via a crossbar switch with as many ports as hosts, so that any disjoint
  pairs of hosts can communicate concurrently at full speed. For instance:
</p>

<p style="text-align:center;" class="ui">
  <img align="center" src="../topic_getting_started/cluster_crossbar.jpg" width="470">
</p>


<div class="ui accordion">
  <div class=" title">
    <i class="dropdown icon"></i>
    See the XML platform description file...
  </div>
  <div class=" content">
    <div class="ui container segment">
    {% highlight XML %}
{% include_relative topic_getting_started/cluster_crossbar.xml %}
    {% endhighlight %}
    </div>
  </div>
</div>

<p class="ui">
  In the above XML, note that one simply specifies a name prefix and suffix for each host, and then give an integer
  range (in the example the cluster contains 256 hosts). All hosts have the same power (1 Gflop/sec) and are connected to the switch via links with same latency (5 microseconds) and
  bandwidth (125 Mbit/sec). See more information on the
  <a href="http://simgrid.gforge.inria.fr">SimGrid Web site</a>.

</p>

<div class="ui divider"></div>


<p class="ui">
  <b>A homogeneous cluster with a shared backbone:</b> Another popular model for a parallel platform is that of a set of homogeneous
  hosts connected to a shared communication medium, a backbone, with some finite bandwidth capacity and on which communicating host pairs can
  experience contention. For instance:
</p>

<p style="text-align:center;" class="ui">
  <img align="center" src="../topic_getting_started/cluster_backbone.jpg" width="470">
</p>


<div class="ui accordion">
  <div class=" title">
    <i class="dropdown icon"></i>
    See the XML platform description file...
  </div>
  <div class=" content">
    <div class="ui container segment">
    {% highlight XML %}
{% include_relative topic_getting_started/cluster_backbone.xml %}
    {% endhighlight %}
    </div>
  </div>
</div>

<p class="ui">
  In the above XML, note that one specifies the latency and bandwidth of the link that connects a host to the backbone (in this
  example 50 microsec and 125 Mbit/sec), as well
  as the latency and bandwidth of the backbone itself (in this example
  500 microsec and 2.25 Gbit/sec). See more information on the
  <a href="http://simgrid.gforge.inria.fr">SimGrid Web site</a>.

</p>

<div class="ui divider"></div>


<p class="ui">
  <b>Two interconnected clusters:</b> One can connect clusters together and in fact build simulated platforms
  hierarchically in arbitrary fashions. For instance:
</p>

<p style="text-align:center;" class="ui">
  <img align="center" src="../topic_getting_started/2_clusters.jpg" width="470">
</p>


<div class="ui accordion">
  <div class=" title">
    <i class="dropdown icon"></i>
    See the XML platform description file...
  </div>
  <div class=" content">
    <div class="ui container segment">
    {% highlight XML %}
    {% include_relative topic_getting_started/2_clusters.xml %}
    {% endhighlight %}
    </div>
  </div>
</div>

<p class="ui">
  The above XML is a bit more involved. See all details and documentation on the
  <a href="http://simgrid.gforge.inria.fr">SimGrid Web site</a>.

</p>

<div class="ui divider"></div>

</div>




<!-------------------------------------------------->
<!-------------------------------------------------->
<!-------------------------------------------------->
<!-------------------------------------------------->






<div class="ui tab segment" data-tab="third">

<p class="ui">
We are now ready to simulate the execution of an MPI program using SMPI. Let us use the following simple
  MPI program,
  <a href="../topic_getting_started/roundtrip.c"><code>roundtrip.c</code></a>, in which the processes pass around a message and
  print the elpased time:
  </p>


<div class="ui accordion">
  <div class=" title">
    <i class="dropdown icon"></i>
    See the code of <a href="../topic_getting_started/roundtrip.c"><code>roundtrip.c</code></a>...
  </div>
  <div class=" content">
    <div class="ui container segment">
      {% highlight C %}
{% include_relative topic_getting_started/roundtrip.c %}
  {% endhighlight %}
    </div>
  </div>
</div>


<p class="ui">
  Say we want to simulate the execution of this program on a homogeneous cluster, such as the one we saw
  in the "XML Platforms" tab: <a href="../topic_getting_started/cluster_crossbar.xml">cluster_crossbar.xml</a>.
  We need an "MPI host file", that is a simple text file that lists all hosts on which we wish to
  start an MPI process: <a href="../topic_getting_started/cluster_hostfile.txt">cluster_hostfile.txt</a>.
</p>

<p class="ui">Compiling the program is straightforward:</p>
<div class="ui segment raised">
{% highlight text %}
  % smpicc -O4 roundtrip.c -o roundtrip
{% endhighlight %}
</div>

<p class="ui">Running (simulating) it using 16 hosts on the cluster is done as follows:</p>

<div class="ui segment raised">
{% highlight text %}
  % smpirun -np 16 -hostfile ./cluster_hostfile.txt -platform ./cluster_crossbar.xml ./roundtrip
{% endhighlight %}
</div>

<div class="ui list bulleted">

<div class="ui item">The <code>-np 16</code> option, just like in regular MPI, specifies the number of MPI processes to use. </div>
<div class="ui item">The <code>-hostfile ./cluster_hostfile.txt</code> option, just like in regular MPI, specifies the host file. </div>
<div class="ui item">The <code>-platform ./cluster_crossbar.xml</code> option, <b>which doesn't exist in regular MPI</b>, specifies the platform configuration to be simulated. </div>
<div class="ui item">At the end of the command, one finds the executable name and command-line arguments (in this case there are none).</div>

</div>


<p class="ui">
You will see some warnings/information regarding setting some SMPI configuration parameters. Ignore them for now. One of them will say something about not setting the power of the host running the simulation. This is fine here because in this small example we wish only to simulate the network. 
</p>

<p class="ui">
  Feel free to tweak the content of the XML platform file and the program to see the effect on the simulated execution time.  Note that
  the simulation accounts for realistic network protocol effects and MPI implementation effects. As a result, you may see
  "unexpected behavior" like in the real world (e.g., sending a message 1 byte larger may lead to significant higher
  execution time).
</p>

</div>





<!-------------------------------------------------->
<!-------------------------------------------------->
<!-------------------------------------------------->
<!-------------------------------------------------->




<div class="ui tab segment" data-tab="fourth">

<p class="ui">
  SMPI is robust, but it still has some limitations, as listed (and further explained) below:
</p>


<div class="ui accordion">

  <div class="ui container segment">

    <div class=" title">
      <h4 class="header"><i class="dropdown icon"></i> Do not use global variables that should be distinct across MPI
        processes</h4>
    </div>
    <div class=" content">
      SMPI runs your MPI processes as threads within a single process. So when you declare a global variable in your
      program
      (which is rarely a good idea anyway), all the threads will share it, as threads do. That's likely not what you
      want
      in terms of your MPI processes. Use local variables instead.
    </div>
  </div>

  <div class="ui container segment">

    <div class=" title">
      <h4 class="header">
        <i class="dropdown icon"></i>
        Do not use multithreading in your program
      </h4>
    </div>
    <div class=" content">
      Because SMPI already uses multithreading to simulate your MPI program's execution, if your MPI program uses
      threads
      as well, mayhem can occur. In practice, i.e., with real MPI, you typically want to use threads to exploit
      multi-core
      machines. In these pedagogic modules, simply pretend that each host is single-core and that you don't need to use
      threads.
      This has no impact on your learning MPI, and if/when you transition to real (as opposed to simulated) MPI
      executions, you
      can then simply multi-thread computational sections of your code.
    </div>
  </div>

  <div class="ui container segment">

    <div class=" title">
      <h4 class="header">
        <i class="dropdown icon"></i>
        Don't make your C code weird
      </h4>
    </div>
    <div class=" content">
      Yes, this is vague. <code>smpicc</code> compiles your code, and is fairly robust. But if you go crazy with
      tons of macros and C oddness, <code>smpicc</code> may get confused. It should happen only in rather extreme
      cases, but you are now warned.
    </div>
  </div>

</div>
</div>



