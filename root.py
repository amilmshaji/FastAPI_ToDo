from fastapi import FastAPI, Request
import uvicorn
from database.connection import Settings
from routes import routelist
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# creates an instance of the Settings class, but it is not being used in the code.
settings=Settings()

# creates an instance of the FastAPI class which is a high-performance web framework for building APIs.
app=FastAPI()

# mounts a directory named "static" to the "/static" endpoint of the web application. This will allow the serving of static files (such as images, stylesheets, and javascript files) located in the "static" directory.
app.mount("/static",StaticFiles(directory="static",html=True),name="static")
templates=Jinja2Templates(directory="templates/")



@app.on_event("startup")
async def init_db():
    await settings.initialize_database()
    
#  creates an instance of the Jinja2Templates class, which is a template engine for Python, and sets the directory argument to "templates/".
@app.get("/")
def root(request:Request)-> dict:
    return templates.TemplateResponse("base.html",
                                      {
                                          "request":request
                                      })
    
    
app.include_router(routelist.todo_router,prefix="/todo")    
    
    
if __name__ == "__main__":
 uvicorn.run("root:app", host="0.0.0.0", port=8080,reload=True)  
