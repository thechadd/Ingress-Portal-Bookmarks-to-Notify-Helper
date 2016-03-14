import json
import sys

output = ""
portal_count = 0

def format_portal(portal_name):
    """formats portal name for json output into Notify Helper"""
    return "\n  {\n    \"name\": \"%s\",\n    \"address\": \"\",\n    \"favorite\": true,\n    \"ignore\": false\n  }," %portal_name

# Retrieve script arguments

try:
    if len(sys.argv) != 4:
        raise Exception("Not enough arguments. Usage: python [this script name] [Portal Group]" +
                        "[input json file] [output json file]")
    else:
        bookmark_group = sys.argv[1]
        import_file    = sys.argv[2]
        out_file       = sys.argv[3]

except Exception as e:
    print("Argument retrieval failed: " + str(e))
    exit(0)


# Open and parse json input file
with open(import_file) as data_file:
    data = json.load(data_file)

# Find portal group and extract the portal names
for group_id in data['portals']:
        if data['portals'][group_id]['label'] == bookmark_group:
            print("Found Group: "+data['portals'][group_id]['label'])
            for portal_id in data['portals'][group_id]['bkmrk']:
                portal_count += 1
                print("Portal found: " + data['portals'][group_id]['bkmrk'][portal_id]['label'])
                output += format_portal(data['portals'][group_id]['bkmrk'][portal_id]['label'])
            break
#strip the last comma
output = output.strip(",")

with open(out_file, 'w') as of:
    of.write("{\n\"custom\": [")
    of.write(output)
    of.write("\n]\n}")
    print("%d portals exported." % portal_count)