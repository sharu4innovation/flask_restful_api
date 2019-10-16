# flask_restful_api
A RESTfull API built with flask to manage cloud cluster and machines

This is a take home assignment as part of an interview process: https://github.com/rorodata/careers/blob/master/backend2.md

### Authentication
This API doesn't require any authentication right now

### QuickStart

- Python3:<br>
     https://realpython.com/installing-python/

- `git clone https://github.com/sharu4innovation/flask_restful_api.git`
- RUN the API <br>
      
      python3 project/run.py

## End Points
- http://localhost:5000/api/ + 
   - /manageClusters
     - Add clusters <br>
     
       `POST json with name, region`
     - Delete cluster <br>
       
       `PUT json with name`
   - /manageMachines
     - Add machine <br>
     
       `POST json with cluster, name, ip_address, instance_type, tags (Optional)`
     - Delete machine by name <br>
        
        `PUT json with cluster, name(machine name)`
     - Delete machines by tags <br>
        
        `PUT json with tags`
 
 ## Examples

Create Cluster<br>

`curl --header "Content-Type: application/json"   --request POST   --data '{"name":"xyz","region": "ghjhg"}'   http://localhost:5000/api/manageClusters`

Run this bash script to demo all methods <br>

   ` . project/test.sh `




   





