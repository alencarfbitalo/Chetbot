import telebot

CHAVE_API = "6762967800:AAHF_PCM8P2-hzptzrrOGRasswAciHreEGA"

bot = telebot.TeleBot(CHAVE_API)


@bot.message_handler(commands=["Internet sem Acesso"])
def semacesso(mensagem):
    bot.send_message(mensagem.chat.id, "Aguarde, nossa equipe já vai te atender!")

@bot.message_handler(commands=["Internet com acesso Lento"])
def acessolento(mensagem):
    bot.send_message(mensagem.chat.id, "Aguarde, nossa equipe já vai te atender!")

@bot.message_handler(commands=["Financeiro"])
def financeiro(mensagem):
    bot.send_message(mensagem.chat.id, "Aguarde, nossa equipe já vai te atender!")


@bot.message_handler(commands=["Atendimento ao cliente"])
def atendimentoaocliente(mensagem):
    texto = """
ESCOLHA UMA OPÇÃO PARA CONTINUAR (Clique em uma opção)

/semacesso semacesso
/acessolento acessolento
/financeiro financeiro

RESPONDER QUALQUER OUTRA COISA NÃO VAI FINCIONAR, CLIQUEM EM UMA DAS OPÇÕES"""
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["Reclamações"])
def suportetecnicodecampo(mensagem):
    bot.send_message(mensagem.chat.id, "Para enviar uma reclamação, mande um e-mail para reclamação@siaratec.com")


    bot.polling()