import asyncio
import os

from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

# Initialize the BlobServiceClient with a connection string
connection_string = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Define the container and blob name
container_name = "temp-container-01"

# File path to upload file into blob container
file_path="C:/Users/afiqhusaini.rosdi/OneDrive - PLUS MALAYSIA BERHAD/Documents/Working_Projects/software-apm-template/210923 IP HD Camera And ANPR Engine IP ADDRESS DETAILS 2.xlsx"

# Upload file to blob container
def upload_file_to_blob():
    blob_client = blob_service_client.get_blob_client(container=container_name, blob="210923 IP HD Camera And ANPR Engine IP ADDRESS DETAILS 2.csv") # blob="file name u want to save as"
    with open(file_path, "rb") as csv_file:
        blob_client.upload_blob(csv_file, overwrite=True)

# Create blob container
def create_new_container():
    container_name_2 = "my-container"

    try:
        container_client = blob_service_client.create_container(container_name_2) # create a container
        print("Container created successfully.")
    except Exception as e:

        print(f"Error: {e}")

# List container and blobs
def list_containers_and_blobs():

    containers = blob_service_client.list_containers()

    print("Listing containers and blobs:")

    for container in containers:
        print(f" - Container: {container.name}")

        container_client = blob_service_client.get_container_client(container)
        blobs = container_client.list_blobs()

        for blob in blobs:
            print(f"   - Blob: {blob.name}")