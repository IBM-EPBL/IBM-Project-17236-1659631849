  from flask import Flask,redirect,url_for,render_template

  app=Flask(__name__)

  @app.route("/")
  def Chatbot():
  	return render_template("Chatbot.html")

  if __name__=="__main__":
 	 app.run()
