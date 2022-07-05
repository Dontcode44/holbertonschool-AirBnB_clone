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
