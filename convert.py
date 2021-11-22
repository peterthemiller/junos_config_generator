import juniper_display_set.junos_converter
import os
import sys
if not os.path.exists('_output/set'):
    set_folder = os.mkdir('_output/set')
results_folder = [file for file in os.listdir('_output') if os.path.isfile]
results_folder.remove('set')
for device in results_folder:
    with open('_output/set/' + device[:-4] + 'set.txt', 'w+') as f:
        sys.stdout = f
        juniper_display_set.junos_converter.get_set_config(
            ('_output/' + device), False)
