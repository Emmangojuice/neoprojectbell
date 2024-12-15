from flask import Blueprint, jsonify, request 

app_routes = Blueprint("app_routes",__name__)

orders - []


#define app routes 

@app_routes.route("/add_order", methods=["POST"])
def add_order():
    data = request.json
    orders.append(data)
    return jsonify({"message":"Order added!","data": data}), 201

@app_routes.route("/orders", methods=["GET"])
def get_orders():
    return jsonify(orders)

