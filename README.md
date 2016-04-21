# Stone Blocks
Manager your granite blocks

### Used colors
 
 * Primary: #4C007F
 * Secundary: #777777
 * Auxiliary: #B64CFF
 * Auxiliary: #9700FF

* Requires Python3

### Clone the project

```shell
$ git clone git@github.com:jesuejunior/stone.git
```

```shell
$ cd stone
```
### Install virtualenv 

It's better and easy if you use _virtualenv_ 

 * On Unix-like

``` $ sudo apt-get install python-pip ```

 * On OSX

```sudo easy_install pip```

### Install virtualenvwrapper via PIP

```shell
$ sudo pip install virtualenvwrapper 
```

### Creating virtualenv on Unix-like with Python3

```shell
$ mkvirtualenv --python=/usr/bin/python3 stone
```

### Creating virtualenv on OSX with Python3

```shell
$ mkvirtualenv --python=/usr/local/bin/python3 stone
```

### Install dependencies for the project

```shell
$ pip install -r requirements.txt
```

### Create a container of PostgreSQL if you don't have docker installed you will need run PostgreSQL instance locally

```shell
docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=123456 -e POSTGRES_USER=postgres -e POSTGRES_DB=stone -d postgres
```

### Run migrations

```shell
$ python manager.py migrate auth && python manager.py migrate
```

### Run syncdb to create an admin user

```shell
$ python manager.py syncdb
```

### Run all tests

```shell
$ py.test
```

### Run server on development mode

```shell
$ python manager.py runserver
```


