# Message Broker
This is one of the features of my Software Architecture Project

## Feature specification
As a user, I would like to receive an SMS text message every time my credit card is accepted, to have real-time notification of the transactions made. This should occur 99.9% of the time, as it is important to have a reliable and accurate system that keeps me informed about the use of my credit card.
Acceptance Criteria:

When a credit card transaction is approved, the system must automatically send an SMS text message to the phone number associated with the card.
The text message must contain relevant information about the transaction, such as the date, time, amount, and location of the purchase.
The system must have a 99.9% success rate in sending text messages so that almost all approved transactions generate a notification.
The SMS notification service must be reliable and have a fast response time so that the user receives the information in real-time.

> Implemented using Django and Twilio API
