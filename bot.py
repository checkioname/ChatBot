from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer




app = Flask(__name__)

main_bot = ChatBot("ChatterBot", storage_adapter="chatterbot.storage.SQLStorageAdapter")

# trainer.train([
#     "Olá",
#     "Tudo bem e com você?",
# ])

trainer = ListTrainer(main_bot)
trainingdata=open('/home/king/Documents/chatbot/trainer/compliment.yml').read().splitlines

trainercorpus = ChatterBotCorpusTrainer(main_bot)

trainer_corpus.train(
'chatterbot.corpus.portuguese'
)





@app.route("/")
def home():
    return render_template("index.html")



@app.route("/get")
def get_bot_response():
    userText = request.args.get("msg")
    return str(main_bot.get_response(userText))





@app.route("/bot")
def hello():
    return "Hello"

if __name__ == "__main__":
    app.run()