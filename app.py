from flask import Flask, render_template, request, redirect, Response, Request, url_for
import random as rn
import sendMail as sm


app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/uploads/"



def random():
    numb = range(9)
    otp = rn.sample(numb, 6)
    listToStr = ' '.join([str(elem) for elem in otp])
    return listToStr


@app.route("/", methods=['POST', 'GET'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        sm.SendMail(random(), username) #username = otp gönderilecek mail adress
        return render_template('otpVerification.html')


@app.route("/OTP", methods=['POST', 'GET'])
def otpVer():
    if request.method == "GET":
        return render_template('otpVerification.html')
    if request.method == "POST":
        OTP = sm.otpRead()
        userEntry = []
        for i in range(1, 7):
            i = request.form.get('digit-' + str(i))
            userEntry.append(i)
        listToStr = ' '.join([str(elem) for elem in userEntry])

        if str(OTP) == str(listToStr):
            return "Doğrulama Başarılı"
        else:
            return "Kodu Yanlış Girdiniz."


if __name__ == "__main__":
    app.secret_key = 'admin123'
    app.run(host='0.0.0.0', port=80, debug=True)
