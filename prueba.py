import email
from imapclient import IMAPClient

def leer_bandeja():
    HOST = 'mail.dbjsystem.com'  # Ajusta esto para tu servidor IMAP
    USERNAME = 'prueba@dbjsystem.com'
    PASSWORD = '@admin.com'

    with IMAPClient(HOST) as client:
        client.login(USERNAME, PASSWORD)
        client.select_folder('INBOX', readonly=False)

        # Buscar correos no leídos
        messages = client.search(['UNSEEN'])
        print('previo a iterar')
        for msg_id, data in client.fetch(messages, ['ENVELOPE', 'RFC822']).items():
            envelope = data[b'ENVELOPE']
            print('De:', envelope.from_)
            print('Asunto:', envelope.subject.decode())

            # Obtener el cuerpo del mensaje
            email_message = email.message_from_bytes(data[b'RFC822'])
            for part in email_message.walk():
                if part.get_content_type() == 'text/plain':
                    body = part.get_payload(decode=True).decode()
                    print('Cuerpo:', body)
            print('leido')
            client.add_flags(msg_id, [b'\\Seen'])
