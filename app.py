from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/quizes/pokemon", methods=["GET","POST"])
def quiz():
  if request.method == "POST":
    score = 0
    antwoorden : list =[request.form.get("vraag_1"),
      request.form.get("vraag_2"),request.form.get("vraag_3"),
      request.form.get("vraag_4"),request.form.get("vraag_5"),
      request.form.get("vraag_6"),request.form.get("vraag_7"),
      request.form.get("vraag_8")]
    correcte_antwoorden : list = ["c","a","b","a",'151',"a","b",'3']
    print(antwoorden)
    if antwoorden[0] == correcte_antwoorden[0]:
      score += 1
    if antwoorden[1] == correcte_antwoorden[1]:
      score += 1
    if antwoorden[2] == correcte_antwoorden[2]:
      score += 1
    if antwoorden[3] == correcte_antwoorden[3]:
      score += 1
    if antwoorden[4] == correcte_antwoorden[4]:
      score += 1
    if antwoorden[5] == correcte_antwoorden[5]:
      score += 1
    if antwoorden[6] == correcte_antwoorden[6]:
      score += 1
    if antwoorden[7] == correcte_antwoorden[7]:
      score += 1
    print(score)
    return render_template("antwoord.html",score=score)
  return render_template("pokemon.html")

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")