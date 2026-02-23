import requests

BASE_URL = "http://127.0.0.1:5000/customers"

customer_id = None


def test_customer_lifecycle():
    global customer_id

    # -----------------------------
    # STEP 1: POST - Create Customer
    # -----------------------------
    payload = {
        "name": "Ankit Patil",
        "email": "ankit@test.com",
        "balance": 10000
    }

    response = requests.post(BASE_URL, json=payload)

    assert response.status_code == 201
    data = response.json()

    assert "id" in data
    assert data["name"] == payload["name"]

    customer_id = data["id"]
    print("Customer Created ID:", customer_id)

    # -----------------------------
    # STEP 2: GET - Retrieve Customer
    # -----------------------------
    response = requests.get(f"{BASE_URL}/{customer_id}")

    assert response.status_code == 200
    data = response.json()

    assert data["email"] == "ankit@test.com"
    assert data["balance"] == 10000

    # -----------------------------
    # STEP 3: PUT - Update Customer
    # -----------------------------
    updated_payload = {
        "name": "Ankit Patil",
        "email": "ankit_updated@test.com",
        "balance": 10000
    }

    response = requests.put(f"{BASE_URL}/{customer_id}", json=updated_payload)

    assert response.status_code == 200
    data = response.json()

    assert data["email"] == "ankit_updated@test.com"
    assert data["id"] == customer_id

    # -----------------------------
    # STEP 4: DELETE - Remove Customer
    # -----------------------------
    response = requests.delete(f"{BASE_URL}/{customer_id}")

    assert response.status_code == 204

    # Verify GET after delete
    response = requests.get(f"{BASE_URL}/{customer_id}")
    assert response.status_code == 404

    print("Customer lifecycle test passed successfully!")
