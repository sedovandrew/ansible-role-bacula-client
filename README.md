Role bacula_client
==================

[![Build Status](https://travis-ci.org/sedovandrew/ansible-role-bacula-client.svg?branch=master)](https://travis-ci.org/sedovandrew/ansible-role-bacula-client)

Install and configure Bacula Client.

Role Variables
--------------

[variables](default/main.yml)

Example Playbook
----------------

    - hosts: servers
      roles:
         - role: sedovandrew.bacula_client
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
