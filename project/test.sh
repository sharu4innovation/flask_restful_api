echo "Create Cluster"
curl --header "Content-Type: application/json"   --request POST   --data '{"name":"xyz","region": "ghjhg"}'   http://localhost:5000/api/manageClusters

echo "Create Machine"

curl --header "Content-Type: application/json"   --request POST   --data '{"name":"machine1","ip_address": "90.123.689.767", "instance_type":"N1", "cluster":"xyz", "tags":{"product":"muse", "price": "800"}}'   http://localhost:5000/api/manageMachines
curl --header "Content-Type: application/json"   --request POST   --data '{"name":"machine2","ip_address": "90.123.689.767", "instance_type":"N1", "cluster":"xyz", "tags":{"product":"muse", "price": "800"}}'   http://localhost:5000/api/manageMachines
curl --header "Content-Type: application/json"   --request POST   --data '{"name":"machine3","ip_address": "90.123.689.767", "instance_type":"N1", "cluster":"xyz", "tags":{"price": "800"}}'   http://localhost:5000/api/manageMachines


echo "Delete Machines by Tags"
curl --header "Content-Type: application/json"   --request PUT   --data '{"tags": {"product":"muse"}, "cluster":"xyz"}'   http://localhost:5000/api/manageMachines

echo "Delete Machines by Name"
curl --header "Content-Type: application/json"   --request PUT   --data '{"name": "machine3", "cluster":"xyz"}'   http://localhost:5000/api/manageMachines

echo "Delete Cluster"
curl --header "Content-Type: application/json"   --request PUT   --data '{"name": "xyz"}'   http://localhost:5000/api/manageClusters
