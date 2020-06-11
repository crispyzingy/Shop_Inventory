from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# our inventory items
inventory = [
    {"item_id": "1", "item_name": "chips", "item_price": 50, "item_quantity": 100},
    {"item_id": "2", "item_name": "biscuits", "item_price": 75, "item_quantity": 200},
    {"item_id": "3", "item_name": "candies", "item_price": 10, "item_quantity": 300},
]

# get all items
@app.route("/products/all", methods=["GET"])
def getAllProducts():
    return jsonify(inventory)


# get an item
@app.route("/products/<product_id>", methods=["GET"])
def getProduct(product_id):
    product_list = [
        product for product in inventory if (product["item_id"] == product_id)
    ]
    return jsonify(product_list)


# update an item
@app.route("/products/<product_id>", methods=["PUT"])
def updateProduct(product_id):
    product_list = [
        product for product in inventory if (product["item_id"] == product_id)
    ]
    if "item_name" in request.json:
        product_list[0]["item_name"] = request.json["item_name"]
    if "item_price" in request.json:
        product_list[0]["item_price"] = request.json["item_price"]
    if "item_quantity" in request.json:
        product_list[0]["item_quantity"] = request.json["item_quantity"]
    return jsonify(product_list[0])


# create a new item
@app.route("/products/all", methods=["POST"])
def createProduct():
    new_item = {
        "item_id": request.json["item_id"],
        "item_name": request.json["item_name"],
        "item_price": request.json["item_price"],
        "item_quantity": request.json["item_quantity"],
    }
    inventory.append(new_item)
    return jsonify(new_item)


# delete item
@app.route("/products/<product_id>", methods=["DELETE"])
def deleteProduct(product_id):
    product_list = [
        product for product in inventory if (product["item_id"] == product_id)
    ]
    if len(product_list) == 0:
        abort(404)

    inventory.remove(product_list[0])
    return jsonify("Success! Item deleted.")


# runs our app
if __name__ == "__main__":
    app.run(debug=True)
