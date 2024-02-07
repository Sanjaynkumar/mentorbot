# -*- coding: utf-8 -*-
"""YT_LangChain_Running_HuggingFace_Models_Locally.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AUTft4Cub7STTERECuaCBjGNSse5PJ5c
"""

"""## BlenderBot - Encoder-Decoder"""

from langchain import PromptTemplate, HuggingFaceHub, LLMChain

template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

from langchain.llms import HuggingFacePipeline
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline, AutoModelForSeq2SeqLM

#model_id = 'facebook/blenderbot-1B-distill'
model_id = 'facebook/blenderbot-400M-distill'
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSeq2SeqLM.from_pretrained(model_id)

pipe = pipeline(
    "text2text-generation",
    model=model,
    tokenizer=tokenizer,
    max_length=100
)

local_llm = HuggingFacePipeline(pipeline=pipe)

llm_chain = LLMChain(prompt=prompt,
                     llm=local_llm
                     )

#question = "Hi"

#print(llm_chain.run(question))

