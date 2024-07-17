from sentiment_analysis.pipeline.train_pipeline import TrainPipeline
from fastapi import FastAPI
import uvicorn
import sys
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from sentiment_analysis.exception import CustomException
from sentiment_analysis.constants import *


text:str = "What is machine learing?"

app = FastAPI()

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")




@app.get("/train")
async def training():
    try:
        train_pipeline = TrainPipeline()

        train_pipeline.run_pipeline()

        return Response("Training successful !!")

    except Exception as e:
        return Response(f"Error Occurred! {e}")
    




if __name__=="__main__":
    uvicorn.run(app, host=APP_HOST, port=APP_PORT)


    