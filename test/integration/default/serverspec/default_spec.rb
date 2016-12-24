require_relative 'spec_helper'

describe 'ansible-geerlingguy.homebrew::default' do

  describe package('ruby') do
    it { should be_installed }
  end

  describe package('gcc') do
    it { should be_installed }
  end

  describe file('/home/kitchen/.linuxbrew/bin') do
    it { should be_directory }
  end

  describe file('/home/kitchen/.linuxbrew/bin/brew') do
    it { should be_file }
  end

  describe file('/home/kitchen/.linuxbrew/bin/patchelf') do
    it { should be_symlink }
  end

  describe file('/home/kitchen/.linuxbrew/lib/ld.so') do
    it { should be_symlink }
  end

  describe file('/home/kitchen/.linuxbrew/lib/libz.so') do
    it { should be_symlink }
  end

  describe file('/home/kitchen/.linuxbrew/lib/libz.a') do
    it { should be_symlink }
  end

  describe file('/home/kitchen/.linuxbrew/lib/pkgconfig') do
    it { should be_directory }
  end

end
