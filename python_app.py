from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return """
    <div style="
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        font-size: 40px;
        font-family: Arial, sans-serif;
        color: #ffffff;
        background: linear-gradient(135deg, #ff0000, #000000);
        text-align: center;
    ">
        ✅ CI/CD SUCCESS! <br>🚀 Python App Deployed Successfully!
    </div>
    """

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
