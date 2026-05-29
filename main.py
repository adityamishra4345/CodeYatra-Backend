from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class InspectRequest(BaseModel):
    content: str

class InspectResponse(BaseModel):
    verdict: str
    threat_score: int
    content_type: str
    redirect_chain: List[str]
    typosquat_match: Optional[str] = None
    tld_risk: bool
    apk_detected: bool
    findings: List[str]

class TextAnalyzeRequest(BaseModel):
    text: str

class TextAnalyzeResponse(BaseModel):
    verdict: str
    threat_score: int
    triggered_keywords: List[str]
    nlp_label: str
    nlp_confidence: float
    findings: List[str]



@app.post("/api/inspect", response_model=InspectResponse)
async def inspect_qr(request: InspectRequest):
    return InspectResponse(
        verdict="SAFE",
        threat_score=0,
        content_type="URL",
        redirect_chain=[request.content],
        typosquat_match=None,
        tld_risk=False,
        apk_detected=False,
        findings=[]
    )

@app.post("/api/analyze-text", response_model=TextAnalyzeResponse)
async def analyze_text(request: TextAnalyzeRequest):
    return TextAnalyzeResponse(
        verdict="SAFE",
        threat_score=0,
        triggered_keywords=[],
        nlp_label="safe",
        nlp_confidence=0.99,
        findings=[]
    )