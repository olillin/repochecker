# Git Repo Checker

[![PyPI - Version](https://img.shields.io/pypi/v/gitrepochecker?style=flat-square&logo=Python&logoColor=white)](https://pypi.org/project/gitrepochecker)

CLI to get status of git repositories.

## Installation

### Pip

To install using **pip** simply run the command below:

```console
pip install gitrepochecker
```

### Nix/NixOS

Repo checker can be installed using [Nix Flakes](#nix-flakes), see the section below.

#### Nix Flakes

Add the required inputs to your flake configuration:

`flake.nix`

```nix
{
  description = "NixOS configuration with gitrepochecker";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-25.11";

    repochecker = {
      url = "github:olillin/repochecker";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = {
    self,
    nixpkgs,
    ...
  } @ inputs: {
    nixosConfigurations.yourconfiguration = nixpkgs.lib.nixosSystem {
      specialArgs = {inherit inputs;};
      modules = [
        ./configuration.nix
      ];
    };
  };
}
```

Install the package in your `configuration.nix` or an imported module:

`configuration.nix`

```nix
{
  pkgs,
  inputs,
  ...
}: {
  environment.systemPackages = with pkgs; [
    inputs.repochecker.packages.${pkgs.stdenv.hostPlatform.system}.default
  ];
}
```


## Usage

```console
usage: repochecker [-h] [-i | -a] [-s | -r] [-d RECURSION_DEPTH] [-b] directory

Check git repository information and get a summary

positional arguments:
  directory

options:
  -h, --help            show this help message and exit
  -i, --invert
  -a, --all
  -s, --single
  -r, --recursive
  -d RECURSION_DEPTH, --recursion-depth RECURSION_DEPTH
  -b, --brief
```

## Example response

```console
C:\Users\oli\Workspaces>repochecker .

C:\Users\oli\Workspaces\Blockstates
 Is git repo: False


C:\Users\oli\Workspaces\RepoChecker
 Is git repo: True
 Current branch: None
 Branches: 
  * main -> origin/main
 No uncommited changes: False
 No unpushed commits: True
 No stashed changes: True


C:\Users\oli\Workspaces\XaeroMerge
 Is git repo: True
 Current branch: None
 Branches: 
  * main -> origin/main ahead 1
 No uncommited changes: False
 No unpushed commits: False
 No stashed changes: True
```
