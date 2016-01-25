from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index_page():
    """Show an index page."""
    return render_template("index.html")

@app.route('/application', methods=['GET', 'POST'])
def application_page():
    """Shows the application page where user inputs form about job type and job requirements."""
    return render_template("application-form.html")

@app.route('/application-form', methods=['GET', 'POST'])
def application_response():
    """Shows the user's response from previous form to confirm user's input."""
    print "!!!!!!!!!!!!!!!_-----------------------------"
    print"LOOK AT ME HEREEEEEEEEHELLOOOOOOO!!!!!!--------------"
    first = request.form.get("firstname")
    print 'first'
    last = request.form.get("lastname")
    print 'last'
    salary = request.form.get("salaryreq")
    print 'salary'
    job = request.form.get("jobtype")
    print 'job'
    return render_template("application-response.html",
                            firstname=first,
                            lastname=last,
                            salaryreq=salary,
                            jobtype=job)

if __name__ == "__main__":
    app.run(debug=True)
