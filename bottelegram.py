import telebot

CHAVE_API = "coloque aqui seu codigo gerado no BotFather"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["Internet_sem_acesso"])
def Internet_sem_acesso(mensagem):
    bot.send_message(mensagem.chat.id, "Aguarde, nossa equipe já vai te atender!")


@bot.message_handler(commands=["Internet_com_acesso_lento"])
def Internet_com_acesso_lento(mensagem):
    bot.send_message(mensagem.chat.id, "Aguarde, nossa equipe já vai te atender!")


@bot.message_handler(commands=["Outros"])
def Outros(mensagem):
    bot.send_message(mensagem.chat.id, "Aguarde, nossa equipe já vai te atender!")


    @bot.message_handler(commands=["Voltar"])
    def Voltar(mensagem):
        bot.send_message(mensagem.chat.id, "clique aqui para ao menu: /Suporte")

@bot.message_handler(commands=["Suporte"])
def Suporte(mensagem):
    texto = """
    Qual o seu Ploblema? (Clique em uma opção)
    
    /Internet_sem_acesso
    
    /Internet_com_acesso_lento
    
    /Outros
    
    /Voltar"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["Financeiro"])
def Financeiro(mensagem):
    bot.send_message(mensagem.chat.id, "Aguarde, nossa equipe já vai te atender!")

@bot.message_handler(commands=["ReclameAqui"])
def ReclameAqui(mensagem):
    bot.send_message(mensagem.chat.id, "Para enviar uma reclamação, mande um e-mail para reclamação@suaempresa.com")


def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
Escolha uma opção para continuar (Clique no item):

/Suporte

/Financeiro

/ReclameAqui

Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(mensagem, texto)

bot.polling()