# holbertonschool-AirBnB_clone
This is the first step towards building the first full web application: the AirBnB clone. We have to write a command interpreter to manage our own AirBnB objects.

<h4><img src="https://news.airbnb.com/wp-content/uploads/sites/4/2021/07/2014_July@2X.jpg?fit=616%2C616&resize=616%2C616"><br></h4>
<h4>First step: Write a command interpreter to manage your AirBnB objects.</h4>
<p>This is the first step towards building your first full web application: the&nbsp;<strong>AirBnB clone</strong>. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration&hellip;</p>
<p>Each task is linked and will help you to:</p>
<ul>
    <li>put in place a parent class (called&nbsp;<code>BaseModel</code>) to take care of the initialization, serialization and deserialization of your future instances</li>
    <li>create a simple flow of serialization/deserialization: Instance &lt;-&gt; Dictionary &lt;-&gt; JSON string &lt;-&gt; file</li>
    <li>create all classes used for AirBnB (<code>User</code>,&nbsp;<code>State</code>,&nbsp;<code>City</code>,&nbsp;<code>Place</code>&hellip;) that inherit from&nbsp;<code>BaseModel</code></li>
    <li>create the first abstracted storage engine of the project: File storage.</li>
    <li>create all unittests to validate all our classes and storage engine</li>
</ul>

<h3>What&rsquo;s a command interpreter?</h3>
<p>Do you remember the Shell? It&rsquo;s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:</p>
<ul>
    <li>Create a new object (ex: a new User or a new Place)</li>
    <li>Retrieve an object from a file, a database etc&hellip;</li>
    <li>Do operations on objects (count, compute stats, etc&hellip;)</li>
    <li>Update attributes of an object</li>
    <li>Destroy an object</li>
</ul>
General
How to create a Python package
How to create a command interpreter in Python using the cmd module
What is Unit testing and how to implement it in a large project
How to serialize and deserialize a Class
How to write and read a JSON file
How to manage datetime
What is an UUID
What is *args and how to use it
What is **kwargs and how to use it
How to handle named arguments in a function

<h2>Requirements</h2>
<h3>Python Scripts</h3>
<ul>
    <li>Allowed editors:&nbsp;<code>vi</code>,&nbsp;<code>vim</code>,&nbsp;<code>emacs</code></li>
    <li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)</li>
    <li>All your files should end with a new line</li>
    <li>The first line of all your files should be exactly&nbsp;<code>#!/usr/bin/python3</code></li>
    <li>A&nbsp;<code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
    <li>Your code should use the pycodestyle (version&nbsp;<code>2.8.*</code>)</li>
    <li>All your files must be executable</li>
    <li>The length of your files will be tested using&nbsp;<code>wc</code></li>
    <li>All your modules should have a documentation (<code>python3 -c &apos;print(__import__(&quot;my_module&quot;).__doc__)&apos;</code>)</li>
    <li>All your classes should have a documentation (<code>python3 -c &apos;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&apos;</code>)</li>
    <li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c &apos;print(__import__(&quot;my_module&quot;).my_function.__doc__)&apos;</code> and&nbsp;<code>python3 -c &apos;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&apos;</code>)</li>
    <li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
</ul>
<h3>Python Unit Tests</h3>
<ul>
    <li>Allowed editors:&nbsp;<code>vi</code>,&nbsp;<code>vim</code>,&nbsp;<code>emacs</code></li>
    <li>All your files should end with a new line</li>
    <li>All your test files should be inside a folder&nbsp;<code>tests</code></li>
    <li>You have to use the&nbsp;<a href="https://intranet.hbtn.io/rltoken/QX7d4D__xhOJIGIWZBp39g" target="_blank" title="unittest module">unittest module</a></li>
    <li>All your test files should be python files (extension:&nbsp;<code>.py</code>)</li>
    <li>All your test files and folders should start by&nbsp;<code>test_</code></li>
    <li>Your file organization in the tests folder should be the same as your project</li>
    <li>e.g., For&nbsp;<code>models/base_model.py</code>, unit tests must be in:&nbsp;<code>tests/test_models/test_base_model.py</code></li>
    <li>e.g., For&nbsp;<code>models/user.py</code>, unit tests must be in:&nbsp;<code>tests/test_models/test_user.py</code></li>
    <li>All your tests should be executed by using this command:&nbsp;<code>python3 -m unittest discover tests</code></li>
    <li>You can also test file by file by using this command:&nbsp;<code>python3 -m unittest tests/test_models/test_base_model.py</code></li>
    <li>All your modules should have a documentation (<code>python3 -c &apos;print(__import__(&quot;my_module&quot;).__doc__)&apos;</code>)</li>
    <li>All your classes should have a documentation (<code>python3 -c &apos;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&apos;</code>)</li>
    <li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c &apos;print(__import__(&quot;my_module&quot;).my_function.__doc__)&apos;</code> and&nbsp;<code>python3 -c &apos;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&apos;</code>)</li>
    <li>We strongly encourage you to work together on test cases, so that you don&rsquo;t miss any edge case</li>
</ul>
<p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220705%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220705T171150Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e3be5ac919701b1e83176a918fc8f3efeb8988b73d4ac39b46b430750fb8f279"><br></p>
