from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class Input(BaseModel):
    s1 : str 
    s2 : str 
    s3 : str 
    s4 : str