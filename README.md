# blog-app-django
simple rest api based blog app using django rest framework

<h2>To run this project:</h2>

# Ubuntu
1. sudo apt-get install npm
2. npm i pm2 -g
3. pm2 start run.py --interpreter=python3

# macOS
1. brew install npm
2. npm i pm2 -g
3. pm2 start run.py --interpreter=python3

# stop the instance : 
pm2 stop {id} (eg: pm2 stop 0)

# restart the instance : 
pm2 restart {id} (EG: PM2 restart 0)

# delete the instance : 
pm2 delete {id} (eg: pm2 delete 0)