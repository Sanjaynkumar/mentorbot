# -*- coding: utf-8 -*-
"""SVHS_Mentorbot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1W3Fo6lsK5VrYD26xr48YKGP-9Q2_rmb_

## Chat with your PDF files using LlamaIndex, Astra DB (Apache Cassandra), and Gradient's open-source models, including LLama2 and Streamlit, all designed for seamless interaction with PDF files.

# Installation
"""

# !pip install -q cassandra-driver
# !pip install -q cassio>=0.1.1
# !pip install -q gradientai --upgrade
# !pip install -q llama-index
# !pip install -q pypdf
# !pip install -q tiktoken==0.4.0

"""# Import OS & JSON Modules"""

import os
import json
#from google.colab import userdata

os.environ['GRADIENT_ACCESS_TOKEN'] = 'I8Vo6J3zGHqbnS6ltZlhUdlb2DzOobSH'
os.environ['GRADIENT_WORKSPACE_ID'] =  'a7fbc40f-af37-4bb7-a307-ff2bb6b68801_workspace'

"""# Import Cassandra & llama Index"""

from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster
from llama_index import ServiceContext
from llama_index import set_global_service_context
from llama_index import VectorStoreIndex, SimpleDirectoryReader, StorageContext
from llama_index.embeddings import GradientEmbedding
from llama_index.llms import GradientBaseModelLLM
from llama_index.vector_stores import CassandraVectorStore

import cassandra
print (cassandra.__version__)

"""# Connect to the VectorDB"""

# This secure connect bundle is autogenerated when you donwload your SCB,
# if yours is different update the file name below
cloud_config= {
  'secure_connect_bundle': 'secure-connect-acube-db.zip'
}

# This token json file is autogenerated when you donwload your token,
# if yours is different update the file name below
with open("sanjaykumar@acubetechnologies.in-token.json") as f:
    secrets = json.load(f)

CLIENT_ID = secrets["clientId"]
CLIENT_SECRET = secrets["secret"]


auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

row = session.execute("select release_version from system.local").one()
if row:
  print(row[0])
else:
  print("An error occurred.")

"""# Define the Gradient's Model Adapter for LLAMA-2"""

llm = GradientBaseModelLLM(
    base_model_slug="llama2-7b-chat",
    max_tokens=400,
)

"""# Configure Gradient embeddings"""

embed_model = GradientEmbedding(
    gradient_access_token = os.environ["GRADIENT_ACCESS_TOKEN"],
    gradient_workspace_id = os.environ["GRADIENT_WORKSPACE_ID"],
    gradient_model_slug="bge-large",
)

service_context = ServiceContext.from_defaults(
    llm = llm,
    embed_model = embed_model,
    chunk_size=256,
)

set_global_service_context(service_context)

"""# Load the PDFs"""

documents = SimpleDirectoryReader("Documents").load_data()
print(f"Loaded {len(documents)} document(s).")

"""# Setup and Query Index"""

index = VectorStoreIndex.from_documents(documents,
                                        service_context=service_context)
query_engine = index.as_query_engine()

# query = "How to set the share price during IPO ? "
# response = query_engine.query(query)
# print(response)

