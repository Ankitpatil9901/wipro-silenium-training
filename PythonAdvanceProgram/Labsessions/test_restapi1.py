from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage (acts like database)
customers = {}
current_id = 1


@app.route("/")
def home():
    return "Welcome to Bank Customer API"


# POST → Create Customer
@app.route("/customers", methods=["POST"])
def create_customer():
    global current_id

    data = request.get_json()

    customer = {
        "id": current_id,
        "name": data["name"],
        "email": data["email"],
        "balance": data["balance"]
    }

    customers[current_id] = customer
    current_id += 1

    return jsonify(customer), 201


# GET → Retrieve Customer by ID
@app.route("/customers/<int:id>", methods=["GET"])
def get_customer(id):
    customer = customers.get(id)

    if customer:
        return jsonify(customer), 200
    else:
        return jsonify({"error": "Customer not found"}), 404


# PUT → Update Customer
@app.route("/customers/<int:id>", methods=["PUT"])
def update_customer(id):
    if id not in customers:
        return jsonify({"error": "Customer not found"}), 404

    data = request.get_json()

    customers[id]["name"] = data["name"]
    customers[id]["email"] = data["email"]
    customers[id]["balance"] = data["balance"]

    return jsonify(customers[id]), 200


# DELETE → Remove Customer
@app.route("/customers/<int:id>", methods=["DELETE"])
def delete_customer(id):
    if id not in customers:
        return jsonify({"error": "Customer not found"}), 404

    del customers[id]
    return "", 204


if __name__ == "__main__":
    app.run(debug=True)
