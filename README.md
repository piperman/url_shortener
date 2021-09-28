# url_shortener
Flask app of url shortener

Checkout repository

From directory where checked out run:
python -m pip install -r requirements.txt

Be sure to do this from command line:
export FLASK_APP=url_shorten

Once finished, you can start it up with:
flask run

Goto http://127.0.0.1:5000
Enter in a url such as http://www.microsoft.com
When you submit it, it will re-render the page with the short url
You can take the short url and paste it into a browser address bar and run it, it should resolve to original url and take you there.

You can also look at the stats or urls at:
http://127.0.0.1:5000/stats

This took 2 hours to complete, 30 mins of which was getting my new mac to use ssh keys to work with git.
