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
* example:
    ```yml
    squid_custom_whitelist:
      - name: access
        src:
          - 172.17.0.1
        dest:
          - .google.com
          - .google.com.br
    ```
Dependencies
------------

None.

Example Playbook
----------------

This role was tested with :
* `Molecule` 2.2.1
* `Docker` 18.03.0-ce
* `Ansible` 2.5.0

In order to run the tests just execute: 
``` 
molecule test --all
```

The are 2 scenarios: 
* `default` - where only the default config are used;
* `custom_whitelist` - where it is used the option to whitelist groups made of a name, **N** hosts and **N** domains. 

The scenario tested by default is `default`, if you want to test the `custom_whitelist` scenario, just execute the following command:
```
molecule test -s custom_whitelist
```
The command `molecule test` will create the containers, apply the role, execute the tests and in the end destroy everything. If you want to preserve the containers to access it you will need to execute the following commands:
```sh
molecule create  # create the enviroment 
molecule converge  # apply the role
molecule login  # login in the container
```
Whenever you are done with the tests you can clean the environment running the command:
```
molecule destroy --all
```

License
-------

MIT

Author Information
------------------

Igor Blackman     
<mailto:iblackman@stone.com.br>
