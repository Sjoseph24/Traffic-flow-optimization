import random
from sklearn.tree import DecisionTreeClassifier
from cryptography.fernet import Fernet

# Step 1: Train the AI Model
X = [
    [8, 0, 0], [8, 1, 0], [8, 0, 1],
    [17, 0, 0], [17, 1, 1], [17, 0, 1],
    [12, 0, 0], [12, 1, 1], [20, 0, 0]
]

y = [0, 1, 1, 1, 1, 1, 0, 1, 0]

model = DecisionTreeClassifier()
model.fit(X, y)

# Step 2: IoT Data Simulation
def simulate_iot_data():
    vehicle_count = random.randint(10, 100)
    speed = round(random.uniform(20.0, 80.0), 2)
    signal = random.choice(["Red", "Green", "Yellow"])
    return f"Vehicle Count: {vehicle_count}, Avg Speed: {speed} km/h, Signal: {signal}"

# Step 3: Data Encryption
key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_data(data):
    return cipher.encrypt(data.encode())

def decrypt_data(data):
    return cipher.decrypt(data).decode()

# Step 4: Chatbot Interface
def chatbot():
    print("Traffic Bot: Hello! I can predict traffic conditions.")

    while True:
        try:
            hour = int(input("Enter hour (0-23): "))
            weather = int(input("Is it raining? (1=yes, 0=no): "))
            event = int(input("Is there a nearby event? (1=yes, 0=no): "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue

        features = [[hour, weather, event]]
        prediction = model.predict(features)[0]
        traffic_status = "Heavy Traffic" if prediction == 1 else "Light Traffic"

        print(f"Traffic Prediction: {traffic_status}")

        # Show IoT data (encrypted)
        iot_data = simulate_iot_data()
        encrypted = encrypt_data(iot_data)
        print("\nEncrypted IoT Data:", encrypted)
        print("Decrypted IoT Data:", decrypt_data(encrypted))

        cont = input("\nDo you want another prediction? (y/n): ").lower()
        if cont != 'y':
            break

# Run the chatbot
if __name__ == "__main__":
    chatbot()
