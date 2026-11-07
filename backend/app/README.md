# app

The backend application package. `main.py` is the composition root: it builds the FastAPI application from validated settings, and it is the only place where the application is assembled.

Subfolders follow the layered structure in `docs/06_Project_Structure.md`. Dependencies point inward: outer layers such as `api` depend on inner layers, never the reverse.
