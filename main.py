from flask import Flask, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_cors import CORS
import crud
import models

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Database
db = create_engine("sqlite:///floricultura.db", pool_pre_ping=True, pool_recycle=3600, connect_args={'timeout': 30})
Session = sessionmaker(bind=db)
session = Session()

models.Base.metadata.create_all(bind=db)

# CRUD API Client endpoints
@app.route('/api/clients', methods=['GET'])
def get_all_clients():
    clients = crud.get_all_clients(session)
    return jsonify([{"id": client.id, "name": client.name, "email": client.email} for client in clients])


@app.route('/api/clients', methods=['POST'])
def create_client():
    data = request.json
    crud.create_client(session, data['name'], data['email'])
    return jsonify({"message": "Cliente registrado com sucesso"}), 201


@app.route('/api/clients/<int:id>', methods=['DELETE'])
def delete_client(id):
    crud.delete_client_by_id(session, id)
    return jsonify({"message": "Cliente deletado com sucesso"}), 200


@app.route('/api/clients/<int:id>', methods=['PUT'])
def update_client(id):
    data = request.json
    client = crud.get_client_by_id(session, id)
    if not client:
        return jsonify({"message": "Cliente não encontrado"}), 404

    crud.update_client(session, client_id=client.id, new_name=data.get('name'), new_email=data.get('email'))
    return jsonify({"message": "Cliente atualizado"}), 200


# CRUD API Family endpoints
@app.route('/api/families', methods=['GET'])
def get_family():
    families = crud.get_all_families(session)
    return jsonify([{"id": family.id, "name": family.name} for family in families])


@app.route('/api/families', methods=['POST'])
def create_family():
    data = request.json
    crud.create_family(session, data['name'])
    return jsonify({"message": "Familia registrada com sucesso"}), 201


@app.route('/api/families/<string:name>', methods=['DELETE'])
def delete_family(name):
    crud.delete_family(session, name)
    return jsonify({"message": "Familia apagada com sucesso"}), 200


@app.route('/api/families/<int:id>', methods=['PUT'])
def update_family(id):
    data = request.json
    family = crud.get_family_by_id(session, id)
    if not family:
        return jsonify({"message": "Família não foi registrada"}), 404

    crud.update_family(session, family_id=id, new_name=data.get('familyName'))
    return jsonify({"message": "Família atualizada com sucesso"}), 200


# CRUD API Flowers endpoints
@app.route('/api/flowers', methods=['GET'])
def get_all_flowers():
    flowers = crud.get_all_flowers(session)
    return jsonify(
        [{
            "id": flower.id,
            "name": flower.name,
            "sci_name": flower.sci_name,
            "family": flower.family.name if flower.family in crud.get_all_families(session) else None  # Verifica se há uma família associada
        } for flower in flowers]
    )
    
@app.route('/api/flowers', methods=['POST'])
def create_flower():
    data = request.json
    family = crud.get_family(session, data.get('family'))

    if not family:
        return jsonify({"message": "Family not found"}), 404  # Retorna erro se a família não existir
    
    crud.create_flower(session, data['name'], data['sci_name'], family.name)
    return jsonify({"message": "Flower added successfully"}), 201



@app.route('/api/flowers/<int:id>', methods=['DELETE'])
def delete_flower(id):
    crud.delete_flower_by_id(session, id)
    return jsonify({"message": "Flor deletada com sucesso"}), 200


@app.route('/api/flowers/<int:id>', methods=['PUT'])
def update_flower(id):
    data = request.json
    flower = crud.get_flower_by_id(session, id)
    if not flower:
        return jsonify({"message": "Flor não encontrada"}), 404

    crud.update_flower(session, flower_id=flower.id, new_name=data.get('name'), new_sci_name=data.get('sciName'), new_family_name=data.get('familyName'))
    return jsonify({"message": "Flor atualizada"}), 200


# CRUD API purchase endpoints
@app.route('/api/purchases', methods=['GET'])
def get_all_purchases():
    purchases = crud.get_all_purchases(session)
    return jsonify(
        [{
            "client": purchase.client.name,
            "flower": purchase.flower.name,
            "id": purchase.id, 
            "payment_method": purchase.payment_method, 
            "price": purchase.price, 
        } for purchase in purchases])

    
@app.route('/api/purchases', methods=['POST'])
def create_purchase():
    data = request.json
    crud.create_purchase(session, data['payment_method'], data['price'], data['client_name'], data['flower_name'])

    return jsonify({"message": "Compra registrada com sucesso"}), 201


@app.route('/api/purchases/<int:id>', methods=['DELETE'])
def delete_purchase(id):
    crud.delete_purchase(session, id)
    return jsonify({"message": "Compra deletada com sucesso"}), 200


@app.route('/api/purchases/<int:id>', methods=['PUT'])
def update_purchase(id):
    data = request.json
    purchase = crud.get_purchase(session, id)
    if not purchase:
        return jsonify({"message": "Compra não encontrada"}), 404

    crud.update_purchase(
        session, 
        purchase_id=id, 
        new_payment_method=data.get('payment_method'), 
        new_price=data.get('price'), 
        new_client_name=data.get('client_name'), 
        new_flower_name=data.get('flower_name')
    )
    return jsonify({"message": "Compra atualizada"}), 200



if __name__ == '__main__':
    app.run(debug=True)
