class Message:
    public_key = ''
    message = ''
    signature = ''

    def send_message(self, public_key, message, signature):
        self.public_key = public_key
        self.message = message
        self.signature = signature
        print('Message sent successfully....')

    def get_public_key(self):
        return self.public_key

    def get_message(self):
        return self.message

    def get_signature(self):
        return self.signature
