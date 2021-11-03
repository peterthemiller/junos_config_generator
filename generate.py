from jinja2 import Environment, FileSystemLoader
import yaml
import pdb
import os
with open('devices.yml', 'r') as f:
    devices = yaml.safe_load(f)

with open('vlans.yml', 'r') as f:
    vlans = yaml.safe_load(f)
output_directory = "_output"
if not os.path.exists(output_directory):
    os.mkdir(output_directory)


def customize_vlans(core_node, vlan_list):
    '''
    Takes in a Core Node, string like "CN1" and a list of vlan dictionaries
    renames vlans, and gives them a vlan-id per core node. 
    for now, only takes in single-digit CN numbers
    returns a list of vlan dictionaries
    '''
    for vlan in vlan_list:
        vlan['name'] = core_node + '_' + vlan['name']
        vlan['description'] = core_node + '_' + vlan['description']
        vlan['id'] = core_node[-1] + str(vlan['id'])
    return vlan_list


# press c to continue
# type a variable name to see the data
# pdb.set_trace()
loader = FileSystemLoader('./templates')
# trim_blocks keeps there from being unexpected white space after each vblock
# this would apply to comments even!
# lstrip_blocks keeps stuff from indenting unexpectedly
# https://blog.networktocode.com/post/whitespace-control-in-jinja-templates/ on whitespace control
# or look https://ttl255.com/jinja2-tutorial-part-3-whitespace-control/ at this if you want to die
env = Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)
vlan_temp = env.get_template('vlans.j2')
rendered = vlan_temp.render(vlans)


for device in devices['devices']:
    # adding in vlan template to device template
    device['vlans'] = vlans['vlans']
    # transforming device vlan configuration to be CN-specific
    device['vlans'] = customize_vlans(device['CN'], device['vlans'])
    # loading in device template
    device_template = env.get_template('device_template.j2')
    # render device .conf file
    device_config = device_template.render(device)
    # creates file in ./_output
    f = open(os.path.join(output_directory,
             device['hostname'] + ".conf"), "w+")
    f.write(device_config)
    f.close()
    print(f"Configuration for {device['hostname']} created")
print("DONE")
