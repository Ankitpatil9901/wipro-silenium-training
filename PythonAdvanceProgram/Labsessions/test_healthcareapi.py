from flask import Flask, jsonify, request
from functools import wraps

app = Flask(__name__)

# -----------------------------
# In-memory storage
# -----------------------------
doctors = {}
patients = {}
appointments = {}

doctor_id_counter = 500
patient_id_counter = 100
appointment_id_counter = 1000

VALID_TOKEN = "mysecrettoken"


# -----------------------------
# Bearer Token Authentication
# -----------------------------
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header or auth_header != f"Bearer {VALID_TOKEN}":
            return jsonify({"error": "Unauthorized"}), 401

        return f(*args, **kwargs)

    return decorated


# -----------------------------
# 1️⃣ Create Doctor
# POST /v1/doctors
# -----------------------------
@app.route("/v1/doctors", methods=["POST"])
@token_required
def create_doctor():
    global doctor_id_counter

    data = request.get_json()

    doctor = {
        "doctor_id": doctor_id_counter,
        "name": data["name"],
        "specialization": data["specialization"],
        "experience": data["experience"]
    }

    doctors[doctor_id_counter] = doctor
    doctor_id_counter += 1

    return jsonify(doctor), 201


# -----------------------------
# 2️⃣ Register Patient
# POST /v1/patients
# -----------------------------
@app.route("/v1/patients", methods=["POST"])
@token_required
def register_patient():
    global patient_id_counter

    data = request.get_json()

    # Validation: Age
    if data["age"] < 0:
        return jsonify({"error": "Invalid age"}), 400

    # Validation: Email
    if "email" not in data or not data["email"]:
        return jsonify({"error": "Email required"}), 400

    # Duplicate phone check
    for patient in patients.values():
        if patient["phone"] == data["phone"]:
            return jsonify({"error": "Duplicate phone number"}), 409

    patient = {
        "patient_id": patient_id_counter,
        "name": data["name"],
        "age": data["age"],
        "email": data["email"],
        "phone": data["phone"]
    }

    patients[patient_id_counter] = patient
    patient_id_counter += 1

    return jsonify(patient), 201


# -----------------------------
# 3️⃣ Book Appointment
# POST /v1/appointments
# -----------------------------
@app.route("/v1/appointments", methods=["POST"])
@token_required
def book_appointment():
    global appointment_id_counter

    data = request.get_json()

    # Check if doctor exists
    if data["doctor_id"] not in doctors:
        return jsonify({"error": "Doctor not found"}), 404

    # Check if patient exists
    if data["patient_id"] not in patients:
        return jsonify({"error": "Patient not found"}), 404

    # Check if time slot already booked
    for appt in appointments.values():
        if (appt["doctor_id"] == data["doctor_id"] and
                appt["date"] == data["date"] and
                appt["time"] == data["time"]):
            return jsonify({"error": "Time slot already booked"}), 409

    appointment = {
        "appointment_id": appointment_id_counter,
        "patient_id": data["patient_id"],
        "doctor_id": data["doctor_id"],
        "date": data["date"],
        "time": data["time"],
        "status": "Booked"
    }

    appointments[appointment_id_counter] = appointment
    appointment_id_counter += 1

    return jsonify(appointment), 201


# -----------------------------
# 4️⃣ View Appointment
# GET /v1/appointments/<id>
# -----------------------------
@app.route("/v1/appointments/<int:id>", methods=["GET"])
@token_required
def get_appointment(id):
    if id not in appointments:
        return jsonify({"error": "Appointment not found"}), 404

    return jsonify(appointments[id]), 200


# -----------------------------
# 5️⃣ Reschedule Appointment
# PUT /v1/appointments/<id>
# -----------------------------
@app.route("/v1/appointments/<int:id>", methods=["PUT"])
@token_required
def reschedule_appointment(id):
    if id not in appointments:
        return jsonify({"error": "Appointment not found"}), 404

    data = request.get_json()

    # Check if new slot already booked
    for appt_id, appt in appointments.items():
        if (appt_id != id and
                appt["doctor_id"] == appointments[id]["doctor_id"] and
                appt["date"] == data["date"] and
                appt["time"] == data["time"]):
            return jsonify({"error": "Time slot already booked"}), 409

    # Update only if slot available
    appointments[id]["date"] = data["date"]
    appointments[id]["time"] = data["time"]

    return jsonify(appointments[id]), 200


# -----------------------------
# 6️⃣ Cancel Appointment
# DELETE /v1/appointments/<id>
# -----------------------------
@app.route("/v1/appointments/<int:id>", methods=["DELETE"])
@token_required
def cancel_appointment(id):
    if id not in appointments:
        return jsonify({"error": "Appointment not found"}), 410

    del appointments[id]
    return "", 204


if __name__ == "__main__":
    app.run(debug=True)
