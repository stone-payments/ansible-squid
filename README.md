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
`squid_custom_configs`     
Custom configs of any kind.

Dependencies
------------

None.

Example Playbook
----------------


* To run the role with the default values just do:
  ```yml
  ---
  - name: Default playbook
    hosts: all
    become: 50
    roles:
      - role: stone-payments.squid
  ```

* If you want to create n-to-n whitelist groups:
  ```yml
  ---
  - name: Playbook creating N to N whitelist
    hosts: all
    become: true
    tasks:
      - name: include custom whitelist
        include_vars:
          file: ../files/custom_whitelist.yml
      - name: execute role
        include_role:
          name: stone-payments.squid

  ```

  The file passed should have a list of groups with `name`, a list of `src` and a list of `dest` the following format:
  ```yml
  squid_custom_whitelist:
    - name: access
      src: # list of IPs that will be allowed to access the list of domains bellow
        - 172.17.0.1
      dest: # list of domains that will be allowed to the IPs from above
        - .google.com
        - .google.com.br
  ```
  or you can add the variable `squid_custom_whitelist` in the `host_vars/group_vars`, remember to follow the same format.

* If you want to pass a config that isn't covered from the other variables, pass `squid_custom_configs`:
  ```yml
  ---
  - name: Playbook creating N to N whitelist
    hosts: all
    become: true
    tasks:
      - name: include custom whitelist
        include_vars:
          file: ../files/custom_whitelist.yml
      - name: execute role
        include_role:
          name: stone-payments.squid
        vars:
          squid_custom_configs:
            - "cache_mem 128 MB"

  ```

This role was tested with :
* `Molecule` 2.2.1
* `Docker` 18.03.0-ce
* `Ansible` 2.5.0
* `Vagrant` 2.0.2
* `Virtualbox` 5.1.34

To test the role with `Molecule` using `Vagrant` you will need to:
```
pip install python-vagrant
```

To test the role with `Molecule` using `Docker` you will need to:
```
pip install docker-py
```

In order to run the tests just execute: 
``` 
molecule test --all
```

The are 2 scenarios: 
* `default` - where it uses docker for testing;
* `vagrant` - where it uses vagrant with virtualbox for testing.

The scenario tested by default is `default`, if you want to test the other scenario, for example the `vagrant` scenario, just execute the following command passing the scenario's name:
```
molecule test -s vagrant
```
The command `molecule test` will create the containers, apply the role, execute the tests and in the end destroy everything. If you want to preserve the containers to access it you will need to execute the following commands:
```sh
molecule converge  # create and apply the role
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
