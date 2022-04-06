*********
Ansu Fati
*********

Developed with Python 3.9.10.


Run from virtual environment
############################

.. code-block::

    pip install -r requirements.txt
    pytest
    python manage.py logs/data.log
    python manage.py logs/data.log
    python manage.py logs/data.log


Run from Docker
###############

.. code-block::

    docker build -t ansu_fati .
    docker run -it ansu_fati pytest
    docker run -it ansu_fati python manage.py logs/data.log
    docker run -it ansu_fati python manage.py logs/empty.log
    docker run -it ansu_fati python manage.py logs/random.log
