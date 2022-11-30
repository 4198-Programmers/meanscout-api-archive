# Meanscout Api (python)
### Please note that this version is deprecated and will not be worked on in favour of the rust edition
<br>

## Pre-Requisites
Before running, you need to have python3 installed and install the following packages using the following command.
```
pip3 install uvicorn fastapi pydantic
```

## Running the program
To run the program, it's as simple as just running `python3 main.py`

## How to change config

On line 94, there is code for the config settings of the app. 
```python
# Line 94
if __name__ == '__main__':
    uvicorn.run("main:app",
            host="0.0.0.0",
            port=8000,
            reload=True,
    )
```

To change the host, port, or whether to reload the app if the connection fails, change the variable accordingly in the code.