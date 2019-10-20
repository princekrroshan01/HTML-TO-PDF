from flask import Flask,render_template,make_response
import pdfkit


app=Flask(__name__)

@app.route('/<name>/<location>')
def pdfconv(name,location):
    render=render_template('pdfconv.html',name=name,location=location)
    path_wkthmltopdf = 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    #pdfkit.from_url(url=urlpath, output_path=pdffilepath,configuration=config)
    #pdfkit.from_url(url,pdffile,configuration=config)
    pdf=pdfkit.from_string(render,False,configuration=config)

    response=make_response(pdf)
    response.headers['Content-type']='application/pdf'
    response.headers['Content-Disposition']='inline; filename=output.pdf'

    return response


if(__name__=='__main__'):
    app.run(debug=True)
