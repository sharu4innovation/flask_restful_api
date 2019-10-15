class Machine():
    def __init__(self, name, ip_address, instance_type, cluster, **kwargs):
        self.name = name
        self.ip_address = ip_address
        self.instance_type = instance_type
        self.cluster = cluster
        self.tags = kwargs.get("tags")
        self.status = 'Not Running'

class Cluster():
    def __init__(self, region, name):
        self.region = region
        self.machines = {}

    def create_machine(self, cluster, name, ip_address, instance_type, **kwargs):
        self.machines[name] = Machine(name, ip_address, instance_type, cluster, tags = kwargs['tags'])

    def delete_machines(self, **kwargs):

        if kwargs.get('tags'):
            machine_list = []
            for name, machine in self.machines.items():
                if (kwargs.get('tags').items() <= machine.tags.items()):
                    machine_list.append(name)
            for i in self.machines.copy():
                if i in machine_list:
                    self.machines.pop(i)

        else:
            if self.machines.get(kwargs.get('name')):
                del self.machines[kwargs.get('name')]
            else:
                return False
