# Using Vagrantfile And Ansible To Create An Linux Virtual Machine For Practicing DevOps

This configuration is highly flexible and can be configured from -

- [install-requirements.yml](./infrastructure/client/install-requirements.yml) - To configure your Virtual Machine.
- [Vagrantfile](./infrastructure/client/Vagrantfile) - To configure the hardware settings like, Memory, CPU, Hostname, etc.

### Getting Started

1. Install Git ([Download Now](https://git-scm.com/download)), VirtualBox ([Download Now](https://www.virtualbox.org/wiki/Downloads)) and Vagrant ([Download Now](https://www.vagrantup.com/downloads))

2. Open Command Prompt / Terminal / PowerShell and run following -

```
  git clone https://github.com/kamal2k89/aks-one.git
  cd ./aks-one/infrastructure/client/
  vagrant up
```
