{pkgs ? import<nixpkgs> {config.allowUnfree = true;} }:

pkgs.mkShell {
  name = "python-env";
  packages = [
    # pkgs.fish
    pkgs.git
    pkgs.wget

    # VS Code FHS
    (pkgs.vscode.fhsWithPackages (ps: with ps; [
      python3
      jupyter
      nix
    ]) // { # this bit doesn't seem to work :(
      vscodeExtensions = with pkgs.vscode-extensions.override; [
        ms-python.python
          ms-python.debugpy
          ms-toolsai.jupyter
          ms-python.pylint
          ms-python.vscode-pylance

        pkief.material-icon-theme
        bbenoist.nix
      ];
    })

    # Python environment
    (pkgs.python3.withPackages (python-pkgs: with python-pkgs; [
      pandas
      numpy
      matplotlib
      seaborn
      jupyter
      pytest
      flake8
      debugpy
      openpyxl
      xlrd
    ]))
  ];
}