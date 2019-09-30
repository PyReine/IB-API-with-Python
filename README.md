# IB-API-with-Python
The repository contains the useful links to connect to IB API and some codes to command the data :

IB has the detail document about their API which can be found in the following link:
https://interactivebrokers.github.io/tws-api/initial_setup.html

The important step concerns enabling ActiveX and Socket Client. If you'd like to connect to the production account, you can use the socket port "7496" and if you choose to connect to the paper account, you can use the socket port "7497".
The socket port is also needed later in the coding part to establish the connection between IB API and your IDE(integrated development environment):
ib.connect('127.0.0.1', 7496, clientId=2)
You can find the detaill of the code in the connecting to IB API.py 

Data reprocessing.py file provides the data manipulation using Pandas. The minutes data extracted from IB don't contain the close price for each day. Thus, a manipulation is needed here to combine the dataset so that the prediction of the close price can be processed based on the minites data. The difficulty here is to match the dates between two sources. 
