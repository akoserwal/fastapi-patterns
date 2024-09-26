# FastAPI Solid


```
uv venv
```

```
 source .venv/bin/activate
 ```

```
pip install "fastapi[all]" uvicorn pydantic
```

Run
```
uvicorn main:app --reload
```



Explanation of SOLID Principles


1. SRP (Single Responsibility Principle):

* The UserService handles business logic related to users.
* The InMemoryUserRepository is responsible for data persistence.
* Routes, models, and schemas have their own well-defined responsibilities.

2. OCP (Open/Closed Principle):
* The UserService can work with any implementation of IUserRepository (in-memory, database, mongodb, etc.) without changing its code.

3.LSP (Liskov Substitution Principle):
* The InMemoryUserRepository can replace any other repository implementation without changing the behavior of the application.


4. ISP (Interface Segregation Principle):
* The repository interface IUserRepository defines only necessary methods, keeping the contract minimal and focused.

5. DIP (Dependency Inversion Principle):
* The UserService depends on the IUserRepository abstraction rather than a concrete class, making the system more flexible and easier to extend.
