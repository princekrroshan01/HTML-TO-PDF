# HTML-TO-PDF

* A simple flask app to demonstrate the conversion of your website html page to pdf which may be used for machine learning purpose.
* As the chat app uses websocket  we can't store chat in our database to apply machine learning on data to track user sentiment analysis. 


## Prerequisites 

pip install -r requirements.txt 


## General info

* As in virtual environment for windows the executable for python script is
'venv\Scripts' which does not support execution of binaries.  

* Also It does not have extra package support like ubuntu which has python-dev.

```
>>> import os
>>> import sys
>>> os.path.dirname(sys.executable)
'\venv\Scripts'

```

if not in virtual environment
<br>
Steps to check executable path 

```
>>> import os
>>> import sys
>>> os.path.dirname(sys.executable)
'C:\\Program Files (x86)\\Python37-32'
```

This time python scripts are executed by <br>
'C:\\Program Files (x86)\\Python37-32'

Problem arises here as library needs exection of a binary for PDF conversion and virtual environment has some problem with path configuration to execute the binary.

* Will research on it in future.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change
