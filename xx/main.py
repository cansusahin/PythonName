
import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("""<!DOCTYPE html>
<html lang="tr">
<head>
    <style>body {
   background-image: url("https://hdwallpapersbuzz.com/wp-content/uploads/2017/02/Black-3d-hd-wallpapers-1080p-widescreen-31.jpg");

}

h1 {
    color: PapayaWhip;
     background-image: url("https://lh3.googleusercontent.com/-E0P04jAUGRU/TrmH9y4Gz8I/AAAAAAAAKZo/g8V_u06zt8U/s530/base2.png");
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
