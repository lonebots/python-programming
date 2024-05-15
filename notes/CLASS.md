## Python Class 

### Access Modifiers

- **Public** : Accessible from anywhere
- **Protected** : Accessible only in the class and its subclasses
- **Private** : Accessible only in the class

check the below example for conventions in python, while using access modifiers.

```python
class MyClass:

    _protected = None
    __private = None


    def __init__(self):
        self.public = "Public"
        self._protected = "Protected"
        self.__private = "Private"

```