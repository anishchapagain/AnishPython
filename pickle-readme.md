# Python Pickle Examples

This repository contains examples demonstrating how to use Python's `pickle` module for data serialization and deserialization. From basic usage to advanced techniques, these examples cover a wide range of scenarios you might encounter.

## Table of Contents

- [Basic Examples](#basic-examples)
- [Intermediate Examples](#intermediate-examples)
- [Advanced Examples](#advanced-examples)
- [Hard Cases and Solutions](#hard-cases-and-solutions)
- [Best Practices](#best-practices)

## Basic Examples

### Simple Serialization and Deserialization

```python
import pickle

# Basic data types
data = {
    'integer': 42,
    'float': 3.14159,
    'string': 'Hello, Pickle!',
    'list': [1, 2, 3, 4, 5],
    'dict': {'a': 1, 'b': 2, 'c': 3},
    'boolean': True,
    'none': None
}

# Serialize to a file
with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)
    
# Deserialize from a file
with open('data.pkl', 'rb') as f:
    loaded_data = pickle.load(f)
    
print(loaded_data)
```

### Memory-based Serialization

```python
import pickle

# Serialize to bytes
data = ["apple", "banana", "cherry"]
serialized_data = pickle.dumps(data)
print(f"Serialized data: {serialized_data}")

# Deserialize from bytes
deserialized_data = pickle.loads(serialized_data)
print(f"Deserialized data: {deserialized_data}")
```

## Intermediate Examples

### Pickling Custom Objects

```python
import pickle

class Person:
    def __init__(self, name, age, skills):
        self.name = name
        self.age = age
        self.skills = skills
        
    def __str__(self):
        return f"{self.name}, {self.age} years old, skills: {', '.join(self.skills)}"

# Create an instance
alice = Person("Alice", 30, ["Python", "Machine Learning", "Data Analysis"])

# Pickle the object
with open('person.pkl', 'wb') as f:
    pickle.dump(alice, f)
    
# Unpickle the object
with open('person.pkl', 'rb') as f:
    loaded_alice = pickle.load(f)
    
print(loaded_alice)  # Calls __str__
```

### Pickling Multiple Objects

```python
import pickle

# Multiple objects
data1 = [1, 2, 3, 4, 5]
data2 = {"name": "John", "age": 30}
data3 = "Hello, Pickle!"

# Pickle multiple objects to the same file
with open('multiple.pkl', 'wb') as f:
    pickle.dump(data1, f)
    pickle.dump(data2, f)
    pickle.dump(data3, f)
    
# Unpickle multiple objects
with open('multiple.pkl', 'rb') as f:
    loaded_data1 = pickle.load(f)
    loaded_data2 = pickle.load(f)
    loaded_data3 = pickle.load(f)
    
print(loaded_data1)
print(loaded_data2)
print(loaded_data3)
```

### Using Different Protocols

```python
import pickle
import os

data = {"name": "Protocol Test", "values": list(range(1000))}

# Compare different protocols
for protocol in range(0, pickle.HIGHEST_PROTOCOL + 1):
    filename = f'data_proto{protocol}.pkl'
    with open(filename, 'wb') as f:
        pickle.dump(data, f, protocol=protocol)
    size = os.path.getsize(filename)
    print(f"Protocol {protocol}: {size} bytes")
```

## Advanced Examples

### Customizing Pickle Behavior

```python
import pickle
import io

class CustomClass:
    def __init__(self, value, secret):
        self.value = value
        self.secret = secret  # We don't want to pickle this
        
    def __getstate__(self):
        """Return state to be pickled - exclude secret"""
        state = self.__dict__.copy()
        del state['secret']
        state['extra'] = f"Pickled at version 1.0"
        return state
    
    def __setstate__(self, state):
        """Restore state from pickle"""
        self.__dict__.update(state)
        self.secret = "Default secret after unpickling"
        
obj = CustomClass("important data", "very secret value")
serialized = pickle.dumps(obj)
restored = pickle.loads(serialized)

print(f"Original object secret: {obj.secret}")
print(f"Restored object secret: {restored.secret}")
print(f"Extra info: {restored.extra}")
```

### Handling Class Definition Changes

```python
import pickle

# Version 1 of the class (imagine this was in an older version of your code)
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        
# Create and pickle a User object
user_v1 = User("john_doe", "john@example.com")
with open('user.pkl', 'wb') as f:
    pickle.dump(user_v1, f)

# Version 2 of the class (with new attribute and method)
class User:
    def __init__(self, username, email, role="user"):
        self.username = username
        self.email = email
        self.role = role  # New attribute
        
    def has_admin_rights(self):  # New method
        return self.role == "admin"

# Load the old object into the new class definition
with open('user.pkl', 'rb') as f:
    user_v2 = pickle.load(f)

# The object is missing the new 'role' attribute
print(f"Username: {user_v2.username}")
print(f"Email: {user_v2.email}")

try:
    print(f"Role: {user_v2.role}")  # This will raise an AttributeError
except AttributeError:
    print("Role attribute is missing!")

# But we can still use the new method (it will fail though)
try:
    print(f"Has admin rights: {user_v2.has_admin_rights()}")
except AttributeError:
    print("Method failed because role attribute is missing!")

# Let's add the missing attribute
user_v2.role = "user"
print(f"Now has admin rights: {user_v2.has_admin_rights()}")
```

### Handling Circular References

```python
import pickle

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        self.children.append(child)
        child.parent = self  # Creates a circular reference

# Create nodes with circular references
root = Node("Root")
child1 = Node("Child 1")
child2 = Node("Child 2")
root.add_child(child1)
root.add_child(child2)
child1.add_child(Node("Grandchild 1"))
child1.add_child(child2)  # Creates another circular reference

# Pickle and unpickle
with open('circular.pkl', 'wb') as f:
    pickle.dump(root, f)

with open('circular.pkl', 'rb') as f:
    loaded_root = pickle.load(f)

# Verify the structure was preserved
print(f"Root name: {loaded_root.name}")
print(f"First child name: {loaded_root.children[0].name}")
print(f"First child's parent name: {loaded_root.children[0].parent.name}")
print(f"Are root and first child's parent the same object? {loaded_root is loaded_root.children[0].parent}")
```

## Hard Cases and Solutions

### Problem: Pickling Unpicklable Objects

Some objects can't be pickled, such as file handles, database connections, and certain types of functions.

```python
import pickle
import tempfile

class DatabaseConnection:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connection = self._connect()  # Unpicklable resource
        self.queries = []
        
    def _connect(self):
        # Simulate connecting to a database
        print(f"Connecting to {self.connection_string}...")
        # In reality, this would return a database connection
        return tempfile.TemporaryFile()  # This can't be pickled
    
    def execute_query(self, query):
        self.queries.append(query)
        print(f"Executing: {query}")
        # Would actually execute the query using self.connection
        
    def __getstate__(self):
        """Solution: Custom state for pickling"""
        state = self.__dict__.copy()
        # Remove the unpicklable connection
        del state['connection']
        return state
    
    def __setstate__(self, state):
        """Recreate the connection when unpickling"""
        self.__dict__.update(state)
        # Recreate the connection
        self.connection = self._connect()

# Create and use a database connection
db = DatabaseConnection("mysql://localhost/mydb")
db.execute_query("SELECT * FROM users")
db.execute_query("UPDATE products SET price = 10 WHERE id = 1")

# Pickle and unpickle
with open('database.pkl', 'wb') as f:
    pickle.dump(db, f)

with open('database.pkl', 'rb') as f:
    loaded_db = pickle.load(f)

# The connection was recreated, and the queries history preserved
print(f"Query history: {loaded_db.queries}")
loaded_db.execute_query("SELECT * FROM orders")
```

### Problem: Pickle Across Different Versions of a Class

As your code evolves, class definitions change. This can break unpickling of old data.

```python
import pickle

# Solution: Version-aware class
class VersionedUser:
    _version = 2  # Current version of the class
    
    def __init__(self, username, email=None, is_active=None, role=None):
        self.username = username
        
        # v1 attributes
        self.email = email
        
        # v2 attributes
        self.is_active = is_active if is_active is not None else True
        
        # v3 attributes
        self.role = role if role is not None else "user"
    
    def __getstate__(self):
        state = self.__dict__.copy()
        state['_pickle_version'] = self._version
        return state
    
    def __setstate__(self, state):
        pickle_version = state.pop('_pickle_version', 0)
        
        # Update the state based on version differences
        if pickle_version < 2:
            print(f"Upgrading from v{pickle_version} to v2")
            state['is_active'] = True  # Default for old versions
            
        if pickle_version < 3:
            print(f"Upgrading from v{pickle_version} to v3")
            state['role'] = "user"  # Default role for old versions
        
        self.__dict__.update(state)

# Simulate an old v1 pickle (manual creation for demonstration)
old_state = {'username': 'legacy_user', 'email': 'legacy@example.com', '_pickle_version': 1}
v1_pickle = pickle.dumps(old_state)

# Update the VersionedUser class to "v3"
VersionedUser._version = 3

# Load the old data with the new class version
with open('old_user.pkl', 'wb') as f:
    f.write(v1_pickle)

with open('old_user.pkl', 'rb') as f:
    loaded_user = pickle.load(f)

# The object gets upgraded with default values
print(f"Username: {loaded_user['username']}")
print(f"Email: {loaded_user['email']}")
print(f"Is active: {loaded_user.get('is_active')}")
print(f"Role: {loaded_user.get('role')}")
```

### Problem: External Object References

Sometimes you want to pickle an object structure but exclude certain objects, like external resources.

```python
import pickle

class ApiClient:
    def __init__(self, api_key):
        self.api_key = api_key
        
class DataProcessor:
    def __init__(self, data, api_client):
        self.data = data
        self.api_client = api_client  # External dependency
        self.processed_items = []
        
    def process(self):
        # Process data using the API client
        for item in self.data:
            # Simulate processing
            processed = f"Processed {item} using API"
            self.processed_items.append(processed)
            
    def __getstate__(self):
        """Solution: Use a reference to the external object"""
        state = self.__dict__.copy()
        # Replace api_client with just the key
        state['_api_key'] = self.api_client.api_key
        del state['api_client']
        return state
    
    def __setstate__(self, state):
        """Recreate the reference when unpickling"""
        # Extract and remove the API key
        api_key = state.pop('_api_key')
        
        # Create a new API client
        self.__dict__.update(state)
        self.api_client = ApiClient(api_key)

# Setup
api_client = ApiClient("secret_api_key_12345")
processor = DataProcessor(["item1", "item2", "item3"], api_client)
processor.process()

# Pickle and unpickle
with open('processor.pkl', 'wb') as f:
    pickle.dump(processor, f)

with open('processor.pkl', 'rb') as f:
    loaded_processor = pickle.load(f)

# Check that it worked
print(f"API key preserved: {loaded_processor.api_client.api_key}")
print(f"Processed items: {loaded_processor.processed_items}")
```

### Problem: Large Data Sets

Pickling large datasets can be slow and produce large files.

```python
import pickle
import gzip
import time
import os

# Generate a large dataset
large_data = [{"id": i, "value": f"data_{i}", "numbers": list(range(100))} for i in range(10000)]

# Solution 1: Use a higher protocol for efficiency
start_time = time.time()
with open('large_data_default.pkl', 'wb') as f:
    pickle.dump(large_data, f)
default_time = time.time() - start_time
default_size = os.path.getsize('large_data_default.pkl')

start_time = time.time()
with open('large_data_highest.pkl', 'wb') as f:
    pickle.dump(large_data, f, protocol=pickle.HIGHEST_PROTOCOL)
highest_time = time.time() - start_time
highest_size = os.path.getsize('large_data_highest.pkl')

# Solution 2: Use compression
start_time = time.time()
with gzip.open('large_data.pkl.gz', 'wb') as f:
    pickle.dump(large_data, f, protocol=pickle.HIGHEST_PROTOCOL)
compressed_time = time.time() - start_time
compressed_size = os.path.getsize('large_data.pkl.gz')

print(f"Default protocol: {default_size:,} bytes in {default_time:.2f}s")
print(f"Highest protocol: {highest_size:,} bytes in {highest_time:.2f}s")
print(f"Compressed: {compressed_size:,} bytes in {compressed_time:.2f}s")
print(f"Compression ratio: {default_size / compressed_size:.2f}x")

# Loading compressed data
start_time = time.time()
with gzip.open('large_data.pkl.gz', 'rb') as f:
    loaded_data = pickle.load(f)
load_time = time.time() - start_time

print(f"Loaded {len(loaded_data)} items in {load_time:.2f}s")
```

## Best Practices

1. **Always Open Files in Binary Mode**: Always use `'wb'` for writing and `'rb'` for reading pickle files.

2. **Use the Highest Protocol for Efficiency**: For maximum performance, use `protocol=pickle.HIGHEST_PROTOCOL`.

3. **Handle Version Changes**: Design your classes to handle version changes gracefully using `__getstate__` and `__setstate__`.

4. **Be Careful with Unpicklable Objects**: Use custom pickling methods to handle unpicklable resources like file handles and network connections.

5. **Consider Security Implications**: Never unpickle data from untrusted sources - pickle can execute arbitrary code.

6. **Use Compression for Large Data**: For large datasets, use compression like `gzip` to reduce file size.

7. **Implement Safe Loading**: Use timeouts and error handling when loading pickle files to prevent hanging or crashes.

```python
def safe_load_pickle(filename, timeout=5):
    """Load a pickle file with a timeout for safety"""
    import signal
    
    def timeout_handler(signum, frame):
        raise TimeoutError(f"Loading pickle took longer than {timeout} seconds")
    
    # Set the timeout
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout)
    
    try:
        with open(filename, 'rb') as file:
            data = pickle.load(file)
        signal.alarm(0)  # Disable the alarm
        return data
    except (pickle.UnpicklingError, EOFError) as e:
        print(f"Error unpickling file: {e}")
        return None
    except TimeoutError as e:
        print(f"Timeout error: {e}")
        return None
    finally:
        signal.alarm(0)  # Ensure the alarm is canceled
```

8. **Consider Alternatives**: For certain use cases, alternatives like JSON, YAML, or protocol buffers might be more appropriate.

```python
# JSON for simple data structures and interoperability
import json
simple_data = {"name": "John", "age": 30, "skills": ["Python", "JavaScript"]}
with open('data.json', 'w') as f:
    json.dump(simple_data, f)

# YAML for human-readable configuration
import yaml
config_data = {"server": {"host": "localhost", "port": 8080}, "debug": True}
with open('config.yaml', 'w') as f:
    yaml.dump(config_data, f)
```

---

These examples demonstrate the power and flexibility of Python's pickle module, as well as techniques for handling common challenges. Remember that pickle is primarily designed for Python-specific serialization - if interoperability with other systems or languages is required, consider alternatives like JSON or Protocol Buffers.
