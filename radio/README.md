# FOMO Radio

This agent provides text-to-speech capabilities for the FXN network. It accepts text input and returns synthesized audio files.

## Overview

The Voice Synthesis Agent accepts text scripts and converts them to audio files. Features include:
- Text to speech conversion
- Optional voice selection
- Unique ID tracking for each request
- Binary audio file delivery

## Endpoints

### 1. Service Registration

When your agent comes online, it should send a service registration to the `/offers` endpoint.

```json
POST /offers
{
  "data": {
    "type": "service_offer",
    "timestamp": "2024-12-30T00:58:30.396505",
    "provider": "YOUR_PUBKEY",
    "capabilities": {
      "receipt_analysis": true,
      "data_processing": true,
      "data_storage": true
    }
  },
  "signature": "SOLANA_SIGNATURE",
  "pubkey": "YOUR_PUBKEY"
}
```

### 2. Voice Synthesis Request

Your service will receive requests in this format:

```json
{
  "script": "Text to be converted to speech",
  "id": "unique_request_id",
  "voice_id": "optional_voice_selection",
  "type": "receipt_request"
}
```

### 3. Results Endpoint

The service should send audio files to the `/results` endpoint:

```
POST /results
Content-Type: audio/mpeg
Binary audio data
```

The GET endpoint is also available for status checks:
```
GET /results/{offer_id}
```

## Authentication

This agent uses Solana/Anchor for request signing:

1. **Signing Library**: Uses Anchor for transaction signing
2. **Verification**: Ed25519 signature verification using PyNaCl
3. **Public Key**: Expected in base58 format

## Implementation

### Prerequisites
- Python 3.9+
- pip

### Installation

1. Clone this repository
2. Install dependencies:
```bash
cd voice-agent
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

### Requirements.txt
```
fastapi==0.109.0
uvicorn==0.27.0
pydantic==2.5.3
python-multipart==0.0.6
PyNaCl==1.5.0
base58==2.1.1
```

### Running the Server
```bash
python server.py
```

The server will start on port 4000.

### Amazon Linux 2023 Setup
```bash
# Update system
sudo dnf update -y

# Install Python and dependencies
sudo dnf install python3 python3-pip python3-devel -y

# Install virtualenv
python3 -m pip install --user virtualenv

# Setup project
mkdir voice-agent
cd voice-agent
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Error Handling

The server provides error responses in the following format:
```json
{
  "detail": "Error message"
}
```

Common status codes:
- 200: Success
- 400: Bad Request (invalid signature or format)
- 422: Validation Error (missing required fields)
- 500: Server Error

## Example Usage

Service registration example:
```python
import requests
import json

offer = {
    "data": {
        "type": "service_offer",
        "timestamp": "2024-12-30T00:58:30.396505",
        "provider": "EaXLGkTemjH4ufTTzMBJpFk6akEYmBszfx72CYgjiMtx",
        "capabilities": {
            "receipt_analysis": True,
            "data_processing": True,
            "data_storage": True
        }
    },
    "signature": "YOUR_SIGNATURE",
    "pubkey": "YOUR_PUBKEY"
}

response = requests.post("http://localhost:4000/offers", json=offer)
print(response.json())
```
