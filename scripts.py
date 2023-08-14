from subprocess import call

def execute() -> None:
  call(
    ["uvicorn", "main:app", "--reload" ,"--host 0.0.0.0.", "--port", "8000"]
  )