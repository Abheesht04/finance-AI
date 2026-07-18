from fastapi import FastAPI
from fastapi import UploadFile
from fastapi import File

from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse

from pydantic import BaseModel

import os
import shutil

from ui.finance_application import FinanceApplication


# ==========================================================
# Application
# ==========================================================

app = FastAPI(title="Finance AI")

application = FinanceApplication()


# ==========================================================
# Upload Directory
# ==========================================================

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ==========================================================
# CORS
# ==========================================================

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)


# ==========================================================
# Static Website
# ==========================================================



# ==========================================================
# Request Models
# ==========================================================

class ChatRequest(BaseModel):

    question: str


# ==========================================================
# Health
# ==========================================================

@app.get("/health")
def health():

    return JSONResponse(

        {

            "status": "ok",

            "backend": "running",

            "ai": "ready"

        }

    )


# ==========================================================
# Upload PDF
# ==========================================================

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    print("UPLOAD ENDPOINT HIT")

    try:

        file_path = os.path.join(

            UPLOAD_FOLDER,

            file.filename

        )

        with open(file_path, "wb") as buffer:

            shutil.copyfileobj(

                file.file,

                buffer

            )

        application.load_pdf(file_path)

        return JSONResponse(

            {

                "success": True,

                "filename": file.filename

            }

        )

    except Exception as e:

        return JSONResponse(

            {

                "success": False,

                "error": str(e)

            },

            status_code=500

        )


# ==========================================================
# Chat
# ==========================================================

@app.post("/chat")
def chat(request: ChatRequest):

    try:

        answer = application.ask(

            request.question

        )

        return JSONResponse(

            {

                "success": True,

                "answer": answer

            }

        )

    except Exception as e:

        return JSONResponse(

            {

                "success": False,

                "error": str(e)

            },

            status_code=500

        )



app.mount(

    "/",

    StaticFiles(

        directory="ui",

        html=True

    ),

    name="ui"

)
