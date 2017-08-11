
import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("""<!doctype html>
<html lang="tr">
<head>
    <style>
    body {
background-color: powderblue;
}

h1 {
    color: PapayaWhip;
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
    <title>Cansu Ozge Sahin</title>
</head>
<body>
     <h1 class="center">Cansu Ozge Sahin</h1>

</body>
</html>
""")


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
