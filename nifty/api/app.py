from fastapi import FastAPI, Header


from conf import settings
from contrib.auth import is_auth
from core.generators import generate_response
from schemas import MessageRequest

app = FastAPI()


@app.post("/api/messages")
@is_auth
def process_message(request: MessageRequest, x_api_key_token: str = Header(default=None)):
    """ Endpoint to get an answer from the artificial intelligence model. """
    response_message = generate_response(request.message, settings.EMBEDDINGS_REDIS)
    return {'message': response_message}
