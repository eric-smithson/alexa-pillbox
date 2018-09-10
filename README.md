# Alexa Pillbox
Summary: A skill that allows the elderly and their caretakers to ask Alexa if they’ve taken their pills today. Uses IoT pillbox to communicate with Alexa SDK.

## Service exploration:

- Lamda - code snippets that live on AWS that Alexa can trigger. Need to look into if they can read and store data in a database. I remember Alexa skills couldn’t store data directly because of privacy concerns but there may be work arounds if we use S3? It looks like we can use AWS Lamda to store data in S3.
- DynamoDB - simple NoSQL DB that we can store user information in.

## Alexa Intents:
- `TakeMedicine` - for users who want to manually tell Alexa they took their medicine
- `AskIfTookMedicine` - Will be the main intent. Queries `AskIfTookMedicine` lambda handler

## Lamda Handlers:
- `TakeMedicine` - Marks an account as having took their medicine for the day.
- `AskIfTookMedicine` - Queries S3 for the latest date a user took their medicine, if that day matches today, returns “yes”, else return “no"

## MVP Functional requirements:

- Device or user can communicate with Alexa that they have taken their meds today. either through the IoT Pillbox or being told directly “Alexa, I took my medication today”
- Alexa can recall whether or not it had been told that a user had taken their medication,

It is assumed that caretakers and patients alike will be using the same Amazon account, therefore all communication and information recalled will be associated with an Amazon account.
