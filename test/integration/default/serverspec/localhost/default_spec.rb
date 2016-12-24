$LOAD_PATH.unshift(File.dirname(File.dirname(__FILE__)))
require 'spec_helper'

describe 'ansible-geerlingguy.homebrew::default' do

  describe package('ruby') do
    it { should be_installed }
  end

  describe file('/tmp/homebrew') do
    it { should be_directory }
  end

end
