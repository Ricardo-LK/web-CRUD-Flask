from models import *
from sqlalchemy.orm import Session

# Read
def get_all_clients(session: Session):
    clients = session.query(Cliente).all()
    return clients

def get_client_by_name(session: Session, name):
    client = session.query(Cliente).filter_by(name=name).first()
    return client

def get_client_by_id(session: Session, id):
    client = session.query(Cliente).filter_by(id=id).first()
    return client


def get_all_families(session: Session):
    families = session.query(Familia).all()
    return families


def get_family_by_id(session: Session, id):
    family = session.query(Familia).filter_by(id=id).first()
    return family


def get_family_by_name(session: Session, name):
    family = session.query(Familia).filter_by(name=name).first()
    return family


def get_all_flowers(session: Session):
    flowers = session.query(Flor).all()
    return flowers

def get_flower_by_name(session: Session, name):
    flower = session.query(Flor).filter_by(name=name).first()
    return flower

def get_flower_by_id(session: Session, id):
    flower = session.query(Flor).filter_by(id=id).first()
    return flower


def get_all_purchases(session: Session):
    purchase = session.query(Compra).all()
    return purchase

def get_purchase(session: Session, id):
    purchase = session.query(Compra).filter_by(id=id).first()
    return purchase

# Create
def create_user(session: Session, name, password):
    chk_point = session.begin_nested()
    
    try:
        user = Usuario(name=name, password=password)
        session.add(user)
        session.commit()
    except Exception as e:
        chk_point.rollback()
        return {"error": str(e)}, 400


def create_client(session: Session, name, email):
    chk_point = session.begin_nested()
    
    try:
        client = Cliente(name=name, email=email)
        session.add(client)
        session.commit()
    except Exception as e:
        chk_point.rollback()
        return {"error": str(e)}, 400

def create_family(session: Session, name):
    chk_point = session.begin_nested()
    try:
        family = Familia(name=name)
        session.add(family)
        session.commit()    
    except Exception as e:
        chk_point.rollback()
        return {"error": str(e)}, 400


def create_flower(session: Session, name, sci_name, family_name):
    chk_point = session.begin_nested()
    try:
        family = get_family_by_name(session, family_name)
        if not family:
            return {"error": "Family not found"}, 404
        
        flower = Flor(name=name, sci_name=sci_name, family=family)
        session.add(flower)
        session.commit()
        return {"message": "Flower added successfully"}, 201
    
    except Exception as e:
        chk_point.rollback()
        return {"error": str(e)}, 400
        

def create_purchase(session: Session, payment_method, price, client_name, flower_name):
    chk_point = session.begin_nested()
    try:
        client = get_client_by_name(session, client_name)
        flower = get_flower_by_name(session, flower_name)
        
        if not client or not flower:
            return None
        
        purchase = Compra(payment_method=payment_method, price=price, client=client, flower=flower)
        session.add(purchase)
        session.commit()
    except Exception as e:
        chk_point.rollback()
        return {"error": str(e)}, 400



# Update
def update_client(session: Session, client_id, new_name=None, new_email=None):
    chk_point = session.begin_nested()
    try:
        client = get_client_by_id(session, client_id)
        if not client:
            return "Client not found"
        
        if new_name:
            client.name = new_name
        if new_email:
            client.email = new_email

        session.commit()
    except Exception as e:
        chk_point.rollback()
        return {"error": str(e)}, 400
    

def update_family(session: Session, family_id, new_name=None):
    chk_point = session.begin_nested()
    try:
        family = get_family_by_id(session, family_id)
        if not family:
            return "Family not found"

        if new_name:
            family.name = new_name

        session.commit()
    except Exception as e:
        chk_point.rollback()
        return {"error": str(e)}, 400
    

def update_flower(session: Session, flower_id, new_name=None, new_sci_name=None, new_family_name=None):
    chk_point = session.begin_nested()
    try:
        flower = get_flower_by_id(session, flower_id)
        if not flower:
            return "Flower not found"
        
        if new_name:
            flower.name = new_name
        if new_sci_name:
            flower.sci_name = new_sci_name
        if new_family_name:
            new_family = get_family_by_name(session, new_family_name)
            if new_family:
                flower.family_id = new_family.id

        session.commit()
    except Exception as e:
        chk_point.rollback()
        return {"error": str(e)}, 400


def update_purchase(session: Session, purchase_id, new_payment_method=None, new_price=None, new_client_name=None, new_flower_name=None):
    chk_point = session.begin_nested()
    try:
        purchase = get_purchase(session, purchase_id)
        if not purchase:
            return "Purchase not found"

        if new_payment_method:
            purchase.payment_method = new_payment_method
        if new_price:
            purchase.price = new_price
        if new_client_name:
            new_client = get_client_by_name(session, new_client_name)
            if new_client:
                purchase.client = new_client.id
        if new_flower_name:
            new_flower = get_flower_by_name(session, new_flower_name)
            if new_flower:
                purchase.flower = new_flower.id

        session.commit()
    except Exception as e:
        chk_point.rollback()
        return {"error": str(e)}, 400
    

# Delete
def delete_client_by_id(session: Session, client_id):
    chk_point = session.begin_nested()

    try:
        client = get_client_by_id(session, client_id)
        session.delete(client)
        session.commit()
    except Exception as e:
        chk_point.rollback()
        return {"error": str(e)}, 400
    

def delete_client_by_name(session: Session, name):
    chk_point = session.begin_nested()
    try:
        client = get_client_by_name(session, name)
        session.delete(client)
        session.commit()
    except Exception as e:
        chk_point.rollback()
        return {"error": str(e)}, 400


def delete_family(session: Session, family_name):
    chk_point = session.begin_nested()
    try:
        family = get_family_by_name(session, family_name)
        session.delete(family)
        session.commit()
    except Exception as e:
        chk_point.rollback()
        return {"error": str(e)}, 400

def delete_flower(session: Session, name):
    chk_point = session.begin_nested()

    try:
        flower = get_flower_by_name(session, name)
        if flower:
            session.delete(flower)
            session.commit()

    except Exception as e:
        chk_point.rollback()
        return {"error": str(e)}, 400


def delete_flower_by_id(session: Session, id):
    chk_point = session.begin_nested()

    try:
        flower = get_flower_by_id(session, id)
        if not flower:
            return "Flor não encontrada"
        
        session.delete(flower)
        session.commit()
    except Exception as e:
        chk_point.rollback()
        return {"error": str(e)}, 400


def delete_purchase(session: Session, purchase_id):
    chk_point = session.begin_nested()

    try:
        purchase = get_purchase(session, purchase_id)
        if purchase:
            session.delete(purchase)
            session.commit()
    
    except Exception as e:
        chk_point.rollback()
        return {"error": str(e)}, 400