from googleapiclient.discovery import build

def send_email(password):
    # Inserisci la tua chiave API di Google
    api_key = 'AIzaSyCEtbCqlDWkN-1Ar8FMi-IgzEBaxsjo0SE'

    # Crea il servizio Gmail utilizzando la chiave API
    service = build('gmail', 'v1', developerKey=api_key)

    # Crea il corpo dell'email
    subject = "Nuova password generata"
    body = f"La tua nuova password è: {password}"
    message = {
        'subject': subject,
        'body': {
            'text': body
        },
        'to': [
            {
                'email': 'bb.melvanni@gmail.com'
            }
        ]
    }

    # Invia l'email utilizzando l'API di Gmail
    service.users().messages().send(userId='me', body=message).execute()

# Chiamare la funzione send_email con la nuova password generata
new_password = generateRandomPassword()
send_email(new_password)