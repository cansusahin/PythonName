import cgi

from google.appengine.api import users

import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("""<!doctype html>
<html lang="tr">
<head>
    <style>


h1 {
    color: black;

}
.center {
    text-align: center;
}

div {
    width: 320px;
    padding: 10px;
    border: 5px solid gray;
    margin: 0;
}
</style>

    <meta charset="UTF-8">
    <title>Cansu Özge Şahin</title>
</head>
<body>
     <h1 class="center">Cansu Özge Şahin</h1>

</body>
</html>
""")


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
