import semver


def check_homebrew_can_manage_dir(host, directory_str):
    directory = host.file(directory_str)
    assert directory.exists
    assert directory.is_directory
    assert directory.user == host.user().name
    assert directory.group == 'admin'
    assert directory.mode == 0o775


def test_parent_dir_permissions(host):
    parent_dir = host.file('/usr/local')
    assert parent_dir.exists
    assert parent_dir.is_directory
    assert parent_dir.user == 'root'

    # Only test group and permissions on Sierra and older
    if semver.match(host.system_info.release, "<10.13.0"):
        assert parent_dir.group == 'admin'
        assert parent_dir.mode == 0o775


def test_homebrew_install_path(host):
    check_homebrew_can_manage_dir(host, '/usr/local/Homebrew')


def test_homebrew_bin_dir(host):
    check_homebrew_can_manage_dir(host, '/usr/local/bin')


def test_homebrew_bin_path(host):
    bin_path = '/usr/local/bin/brew'
    p = host.file(bin_path)
    assert p.exists
    assert p.is_symlink
    # Reference: https://github.com/philpep/testinfra/pull/263
    # assert p.linked_to == '/usr/local/Homebrew/bin/brew'
    assert p.user == 'root'
    assert p.group == 'admin'
    assert p.mode == 0o755


def test_brew_is_installed(host):
    cmd = host.run('/usr/local/bin/brew --version')
    assert cmd.rc == 0
    output = cmd.stdout.split('\n')[0].split(' ')
    assert output[0] == 'Homebrew'
    assert semver.parse(output[1])


def test_brew_taps(host):
    cmd = host.run('/usr/local/bin/brew tap --list')
    assert cmd.rc == 0
    tapped = cmd.stdout.split()
    assert 'homebrew/core' in tapped
    assert 'caskroom/cask' in tapped


def test_brew_list(host):
    cmd = host.run('/usr/local/bin/brew list')
    assert cmd.rc == 0
    installed = cmd.stdout.split()
    assert 'pv' in installed
    assert 'ssh-copy-id' in installed


def test_brew_cask_list(host):
    cmd = host.run('/usr/local/bin/brew cask list')
    assert cmd.rc == 0
    installed = cmd.stdout.split()
    assert 'firefox' in installed
