from flask import *
app = Flask(__name__, static_url_path='/static')

@app.route("/")
def main():
	filename = "Playlists on Songza.html"
	return render_template(filename)
	# return send_from_directory('/static', filename)
	# return redirect(url_for('static', filename=filename))

if __name__ == "__main__":
    app.run()