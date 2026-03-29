from fastapi import FastAPI
from skills.collect_admin_mfa import collect_admin_mfa_evidence

app = FastAPI(
    title="Skill Runtime",
    description="Python skill runtime for governed AI agents",
    version="1.0.0",
)

# Optional: root endpoint (useful for humans and health checks)
@app.get("/")
def root():
    return {"status": "skill runtime online"}

# Core skill endpoint
@app.post("/skills/collect_admin_mfa_evidence")
def run_collect_admin_mfa():
    return collect_admin_mfa_evidence()
