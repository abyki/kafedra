from __future__ import absolute_import, division, print_function
__metaclass__ = type
import json

ANSIBLE_METADATA = {'status': ['preview'],
          'supported_by': 'community',
          'version': '1.1'}

def main():
  argument_spec = openstack_full_argument_spec(
    name=dict(required=False),
   # public_key=dict(required=False),
   # filters=dict(type='dict', required=False),
   # all_projects=dict(required=False, type='bool', default=False),
   # detailed=dict(required=False, type='bool', default=False),
  )

  module_kwargs = openstack_module_kwargs()

  module = AnsibleModule(argument_spec,**module_kwargs)
 # name = module.params['name']
 # public_key = module.params['public_key']
 # filters = module.params['filters']
 # all_projects=module.params['all_projects']
  sdk, cloud = openstack_cloud_from_module(module)
  try:
    key = cloud.list_keypairs()
    module.exit_json(key = key)
  except sdk.exception.OpenStackCloudException as e:
    module.fail_json(msg=str(e))

from ansible.module_utils.basic import *
from ansible.module_utils.openstack import *
if __name__ == '__main__':
  main()
