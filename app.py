from fastapi import FastAPI
from skills.collect_admin_mfa import collect_admin_mfa_evidence

app = FastAPI(title="MIP Skill Runtime")

@app.post("/skills/collect_admin_mfa_evidence")
def run_collect_admin_mfa():
    return collect_admin_mfa_evidence()
