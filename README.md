# Flight-Aware
Our project is Flight Aware, a massive database of flights around the world. Our simple database allows for infinite possibilities with managing flight information, no matter how big the dataset. 

In our code we have functions for reading, inserting, updating, and deleting for each individual table, since each table has different combinations of information and these functions needed to be created individually for each one. Using our main function, the user can select which table they want to access information from.

Once the user selects a table, they are prompted to pick what function they want to run, between reading, inserting, updating and deleting. Once they select, they will be prompted for the necessary information to execute the process. 

If the user enters data that does not correspond to the format that is required for the data, and error will be shown and the user will be prompted to try again, specifying the parameters. 

If the user tries to update/delete something that does not exist, they will also be given an error and prompted to try again. All outcomes are accounted for and error-checking methods are implemented to make sure that the user has the easiest experience to access the flight data they need. 

After a function is executed, a message is shown to confirm to the user it has been completed, and the user will be prompted to perform another function or exit. 

