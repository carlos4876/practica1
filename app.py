from flask import Flask,render_template, request
app = Flask(__name__)
#ruta index.html
@app.route("/",methods = ['GET','POST'])
def index():
        return render_template("index.html")
# Ruta quienes_somos.html
@app.route("/quienes_somos")
def quienes_somos():
    return render_template("quienes_somos.html")

# Ruta servicios.html
@app.route("/servicios")
def servicios():
    return render_template("servicios.html")

# Ruta noticias.html
@app.route("/noticias")
def noticias():
    return render_template("noticias.html")

# Ruta contactos.html

@app.route("/contactos", methods=["GET", "POST"])
def contactos():
    if request.method == 'POST': #MADAMDOS FORMULARIO
     nombre = request.form.get('nombre')
     email = request.form.get('email')
     mensaje = request.form.get('mensaje')
     return render_template("salida.html",nombre =nombre,email=email ,mensaje = mensaje)
    return render_template("contactos.html")

if __name__ == "__main__":
        app.run(debug=True)
