"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash, session, abort
from flask import send_from_directory
from werkzeug.utils import secure_filename
from app.forms import PropertyForm
from app.models import PropertyProfile


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/property/', methods=['POST', 'GET'])
def property():
    """Render the website's property page."""
    form = PropertyForm()
    if request.method == 'POST' and form.validate_on_submit():
        title = form.title.data
        desc = form.description.data
        nobed = form.nobed.data
        nobath = form.nobed.data
        location = form.location.data
        price = form.price.data
        property_type = form.property_type.data
        photo = form.photo.data

        filename = secure_filename(photo.filename)
        photo.save(os.path.join(
            app.config['UPLOAD_FOLDER'], filename
        ))

        prop = PropertyProfile(title,desc,nobed,nobath,location,price,property_type,filename)
        db.session.add(prop)
        db.session.commit()
        
        flash('Property successfully added.', 'success')
        return redirect(url_for('properties'))
    else:
        flash_errors(form)
    return render_template('property.html', form=form)

@app.route("/property/<path:filename>")
def get_prop(filename):
    root_dir = os.getcwd()
    return send_from_directory(os.path.join(root_dir, app.config['UPLOAD_FOLDER']), filename)

@app.route('/properties/')
def properties():
    """Render the website's properties page."""
    lst = get_properties()
    return render_template('properties.html',items=lst)

@app.route('/property/<path:propertyid>')
def get_property(propertyid):
    root_dir = os.getcwd()
    return send_from_directory(os.path.join(root_dir, app.config['CONFIG_FOLDER']))

###
# The functions below should be applicable to all Flask apps.
###

# Helper function 
def get_properties():
    import os
    rootdir = os.getcwd()
    lst = []
    for subdir, dirs, files in os.walk(rootdir + '/uploads'):
        for file in files:
            lst.append(file)
    lst.pop(0)
    return lst 

# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")

