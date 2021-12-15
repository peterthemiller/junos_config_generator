# junos_config_generator
Generates Juniper configuration files for easy deployment to a lab environment

Main device template (device_template.j2) contains basic system host-name and root-authentication configuration
Other templates add on vlans, routed interfaces, ntp, etc.
Future lab features, such as OSPF, are planned for future templates.
Other planned developments may implement excel file read-ins, perhaps from hoard format
The lab devices used are QFX-RE vms in Cisco CML. 


generate.py takes in the devices.yml and vlans.yml, and generates configuration files in _output
