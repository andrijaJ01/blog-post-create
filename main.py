from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import  RedirectResponse

app=FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8000",
    "http://192.168.1.7:8001",
    "http://192.168.1.7:8001"
]



app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post('/post/new')
async def addpost(title: str = Form(...), subtitle: str = Form(...), summary: str = Form(...), author: str = Form(...), date: str = Form(...), slug: str = Form(...), image: str = Form(...), content: str = Form(...)):
    outfile=f'/home/andrija/ssgpy/content/{slug}.md'
    template=f"---\ntitle: {title}\nsubtitle: {subtitle}\nsummary: {summary}\nslug: {slug}\nimg: {image}\nauthor: {author}\ndate: {date}\n---\n{content}"
    with open(outfile,'w') as f:
        f.write(template)
    return RedirectResponse(url='http://192.168.1.4:8000/')
