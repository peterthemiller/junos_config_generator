from jinja2 import Environment, FileSystemLoader
import yaml
import pdb
import os
import copy

with open('devices.yml', 'r') as f:
    devices = yaml.safe_load(f)

with open('vlans.yml', 'r') as f:
    vlans = yaml.safe_load(f)
output_directory = "_output"
if not os.path.exists(output_directory):
    os.mkdir(output_directory)


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

for device in devices['devices']:
    device['vlans'] = vlans['vlans']
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
