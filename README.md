# HTML-TO-PDF

a simple flask app to convert your website html page to pdf which may be used for machine learning purpose
as the chat app uses websocket were we can't store chat in our database to apply machine learning on data to track user
sentiment analysis 

## installation 

run: pip install -r requirements.txt in your shell

as in virtual environment for windows the executable for pyhton script is
'venv\Scripts' which does not support some of the python third pirty package

and it does not have extra package support like ubuntu which has python-dev


```python
>>> import os
>>> import sys
>>> os.path.dirname(sys.executable)
'\venv\Scripts'
```

if not in virtual environment

```python
>>> import os
>>> import sys
>>> os.path.dirname(sys.executable)
'C:\\Program Files (x86)\\Python37-32'
```

this time python scripts were executed by 
'C:\\Program Files (x86)\\Python37-32'



so configure the path if the package supports like this time it supports

```python
 path_wkthmltopdf = 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    #pdfkit.from_url(url=urlpath, output_path=pdffilepath,configuration=config)
    #pdfkit.from_url(url,pdffile,configuration=config)
    pdf=pdfkit.from_string(render,False,configuration=config)
```

##

