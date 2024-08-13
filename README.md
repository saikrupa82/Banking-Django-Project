
## Bank Transfer System
This project is a simple bank transfer system developed using Django. It allows users to transfer funds between different bank accounts, with features such as selecting the sender and receiver accounts, viewing account details, and managing the transaction process.

### Key Features:
- Account Selection: Users can select the account from which they want to transfer money, as well as the destination account.
- Transfer Amount: Users can specify the amount to transfer.
- Real-Time Balance Update: The system displays the balance of the sender's account and updates it after the transfer.
- User-Friendly Interface: The interface is designed to be intuitive, allowing users to easily complete transactions.
### Project Structure:
- Front-end: The user interface is built using Django's templating engine, with a focus on clarity and ease of use.
- Back-end: The business logic for handling transactions is managed by Django views, models, and forms.


### Account List:
![image](https://github.com/user-attachments/assets/1e580849-62b0-4543-a5c8-5b309596a16d)

A table view listing all available accounts, with options to initiate a transfer for each account.

### Screenshots:
- Transfer Amount Page:
![image](https://github.com/user-attachments/assets/ed5f722e-1e87-48e3-a8b7-bb341c09b3d7)

This page allows users to select the sender's account, enter the amount to be transferred, and select the destination account.


## Setup Instructions:
### Clone the Repository:

bash```
git clone https://github.com/yourusername/bank-transfer-system.git
cd bank-transfer-system```

### Install Dependencies:

bash```
pip install -r requirements.txt```
### Run Migrations:

bash```
python manage.py migrate```
### Start the Development Server:

bash```
python manage.py runserver```
#### Access the Application:

- Open your browser and go to http://127.0.0.1:8000/ to start using the bank transfer system.
Additional Information:
- Technologies Used: Django, HTML, CSS, JavaScript.


