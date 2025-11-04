from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Deployment Success</title>
    </head>
    <body style="
        margin: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        font-size: 45px;
        font-family: Arial, sans-serif;
        color: #fff;
        background: linear-gradient(140deg, #e50914, #000);
        text-align: center;
    ">
        ✅ CI/CD SUCCESS 🚀<br>Python App Deployed Successfully!
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
