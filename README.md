# Ansible Role: Homebrew

[![Build Status][travis-badge]][travis-link]
[![MIT licensed][mit-badge]][mit-link]
[![Galaxy Role][role-badge]][galaxy-link]

Installs [Homebrew][homebrew] on MacOS, and configures packages, taps, and cask apps according to supplied variables.

## Requirements

None.

## Role Variables

Available variables are listed below, along with default values (see [`defaults/main.yml`](defaults/main.yml)):

    homebrew_repo: https://github.com/Homebrew/brew

The GitHub repository for Homebrew core.

    homebrew_prefix: /usr/local
    homebrew_install_path: "{{ homebrew_prefix }}/Homebrew"

The path where Homebrew will be installed (`homebrew_prefix` is the parent directory). It is recommended you stick to the default, otherwise Homebrew might have some weird issues. If you change this variable, you should also manually create a symlink back to /usr/local so things work as Homebrew expects.

    homebrew_brew_bin_path: /usr/local/bin

The path where `brew` will be installed.

    homebrew_installed_packages:
      - ssh-copy-id
      - pv
      - { name: vim, install_options: "with-luajit,override-system-vi" }

Packages you would like to make sure are installed via `brew install`. You can optionally add flags to the install by setting an `install_options` property, and if used, you need to explicitly set the `name` for the package as well.

    homebrew_uninstalled_packages: []

Packages you would like to make sure are _uninstalled_.

    homebrew_upgrade_all_packages: no

Whether to upgrade homebrew and all packages installed by homebrew. If you prefer to manually update packages via `brew` commands, leave this set to `no`.

    homebrew_taps:
      - homebrew/cask

Taps you would like to make sure Homebrew has tapped.

    homebrew_cask_apps:
      - firefox

Apps you would like to have installed via `cask`. [Search][caskroom] for popular apps to see if they're available for install via Cask. Cask will not be used if it is not included in the list of taps in the `homebrew_taps` variable.

    homebrew_cask_uninstalled_apps:
      - google-chrome

Apps you would like to make sure are _uninstalled_.

    homebrew_cask_appdir: /Applications

Directory where applications installed via `cask` should be installed.

    homebrew_use_brewfile: true

Whether to install via a Brewfile. If so, you will need to install the `homebrew/bundle` tap, which could be done within `homebrew_taps`.

    homebrew_brewfile_dir: '~'

The directory where your Brewfile is located.

## Dependencies

  - [elliotweiser.osx-command-line-tools][dep-osx-clt-role]

## Example Playbook

    - hosts: localhost
      vars:
        homebrew_installed_packages:
          - mysql
      roles:
        - geerlingguy.homebrew

See the `tests/local-testing` directory for an example of running this role over
Ansible's `local` connection. See also:
[Mac Development Ansible Playbook][mac-dev-playbook].

## License

[MIT][mit-link]

## Author Information

This role was created in 2014 by [Jeff Geerling][author-website], author of
[Ansible for DevOps][ansible-for-devops].

#### Maintainer(s)

- [Jeff Geerling](https://github.com/geerlingguy)
- [Elliot Weiser](https://github.com/elliotweiser)

[ansible-for-devops]: https://www.ansiblefordevops.com/
[author-website]: https://www.jeffgeerling.com/
[caskroom]: https://caskroom.github.io/search
[galaxy-link]: https://galaxy.ansible.com/geerlingguy/homebrew/
[homebrew]: http://brew.sh/
[mac-dev-playbook]: https://github.com/geerlingguy/mac-dev-playbook
[mit-badge]: https://img.shields.io/badge/license-MIT-blue.svg
[mit-link]: https://raw.githubusercontent.com/geerlingguy/ansible-role-homebrew/master/LICENSE
[dep-osx-clt-role]: https://galaxy.ansible.com/elliotweiser/osx-command-line-tools/
[role-badge]: https://img.shields.io/ansible/role/1858.svg
[travis-badge]: https://travis-ci.org/geerlingguy/ansible-role-homebrew.svg?branch=master
[travis-link]: https://travis-ci.org/geerlingguy/ansible-role-homebrew
