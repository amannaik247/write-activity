from gradio_client import Client

# Replace with your exact space name
client = Client("amannaik/vennify-t5")

# Run prediction
result = client.predict(
    "he dont know what going on",   # text input
    api_name="/predict"             # this must match exactly as defined in your Gradio app
)

print("Corrected:", result)

