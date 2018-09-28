Role bacula_client
==================

Install and configure Bacula Client.

Role Variables
--------------

[variables](default/main.yml)

Example Playbook
----------------

    - hosts: servers
      roles:
         - role: bacula_client
           become: true
           bacula_client_director: BaculaDirector
           bacula_client_password: ClientPassword
           bacula_client_name: BaculaFirstClient

License
-------

BSD

Author Information
------------------

Sedov Andrey - sedoy80@gmail.com
