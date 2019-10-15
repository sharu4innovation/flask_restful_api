from flask_restful import Resource
from flask import Flask, jsonify, request
import pickle
import ast
import os
from resources.cluster import Cluster


def read_state():
    if os.path.exists('cloud.txt'):
        b = open('cloud.txt', 'r')
        b = b.read()
        cloud = {}
        cloud = pickle.loads(ast.literal_eval(b))
    else:
        cloud = {}
    return cloud

def get_json_obj(cloud):
    json_obj = {i: cloud[i].__dict__ for i in list(cloud.keys())}
    for i in json_obj:
        for j in json_obj[i]['machines']:
            json_obj[i]['machines'][j] = json_obj[i]['machines'][j].__dict__
    return json_obj

def save_state(cloud):
    b = str(pickle.dumps(cloud))
    f = open('cloud.txt', "w")
    f.write(b)
    f.close()
    return get_json_obj(cloud)


class Manage_Clusters(Resource):

    def post(self):
        try:
            json_data = request.get_json(force=True)
            name = json_data['name']
            region = json_data['region']
            cloud = read_state()
            cloud[name] = Cluster(name, region)
            return {"cloud response" : save_state(cloud)}
        except KeyError:
            return {"cloud API response": "input all mandatory args, refer docs"}

    def put(self):
        json_data = request.get_json(force=True)
        name = json_data['name']
        cloud = read_state()
        if cloud.get(name):
            del cloud[name]
            return {"cloud API response": save_state(cloud)}
        else:
            return {"cloud API response" : "cluster not found"}

    def get(self):
        cloud = read_state()
        return get_json_obj(cloud)


class Manage_Machines(Resource):

    def post(self):
        try:
            json_data = request.get_json(force=True)
            name = json_data['name']
            cluster = json_data['cluster']
            ip_address = json_data['ip_address']
            instance_type = json_data['instance_type']
            tags = json_data.get('tags')
            cloud = read_state()
            cloud[cluster].create_machine(cluster, name, ip_address, instance_type, tags=tags)
            return {"cloud API response": save_state(cloud)}
        except KeyError:
            return {"cloud API response": "input all mandatory args, refer docs"}

    def put(self):
        json_data = request.get_json(force=True)
        cluster = json_data['cluster']
        name = json_data.get('name')
        tags = json_data.get('tags')
        cloud = read_state()

        try:
            if(tags):
                cloud[cluster].delete_machines(tags=tags)
            elif name:
                cloud[cluster].delete_machines(name = cloud[cluster].machines[name].name)
            else:
                return {"cloud API response": "input all mandatory args, refer docs"}
            return {"cloud API response": save_state(cloud)}
        except KeyError:
            return {"cloud API response": "machine not found"}

    def get(self):
        cloud = read_state()
        return get_json_obj(cloud)




