# Import necessary modules
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lawfirm.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a Client model
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    case = db.Column(db.String(50), nullable=False)
    nature_of_transaction = db.Column(db.String(100), nullable=False)
    case_details = db.Column(db.Text)

# Create database tables
db.create_all()

# API endpoint for adding a new client
@app.route('/add_client', methods=['POST'])
def add_client():
    data = request.json  # Get data from the request

    # Extract information from the request data
    name = data.get('name')
    case = data.get('case')
    nature_of_transaction = data.get('nature_of_transaction')
    case_details = data.get('case_details')

    # Create a new Client instance
    new_client = Client(name=name, case=case, nature_of_transaction=nature_of_transaction, case_details=case_details)

    # Add the new client to the database
    db.session.add(new_client)
    db.session.commit()

    return jsonify({'message': 'Client added successfully'})

# API endpoint for updating client information
@app.route('/update_client/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    client = Client.query.get(client_id)

    if client:
        data = request.json  # Get data from the request

        # Update client information
        client.name = data.get('name', client.name)
        client.case = data.get('case', client.case)
        client.nature_of_transaction = data.get('nature_of_transaction', client.nature_of_transaction)
        client.case_details = data.get('case_details', client.case_details)

        # Commit changes to the database
        db.session.commit()

        return jsonify({'message': 'Client updated successfully'})
    else:
        return jsonify({'message': 'Client not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
