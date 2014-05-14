# Songza Curator Prototype

The idea of this prototype is to demonstrate how Songza could make use of the data of Curators. It shows a list of curators, and on a profile page for the curators, it shows similar curators.

Requirements

 * Python 2.7+
 * MongoDB 2.6+



First, run these commands to setup a virtual environment and to install the required Python modules
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Next, run the setup to retrieve and store all required data into MongoDB
```
python setup.py
```

Then, launch the web server from Flask
```
python app.py
```


Navigate to [http://localhost:5001](http://localhost:5001) to view the prototype!
