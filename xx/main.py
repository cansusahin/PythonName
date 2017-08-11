
import cgi

from google.appengine.api import users
import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("""
                  <!DOCTYPE html>
<html lang="tr">
<head>
    <style>body {
   background-image: url("wallpaper-2501884.png");

}

h1 {
    color: PapayaWhip;
     background-image: url("bg-heading.png");
     background-repeat: no-repeat;
     background-position: center;

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
      <link rel="stylesheet" href="styles.css">
    <title>Cansu Özge Şahin</title>
</head>
<body>
     <h1 class="center">Cansu Özge Şahin</h1>

</body>
</html>""")


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)