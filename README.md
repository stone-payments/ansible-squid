squid
=========

Ansible role to install and configure squid proxy/cache in RedHat/CentOS/Debian/Ubuntu.

Requirements
------------

No specific requirements.

Role Variables
--------------

This role uses a mix of defaults and `host_vars/group_vars`.     
The defaults are used to set the most common squid config, present by default in the package repository.     
The `host_vars/group_vars` are best suited to create custom ACLs and http_access sentences.

### Globals
Variables listed in `defaults/main.yml`

`squid_localnets`     
List of internal subnets, used to create the default ACL named localnet.

`squid_sslports`     
List of ports authorized to used the CONNECT methhod, encrypted traffic.

`squid_safeports`     
List of ports authorized to use HTTP in plain text.

`squid_port`     
Port that squid daemon runs.

`squid_outgoing_adress`     
If specified, tells which IP address to direct the traffic.

`squid_visible_hostname`
Visible proxy name. Appears in authentication dialog.

`squid_acls`     
ACLs from default squid.conf. Can be used to create custom ACLs.

`squid_http_access`     
http_access directives from default squid.conf. Can be used to create custom http_access.

`squid_refresh_pattern`     
List of refresh_paterrn from defalt squid.conf. Can be used to create custom refresh_pattern.

### Custom
Custom variables. Can be used in `defaults/main.yml`, but it was made to best if in `host_vars` and `group_vars`.

`squid_custom_localnets`     
Custom localnets.

`squid_custom_sslports`     
Custom SSL ports.

`squid_custom_safeports`     
Custom HTTP ports.

`squid_custom_acls`     
Custom ACLs.

`squid_custom_http_access`     
Custom http_access directives.

`squid_custom_refresh_pattern`     
Custom refresh_pattern directives.

`squid_custom_whitelist`     
Custom whitelist groups made of a name, **N** hosts and **N** domains.

Dependencies
------------

None.

Example Playbook
----------------

This role comes with a Vagrant file. Just fire a `vagrant up` for testing.     
Once the environemnt is up, just run `vagrant provision` or `ansible-playbook -i tests/inventory tests/test.yml`.     
As the date of this commit, the parameter `host_key_checking=False` it's not working. If some SSH connection error occurs, try to execute `export ANSIBLE_HOST_KEY_CHECKING=False`.
You can use the tests/vars.yml as a playground to test the variables.

License
-------

MIT

Author Information
------------------

Jonatas Baldin      
<mailto:jonatas.baldin@gmail.com>      
http://deployeveryday.com
