import google.generativeai as genai


class Modelo_historia():
    def __init__(self, chave):
        self.gemini = genai.configure(api_key=chave)
        self.model = genai.GenerativeModel("gemini-1.5-flash-8b")
        self.chat = None   
        
    def comecar_historia(self, prompt):
        self.chat = self.model.start_chat(history=[])
        response = self.chat.send_message(prompt)
        return response.text
    
    def set_mensagem(self, mensagem):
        response = self.chat.send_message(mensagem)
        return response.text