# Apache-Airflow-Starter

1. Set the user id with `echo -e "AIRFLOW_UID=$(id -u)" > .env`
2. On all operating systems, you need to run database migrations and create the first user account. To do it, run `docker-compose up airflow-init`
3. Run `docker-compose up`

# Setting up the virtual environment

Conda is the preferred environment manager for my python ecosystem. I have worked with `python 3.7.1`

```
conda create -n aflow python=3.7 pip --y
conda activate aflow
```

Now we can install the packages.

```
pip install -r requirements.txt
```

# Setting up the airflow environment

Do the following or run `bash setup_airflow.sh`

```
# Configurations
export AIRFLOW_HOME=${PWD}/airflow
AIRFLOW_VERSION=2.0.1
PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

# Install Airflow (may need to upgrade pip)
pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

# Initialize DB (SQLite by default)
airflow db init
```

Change few configurations by doing the following:

```
# Inside airflow.cfg
enable_xcom_pickling = True  # needed for Great Expectations airflow provider
load_examples = False  # don't clutter webserver with examples
```

Reset airflow db with the following script and set the admin password `admin`.

```
bash init_airflow_db.sh
```

Launch webserver with the following script.

```
bash start_airflow.sh
```

Credentials:

```
user: admin
password: admin
```

Now you can login to the web `http://localhost:8080/`

To stop the webserver and scheduler, use the following script.

```
bash stop_airflow.sh
```
