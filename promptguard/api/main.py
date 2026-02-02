from fastapi import FastAPI
from pydantic import BaseModel

from promptguard.audit import audit_one

app = FastAPI(title="PromptGuard Audit API", version="0.1.0")


class AuditRequest(BaseModel):
    prompt: str
    output: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/audit")
def audit(req: AuditRequest):
    return audit_one(req.prompt, req.output)