<h2>Echoes</h2>
<p><i>Where every echo unveils a new tale </i></p>

<h3>Introduction</h3>
<p>
    Welcome to <a href="https://echoesblog.tech/index">Echoes,</a>  a blog platform where every echo unveils a new tale. This project was developed as part of my ALX End of Foundations Portfolio. 
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
            <em>pip install -r requirements.txt</em> 
        <li>Run the Flask application</li>
            <em>flask run or flask run --debug</em>
        <li>Acess the application</li>
            <em>http://127.0.0.1:5000/</em>
    </ol>
</p>
<p>
   Now you have the Echoes project up and running locally. Feel free to explore, make changes, 
   and contribute to the project! 
</p>

<h3>Deployment and Hosting</h3>
<p>
    Echoes is hosted on a .tech domain. Purchase a domain name on .tech and add A records 
    pointing to your server's IP address.
</p>
<p>
    Echoes was deployed on a Digital Ocean server. Follow these steps for deployment.
    <ol>
        <li>Set up a Digital Ocean Droplet:
            <ul>
                <li>Create a new droplet</li>
                <li>Choose a distribution(eg Ubuntu)</li>
                <li>Set up SSH access and log in to your Droplet from your local terminal</li>
                <li>Create a less privileged user and give them sudo privileges</li>
                <li>Set up SSH for the user by adding your public into .ssh</li>
                <li>Exit and SSH into the droplet as the less privileged user</li>
            </ul>
        </li>
        <li>Secure your server with UFW</li>
        <li>Clone the repository</li>
        <li>Navigate to the project directory</li>
        <li>Create a virtual environment</li>
        <li>Activate the virtual environment</li>
        <li>Install dependancies</li>
        <li>Configure the application (modify config.py to match server configuration)</li>
        <li>Install, set up MYSQL and upgrade the database</li>
        <li>Install and configure Nginx</li>
        <li>Install and configure Gunicorn </li>
        <li>Setup SSL with Certbot</li>
        <li>Visit your domain</li>        
    </ol>
</p>

<h3>Acknowledgments</h3>
<p>
    I want to express my gratitude to the following resources and individuals who greatly 
    contributed to the development of the Echoes project:
</p>

<h4>Resources: </h4>
<p>
    <ol>
        <li><a href="https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world">The flask mega tutorial</a></li>
        <li><a href="https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-22-04">Digital Ocean gunicorn installation</a></li>
        <li><a href="https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-22-04">Digital Ocean Nginx installation</a></li>
        <li><a href="https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-22-04">Digital Ocean Server setup</a></li>
        <li><a href="https://flask.palletsprojects.com/en/3.0.x/"></a>Flask Documentation</li>
        <li>chatGPT</li>
    </ol>
</p>

<h4>Individuals: </h4>
<p>
    <ol>
        <li>My mentor, <a href="https://github.com/muindetuva">Alfred</a>
            A heartfelt thank you to my mentor for providing guidance, support, and valuable insights throughout the development of Echoes. 
            Their expertise and encouragement were crucial in overcoming challenges and improving the project.
        </li>
        <li>
            My friend, <a href="https://github.com/astianmuchui">Sebastian</a>
            who makes the most beautiful websites and inspires me everyday to become the best 
            developer. His constructive feedback and collaborative efforts significantly enhanced the quality of the project.
        </li>
        <li>
            My friend, <a href="https://github.com/WinnieNgina">Winnie</a>
            A special thanks for being my personal rubberduck, for actively participated in discussions, brainstorming sessions, and code reviews.
            And for believing in me even when I didn't.
        </li>
        <li>
            I want to acknowledge the ALX community and the wider community of developers and contributors whose open-source projects, discussions, 
            and code snippets served as a source of inspiration and learning.
        </li>
    </ol>
</p>
<p>
    I wouldn't have been able to complete this project without the support of these resources and individuals. 
    Your contributions have been invaluable, and I am grateful for the knowledge, encouragement, 
    and camaraderie that fueled the development of Echoes. Thank you!
</p>
