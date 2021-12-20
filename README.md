# Apache-Airflow-Starter

## Setting up the virtual environment

Conda is the preferred environment manager for my python ecosystem. I have worked with `python 3.7.1`

```
conda create -n aflow python=3.7 pip --y
conda activate aflow
```

Now we can install the packages required for the project by doing this or manually.

```
pip install -r requirements.txt
```

## Setting up the airflow environment

> Note: You should activate the conda environment before running the following commands.

1. Do the following or run `bash setup_airflow.sh`.

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

2. Change few configurations by doing the following:

```
# Inside airflow.cfg
enable_xcom_pickling = True  # needed for Great Expectations airflow provider
load_examples = False  # don't clutter webserver with examples
```

3. Reset airflow db with the following script and set the admin password `admin`.

```
bash init_airflow_db.sh
```

4. Launch webserver with the following script.

```
bash start_airflow.sh
```

Credentials:

```
user: admin
password: admin
```

If you issue login then try this `FLASK_APP=airflow.www.app flask fab reset-password` or `FLASK_APP=airflow.www.app flask fab create-admin`

Now you can login to the web `http://localhost:8080/`

5. To stop the webserver and scheduler, use the following script.

```
bash stop_airflow.sh
```
