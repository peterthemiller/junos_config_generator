import juniper_display_set.junos_converter
import os
import sys
results_folder = [file for file in os.listdir('_output') if os.path.isfile]
print(results_folder)
if not os.path.exists('_output/set'):
    set_folder = os.mkdir('_output/set')
for device in results_folder:
    with open('_output/set/' + device, 'w+') as f:
        sys.stdout = f
        juniper_display_set.junos_converter.get_set_config(
            ('_output/' + device), False)
