from google import genai
from google.genai import types

import PIL.Image
import os
from dotenv import load_dotenv
load_dotenv()
from pydantic import BaseModel


class Panoutput(BaseModel):
    name: str
    fathers_name: str
    pan_number: str
    dob: str

GOOGLE_API_KEY = os.getenv('GEMINI_API_KEY')


image = PIL.Image.open('pan.webp')

client = genai.Client(api_key=GOOGLE_API_KEY)
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=["Extact the content of this image in an structured JSON format?", image],
    config={
        'response_mime_type': 'application/json',
        'response_schema': Panoutput,
    }
)

print(response.text)