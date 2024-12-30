from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime
import uvicorn
import logging
import json
import uuid
import base58

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - [%(name)s] %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI()

class Capabilities(BaseModel):
    receipt_analysis: bool
    data_processing: bool
    data_storage: bool

class ServiceOfferData(BaseModel):
    type: str
    timestamp: str
    provider: str
    capabilities: Capabilities

class ServiceOffer(BaseModel):
    data: ServiceOfferData
    signature: str
    pubkey: str

class AudioRequest(BaseModel):
    script: str
    id: str
    voice_id: Optional[str] = None
    type: str = "receipt_request"

def log_request_details(data: dict, signature: str, pubkey: str):
    """Log detailed information about the request for debugging"""
    logger.info("=" * 50)
    logger.info("Request Details:")
    logger.info(f"Public Key: {pubkey}")
    logger.info(f"Signature Length: {len(signature)}")
    logger.info(f"Data being verified: {json.dumps(data, indent=2)}")
    logger.info("=" * 50)

@app.post("/offers")
async def handle_offers(request: Request):
    # Log raw request
    body = await request.body()
    logger.info(f"Received raw request: {body.decode()}")
    
    try:
        # Parse the incoming request
        data = json.loads(body)
        logger.info(f"Parsed request data: {json.dumps(data, indent=2)}")
        
        # If it's a service offer
        if "data" in data and data["data"].get("type") == "service_offer":
            service_offer = ServiceOffer(**data)
            
            # Log the details for debugging
            log_request_details(
                service_offer.data.dict(),
                service_offer.signature,
                service_offer.pubkey
            )
            
            # For now, accept all signatures while we debug
            logger.info("Temporarily accepting all signatures for debugging")
            
            # Generate our audio transcription request
            audio_request = {
                "script": "hello from Anthony at FXN",
                "id": str(uuid.uuid4()),
                "type": "receipt_request"
            }
            
            logger.info(f"Sending audio request: {json.dumps(audio_request, indent=2)}")
            return audio_request
            
        # If it's an audio response
        elif "audio_url" in data:
            logger.info(f"Received audio response: {json.dumps(data, indent=2)}")
            # Store this for the results endpoint
            # For now, just log it
            return {"message": "Audio response received"}
            
        else:
            raise HTTPException(status_code=400, detail="Unknown request type")
            
    except Exception as e:
        logger.exception("Error processing request")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/results")
async def post_result(request: Request):
    """Handle incoming results from the audio service"""
    body = await request.body()
    logger.info("=" * 50)
    logger.info("Received result")
    logger.info(f"Content-Type: {request.headers.get('content-type', 'not specified')}")
    logger.info(f"Content-Length: {len(body)} bytes")
    
    try:
        # Check if it's JSON first
        try:
            data = json.loads(body)
            logger.info("Received JSON data:")
            logger.info(json.dumps(data, indent=2))
            return {"message": "JSON result received"}
        except json.JSONDecodeError:
            # If not JSON, assume it's binary audio data
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"audio_{timestamp}.mp3"  # Assuming MP3 format, adjust if needed
            
            # Save binary data
            with open(filename, 'wb') as f:
                f.write(body)
            
            logger.info(f"Saved audio file to {filename}")
            return {"message": "Audio file saved", "filename": filename}
            
    except Exception as e:
        logger.error(f"Error processing result: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/results/{offer_id}")
async def get_result(offer_id: str):
    # This would normally fetch from a database
    logger.info(f"Result requested for offer_id: {offer_id}")
    return {
        "message": "Not implemented yet"
    }

if __name__ == "__main__":
    logger.info("Starting server...")
    uvicorn.run(app, host="0.0.0.0", port=4000)
