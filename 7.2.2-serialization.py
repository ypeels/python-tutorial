# json.dumps(<item>) returns the JSON string representation of <item>
# json.dump(<item>, <file>) serializes <item> to <file> as JSON
# json.load(<file>) is the inverse of json.dump()
# json.loads() is the inverse of json.dumps()

import json
l = [1, 'simple', 'list']
j = json.dumps(l)
print repr(j)               # '[1, 'simple', 'list']'
print repr(json.loads(j))   # [1, u'simple', u'list']


# This simple serialization technique can handle lists and dictionaries, 
# but serializing arbitrary class instances in JSON requires a bit of extra effort. 
# The reference for the json module contains an explanation of this.

# Alternative:
# pickle is a protocol which allows the serialization of arbitrarily complex Python objects.
# it is specific to Python and cannot be used to communicate with applications written in other languages.
# It is also insecure by default: deserializing pickle data coming from an untrusted source can execute arbitrary code, if the data was crafted by a skilled attacker.
