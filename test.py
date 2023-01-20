from fastapi import APIRouter, FastAPI, Header, Request, Response
import http
 
 app = FastAPI()

 @app.post("/webhook",status_code=http.HTTPStatus.ACCEPTED)
 async def webhook(request:Request):
    return
