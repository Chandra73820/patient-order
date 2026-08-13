from flask import Flask, jsonify, request

app = Flask(__name__)

orders = [
    {
        "order_id": "PO-1001",
        "patient_id": "P-001",
        "medicine": "Paracetamol",
        "quantity": 10,
        "status": "Pending"
    }
]


@app.route("/")
def home():
    return jsonify({
        "application": "Patient Order",
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/orders", methods=["GET"])
def get_orders():
    return jsonify(orders)


@app.route("/orders", methods=["POST"])
def create_order():
    data = request.json

    order = {
        "order_id": f"PO-{1000 + len(orders) + 1}",
        "patient_id": data.get("patient_id"),
        "medicine": data.get("medicine"),
        "quantity": data.get("quantity"),
        "status": "Pending"
    }

    orders.append(order)

    return jsonify(order), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
