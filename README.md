# rest_framework_with_docker

###### Add docker file and build setup ######
###### Follow 17th video on udemy. abm21719@ ######
* `After creating setup run this command : docker build .`

* `After running this command if you get the below error :-->
Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Post http://%2...........`

* `Run these 2 commands : 1. sudo usermod -aG docker ${USER}
                          2. su - ${USER}`

* `Again run this command : docker build .`


###### Then comes to docker-compose.yml file. ######
###### Follow 17th video on udemy. abm21719@ ######
* `after writing all code in docker-compose.yml run this command : docker-compose build`

* `After running this command if you find this error :
ERROR: Version in "./docker-compose.yml" is unsupported. You might be seeing this error because you're using the wrong Compose file version. Either specify a version of "2" (or "2.0") and place your service definitions under the `services` key, or omit the `version` key and place your service definitions at the root of the file to use version 1.
For more on the Compose file format versions, see https://docs.docker.com/compose/compose-file/`


* `Then run these 4 commands :
        1. sudo apt-get remove docker-compose
        2. sudo curl -L "https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
        3. sudo chmod +x /usr/local/bin/docker-compose
        4. sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose`


* `then again run the command : docker-compose build`

###### Create project  ######
* `command : docker-compose run app sh -c "django-admin.py startproject django_api_drf ."`
* `create .travis.yml file`
* `create .flake8 file inside app folder"message: added flake8 and travis CI configuration"`

######  Testing command  ( optional ) ######
* `docker-compose run app sh -c "python manage.py test"`

###### If you find error : flake8: not found ######
* ` Run this command : docker-compose build `


###### Creating app using Docker ######
* `docker-compose run app sh -c "python manage.py startapp core"`

###### Run Migration ######
* `Migration command with docker : docker-compose run app sh -c "python manage.py makemigrations <app_name (its optional)>"`
