# Local Testing

To test this Ansible Role's functionality locally, run the playbook included in this subdirectory using the following command:

    ansible-playbook playbook.yml --connection=local --ask-sudo-pass

Note: This presumes you've already installed Ansible using some other method besides `brew install ansible` :)

## Remove Homebrew Entirely

It's a little messy, but...

    # Run this command and answer 'y' when prompted.
    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/uninstall)"
    
    # Delete leftovers.
    rm -rf /usr/local/Homebrew
    rm -rf /usr/local/bin/brew
    ... [other files identified by installer script] ...

This assumes you're using the default values in this role's `defaults/main.yml`.
