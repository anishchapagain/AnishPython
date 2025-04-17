# Pydantic Course Project with UV

This project template demonstrates how to use Pydantic for data validation in Python applications. It's set up using `uv`, a fast Python package installer and resolver.

## Project Structure

```
pydantic-course/
├── .gitignore
├── README.md
├── pyproject.toml
├── requirements.txt
├── setup.py
├── src/
│   └── pydantic_examples/
│       ├── __init__.py
│       ├── 01_basics.py
│       ├── 02_field_types.py
│       ├── 03_validation.py
│       ├── 04_complex_models.py
│       ├── 05_json_handling.py
│       ├── 06_custom_validation.py
│       └── 07_api_project/
│           ├── __init__.py
│           ├── main.py
│           ├── models.py
│           └── routes.py
└── tests/
    ├── __init__.py
    ├── test_basics.py
    └── test_validation.py
```

## Setup Instructions

1. First, install `uv` if you haven't already:

```bash
pip install uv
```

2. Create a new project directory:

```bash
mkdir pydantic-course
cd pydantic-course
```

3. Set up a virtual environment with `uv`:

```bash
uv venv
```

4. Activate the virtual environment:

```bash
# On Windows
.venv\Scripts\activate

# On macOS/Linux
source .venv/bin/activate
```

5. Install the required packages using `uv`:

```bash
uv pip install pydantic fastapi uvicorn email-validator pytest
```

6. Create the project files as described below

## File Contents

### `pyproject.toml`

```toml
[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "pydantic-examples"
version = "0.1.0"
description = "Examples for learning Pydantic"
readme = "README.md"
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
requires-python = ">=3.8"
dependencies = [
    "pydantic>=2.0.0",
    "email-validator>=2.0.0",
    "fastapi>=0.95.0",
    "uvicorn>=0.22.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "black>=23.0.0",
    "isort>=5.12.0",
]

[tool.pytest]
testpaths = ["tests"]

[tool.black]
line-length = 88
target-version = ["py38"]

[tool.isort]
profile = "black"
line_length = 88
```

### `requirements.txt`

```
pydantic>=2.0.0
email-validator>=2.0.0
fastapi>=0.95.0
uvicorn>=0.22.0
pytest>=7.0.0
```

### `README.md`

```markdown
# Pydantic Course Examples

This repository contains examples for learning Pydantic, organized as modules that demonstrate different features of the library.

## Installation

1. Make sure you have Python 3.8+ installed
2. Install dependencies using UV:

```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -r requirements.txt
```

## Running the Examples

Each module in the `src/pydantic_examples` directory can be run individually:

```bash
python -m pydantic_examples.01_basics
```

## Running the API Example

The API example can be run using Uvicorn:

```bash
uvicorn pydantic_examples.07_api_project.main:app --reload
```

Then visit http://localhost:8000/docs to see the API documentation.

## Running Tests

```bash
pytest
```
```

### `.gitignore`

```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/
.python-version
.pytest_cache/

# Distribution / packaging
dist/
build/
*.egg-info/

# IDE
.idea/
.vscode/
*.swp
*.swo

# Logs
*.log
```

### Source Files

Here are the example Python files:

#### `src/pydantic_examples/__init__.py`

```python
"""Pydantic examples package."""

__version__ = "0.1.0"
```

#### `src/pydantic_examples/01_basics.py`

```python
"""Basic usage of Pydantic models."""

from pydantic import BaseModel, ValidationError


class User(BaseModel):
    name: str
    age: int
    email: str


def main():
    """Demonstrate basic Pydantic model usage."""
    print("\n=== Basic Pydantic Models ===\n")

    try:
        # Create a user with valid data
        valid_user = User(name="John Doe", age=30, email="john@example.com")
        print(f"Valid user created: {valid_user}")
        print(f"Access fields directly: {valid_user.name}, {valid_user.age}")
        
        # Convert to dict
        user_dict = valid_user.model_dump()  # In Pydantic v2, .dict() is replaced with .model_dump()
        print(f"As dictionary: {user_dict}")
        
        # Try with invalid data
        print("\nTrying with invalid data...")
        invalid_user = User(name="Jane Doe", age="thirty", email="jane@example.com")
        print("This line won't execute due to the validation error")
    except ValidationError as e:
        print(f"Validation error occurred:")
        print(e)


if __name__ == "__main__":
    main()
```

#### `src/pydantic_examples/02_field_types.py`

```python
"""Different field types in Pydantic models."""

from datetime import datetime
from typing import Dict, List, Optional, Union

from pydantic import BaseModel, Field


class Product(BaseModel):
    id: int
    name: str
    price: float = Field(gt=0)  # Enforce price > 0
    tags: List[str] = []  # Default value as empty list
    in_stock: bool = True
    created_at: datetime
    metadata: Dict[str, str] = {}
    description: Optional[str] = None  # Optional field
    size: Union[int, str]  # Field that can be either int or str


class Item(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)  # ... means required
    price: float = Field(gt=0, description="Price must be greater than zero")
    quantity: int = Field(default=1, ge=0, le=100)  # Between 0 and 100


def main():
    """Demonstrate different field types."""
    print("\n=== Pydantic Field Types ===\n")

    # Create a product
    try:
        product = Product(
            id=1,
            name="Laptop",
            price=999.99,
            tags=["electronics", "computer"],
            created_at="2023-01-15T14:30:00",  # Pydantic automatically parses this to datetime
            size="large",
        )

        print(f"Product created: {product}")
        print(f"Product ID: {product.id}")
        print(f"Product name: {product.name}")
        print(f"Product price: ${product.price}")
        print(f"Product tags: {', '.join(product.tags)}")
        print(f"Product created at: {product.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Product size: {product.size}")
        print(f"Product in stock: {'Yes' if product.in_stock else 'No'}")
        
        print("\nTrying with field constraints...")
        item = Item(name="Monitor", price=299.99)
        print(f"Valid item: {item}")
        
        # This will raise a validation error
        short_name_item = Item(name="X", price=-10, quantity=200)
        print("This line won't execute due to the validation error")
    
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

#### `src/pydantic_examples/03_validation.py`

```python
"""Custom validation in Pydantic models."""

from typing import List

from pydantic import BaseModel, ValidationError, validator


class User(BaseModel):
    username: str
    password: str
    interests: List[str] = []
    
    # Validators are methods decorated with @validator
    @validator("username")
    def username_alphanumeric(cls, v):
        assert v.isalnum(), "Username must contain only alphanumeric characters"
        return v
    
    @validator("password")
    def password_min_length(cls, v):
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters long")
        return v
    
    @validator("interests")
    def interests_count(cls, v):
        if len(v) > 5:
            raise ValueError("You can specify at most 5 interests")
        return v


def main():
    """Demonstrate custom validation."""
    print("\n=== Custom Validation ===\n")

    try:
        # Try with valid data
        user1 = User(
            username="johndoe",
            password="securepass123",
            interests=["coding", "reading"]
        )
        print(f"Valid user created: {user1}")
        
        print("\nTrying with invalid data...")
        
        # Try with invalid data - will raise ValidationError
        user2 = User(
            username="john.doe",  # Contains a period
            password="short",     # Too short
            interests=["coding", "reading", "sports", "cooking", "music", "gaming"]  # Too many
        )
        print("This line won't execute due to the validation error")
        
    except ValidationError as e:
        print("Validation errors:")
        print(e.json())


if __name__ == "__main__":
    main()
```

#### `src/pydantic_examples/04_complex_models.py`

```python
"""Complex nested models in Pydantic."""

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class Address(BaseModel):
    street: str
    city: str
    zip_code: str
    country: str


class OrderItem(BaseModel):
    product_id: int
    quantity: int
    unit_price: float
    
    @property
    def total_price(self) -> float:
        return self.quantity * self.unit_price


class Order(BaseModel):
    id: int
    customer_name: str
    customer_email: str
    shipping_address: Address
    billing_address: Optional[Address] = None
    items: List[OrderItem]
    order_date: datetime
    shipped: bool = False
    
    @property
    def total_amount(self) -> float:
        return sum(item.total_price for item in self.items)
    
    @property
    def item_count(self) -> int:
        return len(self.items)


def main():
    """Demonstrate complex nested models."""
    print("\n=== Complex Nested Models ===\n")

    # Create a complex order
    order = Order(
        id=12345,
        customer_name="Alice Smith",
        customer_email="alice@example.com",
        shipping_address=Address(
            street="123 Main St",
            city="Boston",
            zip_code="02101",
            country="USA"
        ),
        # billing_address is optional, using shipping address as default
        items=[
            OrderItem(product_id=101, quantity=2, unit_price=29.99),
            OrderItem(product_id=205, quantity=1, unit_price=99.00)
        ],
        order_date="2023-05-20T10:30:00"
    )

    print(f"Order #{order.id}")
    print(f"Customer: {order.customer_name}")
    print(f"Shipping to: {order.shipping_address.city}, {order.shipping_address.country}")
    print(f"Number of items: {order.item_count}")
    print(f"Total amount: ${order.total_amount:.2f}")
    print("\nOrder items:")
    
    for i, item in enumerate(order.items, 1):
        print(f"  {i}. Product ID: {item.product_id}")
        print(f"     Quantity: {item.quantity}")
        print(f"     Unit price: ${item.unit_price:.2f}")
        print(f"     Total price: ${item.total_price:.2f}")


if __name__ == "__main__":
    main()
```

#### `src/pydantic_examples/05_json_handling.py`

```python
"""Working with JSON in Pydantic."""

import json
from typing import List, Optional

from pydantic import BaseModel


class Article(BaseModel):
    title: str
    content: str
    author: str
    tags: List[str] = []
    published: bool = False


def main():
    """Demonstrate JSON handling."""
    print("\n=== JSON Handling ===\n")

    # From JSON string to Pydantic model
    json_data = '''
    {
        "title": "Getting Started with Pydantic",
        "content": "Pydantic is a great library for data validation...",
        "author": "John Doe",
        "tags": ["python", "validation", "tutorial"],
        "published": true
    }
    '''

    article = Article.model_validate_json(json_data)  # In Pydantic v2, parse_raw is replaced with model_validate_json
    print("From JSON string to Pydantic model:")
    print(f"  Title: {article.title}")
    print(f"  Author: {article.author}")
    print(f"  Tags: {', '.join(article.tags)}")
    print(f"  Published: {'Yes' if article.published else 'No'}")

    # From Pydantic model to JSON
    article_json = article.model_dump_json()  # In Pydantic v2, json() is replaced with model_dump_json()
    print("\nFrom Pydantic model to JSON:")
    print(f"  {article_json}")

    # From dict to Pydantic model
    article_dict = {
        "title": "Advanced Pydantic Usage",
        "content": "Learn about advanced features...",
        "author": "Jane Smith",
        "tags": ["python", "advanced"]
    }

    article2 = Article.model_validate(article_dict)  # In Pydantic v2, parse_obj is replaced with model_validate
    print("\nFrom dict to Pydantic model:")
    print(f"  {article2}")

    # From Pydantic model to dict
    article_dict_again = article2.model_dump()  # In Pydantic v2, dict() is replaced with model_dump()
    print("\nFrom Pydantic model to dict:")
    print(f"  {article_dict_again}")

    # Read multiple models from JSON
    articles_json = '''
    [
        {
            "title": "Article 1",
            "content": "Content 1",
            "author": "Author 1"
        },
        {
            "title": "Article 2",
            "content": "Content 2",
            "author": "Author 2",
            "tags": ["tag1", "tag2"]
        }
    ]
    '''

    print("\nMultiple models from JSON:")
    articles = [Article.model_validate(item) for item in json.loads(articles_json)]
    for i, article in enumerate(articles, 1):
        print(f"  Article {i}: {article.title} by {article.author}")


if __name__ == "__main__":
    main()
```

#### `src/pydantic_examples/06_custom_validation.py`

```python
"""Advanced custom validation in Pydantic."""

from datetime import date, datetime
from typing import Optional

from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    HttpUrl,
    ValidationError,
    root_validator,
    validator,
)


class User(BaseModel):
    # Using specialized types
    email: EmailStr  # Requires email-validator package
    website: Optional[HttpUrl] = None  # Validates URLs
    
    # Using regex pattern
    username: str = Field(..., pattern=r"^[a-zA-Z0-9_]+$")
    
    # Date fields
    birth_date: date
    registration_date: datetime = Field(default_factory=datetime.now)
    
    # Field with constraints
    score: int = Field(0, ge=0, le=100)
    
    # Pre-validation transformation
    @validator("username")
    def username_to_lowercase(cls, v):
        return v.lower()
    
    # Validate dependent fields
    age: Optional[int] = None
    is_adult: bool = False
    
    @root_validator
    def check_age_adult_consistency(cls, values):
        age = values.get("age")
        is_adult = values.get("is_adult")
        
        if age is not None:
            if age >= 18 and not is_adult:
                values["is_adult"] = True
            elif age < 18 and is_adult:
                values["is_adult"] = False
                
        return values
    
    # Custom validation logic
    password: str
    password_confirm: Optional[str] = None
    
    @root_validator
    def check_passwords_match(cls, values):
        password = values.get("password")
        password_confirm = values.get("password_confirm")
        
        if password_confirm is not None and password != password_confirm:
            raise ValueError("Passwords do not match")
            
        return values


def main():
    """Demonstrate advanced validation techniques."""
    print("\n=== Advanced Custom Validation ===\n")

    try:
        # Create a user with custom validation
        user = User(
            email="john@example.com",
            website="https://john.dev",
            username="JohnDoe",
            birth_date="1990-01-15",
            age=32,
            password="password123",
            password_confirm="password123",
            score=95
        )
        
        print("Valid user created:")
        print(f"  Email: {user.email}")
        print(f"  Website: {user.website}")
        print(f"  Username (lowercase): {user.username}")
        print(f"  Birth date: {user.birth_date}")
        print(f"  Age: {user.age}")
        print(f"  Score: {user.score}")
        print(f"  Is adult: {user.is_adult}")
        print(f"  Registration date: {user.registration_date}")
        
        print("\nTrying with validation errors...")
        
        # This should raise validation errors
        user2 = User(
            email="not-an-email",  # Invalid email
            website="not-a-url",   # Invalid URL
            username="John.Doe!",  # Invalid username (contains . and !)
            birth_date="1995-01-01",
            age=15,                # Under 18
            is_adult=True,         # Inconsistent with age
            password="pass123",
            password_confirm="pass456"  # Doesn't match password
        )
        print("This line won't execute due to validation errors")
        
    except ValidationError as e:
        print("Validation errors:")
        print(e.json())


if __name__ == "__main__":
    main()
```

#### `src/pydantic_examples/07_api_project/models.py`

```python
"""Pydantic models for the Todo API."""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field, validator


class TodoBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=1000)
    due_date: Optional[datetime] = None
    priority: int = Field(1, ge=1, le=5)
    
    @validator("title")
    def title_must_be_capitalized(cls, v):
        if v[0].islower():
            return v.capitalize()
        return v


class TodoCreate(TodoBase):
    """Schema for creating a new todo."""
    pass


class Todo(TodoBase):
    """Schema for a complete todo with ID and metadata."""
    id: UUID
    created_at: datetime
    completed: bool = False
    
    class Config:
        from_attributes = True  # In Pydantic v2, orm_mode is replaced with from_attributes


class UserBase(BaseModel):
    """Base user schema with common fields."""
    email: EmailStr
    name: str = Field(..., min_length=2)


class UserCreate(UserBase):
    """Schema for creating a new user."""
    password: str = Field(..., min_length=8)


class User(UserBase):
    """Schema for a complete user with ID and todos."""
    id: UUID
    todos: List[Todo] = []
    
    class Config:
        from_attributes = True  # In Pydantic v2, orm_mode is replaced with from_attributes
```

#### `src/pydantic_examples/07_api_project/routes.py`

```python
"""API routes for the Todo application."""

from datetime import datetime
from typing import List
from uuid import UUID, uuid4

from fastapi import APIRouter, HTTPException

from .models import Todo, TodoCreate, User, UserCreate

# Create a router
router = APIRouter()

# In-memory database (in a real app, you'd use a proper database)
users_db = {}
todos_db = {}


@router.post("/users/", response_model=User, status_code=201)
def create_user(user: UserCreate) -> User:
    """Create a new user."""
    user_id = uuid4()
    
    # Check if email already exists
    for existing_user in users_db.values():
        if existing_user.email == user.email:
            raise HTTPException(status_code=400, detail="Email already registered")
    
    db_user = User(
        id=user_id,
        email=user.email,
        name=user.name,
        todos=[]
    )
    users_db[user_id] = db_user
    return db_user


@router.get("/users/", response_model=List[User])
def get_users() -> List[User]:
    """Get all users."""
    return list(users_db.values())


@router.get("/users/{user_id}", response_model=User)
def get_user(user_id: UUID) -> User:
    """Get a specific user by ID."""
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    return users_db[user_id]


@router.post("/users/{user_id}/todos/", response_model=Todo, status_code=201)
def create_todo(user_id: UUID, todo: TodoCreate) -> Todo:
    """Create a new todo for a user."""
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    todo_id = uuid4()
    db_todo = Todo(
        id=todo_id,
        created_at=datetime.now(),
        **todo.model_dump()  # In Pydantic v2, dict() is replaced with model_dump()
    )
    todos_db[todo_id] = db_todo
    users_db[user_id].todos.append(db_todo)
    return db_todo


@router.get("/users/{user_id}/todos/", response_model=List[Todo])
def get_user_todos(user_id: UUID) -> List[Todo]:
    """Get all todos for a user."""
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    return users_db[user_id].todos


@router.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: UUID) -> Todo:
    """Get a specific todo by ID."""
    if todo_id not in todos_db:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    return todos_db[todo_id]


@router.put("/todos/{todo_id}/complete", response_model=Todo)
def complete_todo(todo_id: UUID) -> Todo:
    """Mark a todo as completed."""
    if todo_id not in todos_db:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    todos_db[todo_id].completed = True
    return todos_db[todo_id]


@router.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: UUID) -> None:
    """Delete a todo."""
    if todo_id not in todos_db:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    # Remove todo from any user's todo list
    for user in users_db.values():
        user.todos = [todo for todo in user.todos if todo.id != todo_id]
    
    # Delete todo from todos database
    del todos_db[todo_id]
```

#### `src/pydantic_examples/07_api_project/main.py`

```python
"""Main FastAPI application for the Todo API."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import routes

# Create a FastAPI application
app = FastAPI(
    title="Todo API with Pydantic",
    description="A simple Todo API demonstrating Pydantic models with FastAPI",
    version="0.1.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, set this to specific domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the router
app.include_router(routes.router)


@app.get("/")
def read_root():
    """Root endpoint."""
    return {
        "message": "Welcome to the Todo API",
        "docs": "/docs",
        "endpoints": {
            "users": "/users/",
            "todos": "/todos/",
        },
    }


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### Test Files

#### `tests/__init__.py`

```python
"""Tests package."""
```

#### `tests/test_basics.py`

```python
"""Tests for basic Pydantic usage."""

import pytest
from pydantic import ValidationError

from pydantic_examples.01_basics import User


def test_valid_user():
    """Test creating a valid user."""
    user = User(name="Test User", age=25, email="test@example.com")
    
    assert user.name == "Test User"
    assert user.age == 25
    assert user.email == "test@example.com"


def test_invalid_user():
    """Test that creating an invalid user raises ValidationError."""
    with pytest.raises(ValidationError):
        User(name="Test User", age="not an integer", email="test@example.com")


def test_dict_conversion():
    """Test conversion to dictionary."""
    user = User(name="Test User", age=25, email="test@example.com")
    user_dict = user.model_dump()
    
    assert isinstance(user_dict, dict)
    assert user_dict["name"] == "Test User"
    assert user_dict["age"] == 25
    assert user_dict["email"] == "test@example.com"
```

#### `tests/test_validation.py`

```python
"""Tests for custom validation."""

import pytest
from pydantic import ValidationError

from pydantic_examples.03_validation import User


def test_valid_user():
    """Test creating a valid user with custom validation."""
    user = User(
        username="johndoe",
        password="securepass123",
        interests=["coding", "reading"]
    )
    
    assert user.username == "johndoe"
    assert user.password == "securepass123"
    assert len(user.interests) == 2


def test_invalid_username():
    """Test username validation."""
    with pytest.raises(ValidationError) as exc_info:
        User(
            username="john.doe",  # Contains a period
            password="securepass123",
            interests=["coding"]
        )
    
    errors = exc_info.value.errors()
    assert any("Username must contain only alphanumeric characters" in error["msg"] 
              for error in errors)


def test_invalid_password():
    """Test password validation."""
    with pytest.raises(ValidationError) as exc_info:
        User(
            username="johndoe",
            password="short",  # Too short
            interests=["coding"]
        )
    
    errors = exc_info.value.errors()
    assert any("Password must be at least 8 characters long" in error["msg"] 
              for error in errors)


def test_too_many_interests():
    """Test interests validation."""
    with pytest.raises(ValidationError) as exc_info:
        User(
            username="johndoe",
            password="securepass123",
            interests=["1", "2", "3", "4", "5", "6"]  # Too many
        )
    
    errors = exc_info.value.errors()
    assert any("You can specify at most 5 interests" in error["msg"] 
              for error in errors)
```

## How to Use This Project

1. Follow the setup instructions at the beginning
2. Explore each module in order (01_basics.py through 07_api_project)
3. Run each file to see the examples in action:

```bash
# Activate your virtual environment
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Run examples
python -m pydantic_examples.01_basics
python -m pydantic_examples.02_field_types
# ... and so on
```

4. For the API example, run:

```bash
uvicorn pydantic_examples.07_api_project.main:app --reload
```

Then visit http://localhost:8000/docs to interact with the API.

5. Run tests:

```bash
pytest
```

## Key Learning Points

- Organized modules covering different aspects of Pydantic
- Updated to work with Pydantic v2 (the latest version)
- Proper project structure with tests
- Real-world API example
- All installed and managed with `uv` for fast dependency resolution

This project template provides a structured approach to learning Pydantic with proper best practices for Python development.
