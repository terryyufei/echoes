<h2>Echoes</h2>
<p><i>Where every echo unveils a new tale </i></p>

<h3>Introduction</h3>
<p>
    Welcome to Echoes, a blog platform where every echo unveils a new tale. This project was developed as part of my ALX End of Foundations Portfolio. 
    Echoes enables users to sign up, sign in, and share their thoughts through blog posts.
    Additionally, users have the ability to update their profiles, follow, and unfollow each other, fostering a dynamic and engaging community.
    And the best part is that users don't even have to sign up inorder to read the posts!
</p>
<p>
    I initially didn't know what to build or what tech stack to use. I contemplated learning MERN and using it for my project but it was obviously a crazy
    idea because I had only a  month to do this. I decided to use everything I had learned at ALX so far and it was the best decision I ever made.
</p>

<h3>Technology Stack</h3>
<p>
    <h4>Frontend: </h4>
        <ul>
            <li>HTML</li>
            <li>CSS</li>
            <li>JavaScript</li>
        </ul>
</p>
<p>
    <h4>Backend:</h4>
        <ul>
            <li>Flask(Microframework for Python)</li>
        </ul>
</p>
<p>
    <h4>DevOps:</h4>
    <ul>
        <li>Digital ocean server for hosting</li>
        <li>.tech domain for online presence</li>
        <li>Nginx web server for handling HTTP requests</li>
        <li>Gunicorn application server for serving Flask application</li>
        <li>Certbot for SSL encryption</li>
        <li>UFW firewall for security</li>
    </ul>
</p>
<p>
    <h4>Database:</h4>
    <ul>
        <li>SQLITE for local development</li>
        <li>MYSQL for the server</li>
    </ul>
</p>

<h3>Architecture</h3>
<p>
    The decision-making process for the project's architecture involved carefully considering the best approach. 
    A critical choice was whether to start with the backend or frontend development. 
    Given my limited experience with Jinja templates (used by Flask), 
    the decision was made to kickstart the project by building static pages first. 
    This visual representation of the frontend helped streamline the backend development process.
</p>
<p>
    Following the Flask microframework architecture facilitated the separation of concerns, enhancing code organization. 
    The file structure includes:
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
            <li><strong>error.py: </strong>Handles error logic and custom error pages.</li>
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
    <li><strong>README.md: </strong>This document, providing comprehensive information about the project.</li>
</p>

<h3>Getting Started</h3>
<p>
    To set up and run the Echoes project locally, follow these steps:
    <ol>
        <li>Clone the repository</li>
        <li>Navigate to the project directory</li>
        <li>Create a virtual environment</li>
        <li>Activate the virtual environment</li>
        <li>Install the required dependancies</li>
            -pip install -r requirements.txt
    </ol>
</p>
