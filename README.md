<h2>Echoes</h2>
<p><i>Where every echo unveils a new tale </i></p>

<h3>Introduction</h3>
<p>
    For my ALX end of foundations portfolio project, I built a blog platform called echoes.
    Echoes is a blog platform where users can sign up, sign in, and post content. Users can also update their profile, follow and unfollow each other.
</p>
<p>
    I initially didn't know what to build or what tech stack to use. I contemplated learning MERN and using it for my project but it was obvisouly a crazy
    idea because I had only a  month to do this. I decided to use everything I had laerned in ALX so far and it was the best decision I ever made.
</p>

<h3>Languages and frameworks</h3>
<p>
    <h4>Frontend: </h4>
        <ul>
            <li>HTML</li>
            <li>CSS</li>
            <li>Javascript</li>
        </ul>
</p>
<p>
    <h4>Backend:</h4>
        <ul>
            <li>Flask</li>
        </ul>
</p>
<p>
    <h4>DevOps:</h4>
    <ul>
        <li>Digital ocean server</li>
        <li>.tech for hosting</li>
        <li>Nginx web server</li>
        <li>Gunicorn application server</li>
        <li>Certbot for SSL</li>
        <li>UFW firewall</li>
    </ul>
</p>
<p>
    <h4>Database:</h4>
    <ul>
        <li>SQLITE locally</li>
        <li>MYSQL in the server</li>
    </ul>
</p>

<h3>Architecture</h3>
<p>
    I had a hard time deciding on where to start the project. Should I start with the backend and then
    make the frontend? Or should I start with the frontend?
    At this point I had little experince with jinja templates, I did like the syntax and I felt they cluttered my HTML.
    I found it a bit had to style Jinja templates and because of this, I decided to start my project by building the static pages.
    Just having this visual of how the frontend looks like made it easier for me when I was building the backend
</p>
<p>
    Since I used flask, I followed the microframework architecture which helps with separation of concerns.
    Here's a brief breakdown of my file structure;
</p>
<p>
    <h4>Application Logic(app folder)</h4>
    <ol>
        <li><strong>static and templates: </strong>flask uses 'static' folder to serve static assest(CSS, JS and images)
        and 'templates' folder for HTML templates.
        </li>
        <li><strong>Python Modules:</strong>
        <ul>
            <li><strong>email.py: </strong>Handles email-related logic.</li>
            <li><strong>error.py: </strong>Error handling and custom error pages.</li>
            <li><strong>forms.py: </strong>Flask forms to handle user input</li>
            <li><strong>__init__.py: </strong>Marks the 'app' directory as a python package</li>
            <li><strong>models.py: </strong>Defines my database models</li>
            <li><strong>routes.py: </strong>Defines flask routes and views</li>
        </ul></li>
    </ol>
</p>
<p>
    <h4>Configuration and Main Application File</h4>
    <ol>
        <li><strong>config.py: </strong>Holds configuration settings for my flask application</li>
        <li><strong>echoes.py: </strong>Main application module for my flask application. Sets up Flask and provides utility for Flask shell</li>
    </ol>
</p>
<p>
    <h4>Auxillary Directories</h4>
    <ol>
        <li><strong>migrations: </strong>Contains my database migration scripts</li>
        <li><strong>web_static: </strong>Contains my intial static file(with no Jinja)</li>       
    </ol>
</p>
<p>
    <h4>Testing</h4>
    <ul>
         <li><strong>tests.py: </strong> test cases for my flask application</li>
    </ul>
</p>
<p>
    <h4>Documentation</h4>
    <li><strong>README.md: </strong>Provides information about the project</li>
</p>
