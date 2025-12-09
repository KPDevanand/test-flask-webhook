from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.post("/graph/webhook")
async def graph_webhook(request: Request):
    validation_token = request.query_params.get("validationToken")
    if validation_token:
        return PlainTextResponse(validation_token)  # 200 text/plain
    # handle normal notifications here
    return PlainTextResponse("OK")
