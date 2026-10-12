from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "testing for future aic api oh and the INSPECTOR DOESNT PLAY GOLF HA"}
