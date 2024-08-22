0x1A-application server
first task solution >>
1- create the repo
2- create the README.md file 
3- clone the AirBnB repo into the server
4- install nginx in the server
5- install flask in server
6- sudo apt install -y net-tools
7- modify the 0-hello_route.py to rout /airbnb-onepage/ on port 5000

task 2 steps

 pip install gunicorn
task 3 

task 3 steps 

1- write the config file 
2- transfer it to the server 
3-Move the configuration file to the Nginx directory:
sudo mv ~/2-app_server-nginx_config /etc/nginx/sites-available/

4-Create a symbolic link to enable the site:
sudo ln -s /etc/nginx/sites-available/2-app_server-nginx_config /etc/nginx/sites-enabled/

5-Remove the default Nginx configuration if it exists:
sudo rm /etc/nginx/sites-enabled/default

6-Test the Nginx configuration:
sudo nginx -t

7-sudo systemctl reload ngnix 
sudo systemctl reload nginx

8- run the gunicorn with flask app 
gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app
