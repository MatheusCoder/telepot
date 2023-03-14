import json

class Chatbot():
    def __init__(self, nome):
        try:
            memoria = open(nome+".json","r")
        except FileNotFoundError:
            memoria = open(nome+".json","w")
            memoria.write('["Matheus","Waldemar"]')
            memoria.close()
            memoria = open(nome+".json","r")
        self.nome = nome
        self.conhecidos = json.load(memoria)
        memoria.close()
        self.historico = []
        self.frases = {"oi":"Olá,qual o seu nome ?", "tchau":"Adeus", "Quais editais de bolsas atuais ?":"Acesse https://www.ufrpe.br/"}
        
    def escuta(self,frase=None):
        if frase == None:
            frase = input('>: ')
        frase = str(frase)
        frase = frase.lower()
        frase = frase.replace('é', 'eh')
        return frase
    
    def pensa(self,frase):
        if frase == "oi":
            return "Olá, qual seu nome ?"
        if frase == "tchau":
            return "Adeus"
        if frase == "Quais editais de bolsas atuais ?":
            return "Acesse https://www.ufrpe.br/"
        if self.historico[-1] == "Olá, qual seu nome ?":
            nome = self.pegaNome(frase)
            frase = self.respondeNome(nome)
            return frase
        return "Não entendi"
    
    def pegaNome(self, nome):
        if "o meu nome eh " in nome:
            nome = nome[14:]
        nome = nome.title()
        return nome
    
    def respondeNome(self, nome):
        if nome in self.conhecidos:
            frase = "Opa mano "
        else:
            frase = "Muito prazer "
        return frase+nome
        
    def fala(self,frase):
        print(frase)
        self.historico.append(frase)
