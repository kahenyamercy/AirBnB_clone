AirBnB Clone Command Interpreter
PROJECT DESCRIPTION
In this project, we build a command interpreter to manage AirBnB objects. This involves creating a parent class, BaseModel, responsible for the initialization, serialization, and deserialization of instances. We establish a serialization/deserialization flow: Instance <-> Dictionary <-> JSON string <-> File. Additionally, we create classes for various AirBnB entities (e.g., User, State, City, Place) that inherit from BaseModel. We also implement the first abstracted storage engine: File storage. The project includes comprehensive unit tests to validate all classes and the storage engine.


COMMAND INTERPRETER
The command interpreter allows users to:

Create: Instantiate new objects such as User, Place, etc.
Retrieve: Access objects from files, databases, etc.
Perform Operations: Conduct operations on objects (e.g., count, compute stats).
Update: Modify attributes of an object.
Destroy: Delete an object.


How to Start the Command Interpreter
1.Clone the Repository: Clone this repository to your local machine using the following command:  git clone https://github.com/your-username/airbnb-clone.git
2.Navigate to the Project Directory: Change your current directory to the project folder: cd airbnb-clone
3.Run the Command Interpreter: Execute the command interpreter using the following command: python3 console.py

How to Use the Command Interpreter
#To Create a New Object: Use the create command followed by the class name (e.g., create User).
#To Retrieve an Object: Use the show, all, or count commands followed by the class name (e.g., show User, all City, count Place).
#To Update an Object: Use the update command followed by the class name, object ID, attribute name, and attribute value (e.g., update User 1234 first_name "John").
#To Destroy an Object: Use the destroy command followed by the class name and object ID (e.g., destroy User 1234).
