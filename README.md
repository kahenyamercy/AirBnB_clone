# AirBnB_clone - The Console

## AirBnB_clone Description

`AirBnB` is a web application that helps people discover their perfect homes. You can view the source of idea by clicking [airbnb.com](https://www.airbnb.com/). Now the `AirBnB_clone` is a learning project at ALX with an aim to help us utilize the skills we have so far learnt by collectively and collaboratively build a replica of the application.

This project being a full web application, it have been divided into various part, the console being the first one, where we now deal with managing the data for this application. Now let us see what `The Console` part entails.

## The Console
The console part involves having an interactive console (a command interpreter) that will help us interact with the data. Basically, the console we enable us to perform various `CRUD` operations.

In this part, we use Python skilss to effectively manage data needed in `AirBnB` application by defining the following models:
1. User - Handles user information
2. State - Handles the state information
3. City - Handles the city information
4. Place - Handles the place information (the homes)
5. Amenity - This are the services that comes with the home you choose
6. Review - This handles all the information about place reviews and who reviewed.

> All these models have some of the information that they all keep that is common among them. Therefore we have another models `BaseModel` that handles this common information.

In this part, we are utilizing file storage (JSON file) to store our data. 

## Command Interpreter

The command interpreter allows users to:
- Create: Instantiate new objects such as User, Place, etc.
- Retrieve: Access objects from files, databases, etc.
- Perform Operations: Conduct operations on objects (e.g., count, compute stats).
- Update: Modify attributes of an object.
- Destroy: Delete an object.


## Starting the Command Interpreter
1. Clone the Repository: 
```
git clone https://github.com/your-username/airbnb-clone.git

```
2. Navigate to the Project Directory:
```
cd airbnb-clone
```
3. Run the Command Interpreter:
```
./console.py
```

## Using Command Interpreter

### Creating new object
To create a new instance of any of the classes use the following syntax `create <class name>`
Example usage
```
create User
```
The `<class name>` must be among the defined models of the project.

### Retrieving an Object
To get a string representation of an certain instance based on the id use `show <class name> <id>`
Example usage:
```
show User 3304c837-fd91-4d4b-b93a-2ebb8669d6b7
```

Alternatively, you can use the format `<class name>.show(<id>)`

```
User.show("3304c837-fd91-4d4b-b93a-2ebb8669d6b7")
```
> Note that the second format requires you to wrap the `id` in quotes `"" or ''`

### Retrieving all objects
To retrieve all the instances use the below command
```
all
```
You can specify the class whose instance to be retrieved by add the `<class name>`
```
all User
```

Alternatively, you can use the format `<class name>.all()` to retrieve all instances of a certain class
```
User.all()
```

### Updating an Object
To update an object use `update <class name> <id> <attribute name> "<attribute value>"`
Example usage
```
update User 3304c837-fd91-4d4b-b93a-2ebb8669d6b7 last_name "Wamae"
```

Alternatively, you can use the format `<class name>.update(<id>, <attribute name>, <attribute value>)`
```
User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "first_name", "John")
```
> The above methods can only update one attribute of the instance at a time.

To update multiple attributes of an instance you can use the dictionary method as follow
`<class name>.update(<id>, <dictionary representation>)`
Example usage
```
User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", {'first_name': "Wamae", "age": 20})
```

### Destroying an Object
To destroy an object use `destroy <class name> <id>`
Example usage
```
destroy User 3304c837-fd91-4d4b-b93a-2ebb8669d6b7
```
Alternatively, you can use the format `<class name>.destroy(<id>)`
```
User.destroy("3304c837-fd91-4d4b-b93a-2ebb8669d6b7")
```

### Getting class instances count
To get to know how many instance of a certain class you have, use `<class name>.count()`
Example use
```
User.count()
```

### Future Updates
This is just the first part of the `AirBnB_clone` and in future we will have more projects: HTML/CSS templating, database storage, API, front-end integration… that will build on top of this part to have a full web application as the end product.
