from nornir.core.inventory import Host, Group, Defaults
import json

print(json.dumps(Host.schema(), indent=4))
print(json.dumps(Group.schema(), indent=4))
print(json.dumps(Defaults.schema(), indent=4))