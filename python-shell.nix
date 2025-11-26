{pkgs ? import<nixpkgs> {config.allowUnfree = true;} }:

pkgs.mkShell {
  name = "python-env";
  packages = [
    pkgs.fish
    pkgs.git

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
        njpwerner.autodocstring

        pkief.material-icon-theme
        bbenoist.nix
      ];
    })

    # VS Code with extensions
    # (pkgs.vscode-with-extensions.override {
    #   vscodeExtensions = with pkgs.vscode-extensions; [
    #     ms-python.python
    #     ms-python.debugpy
    #     ms-toolsai.jupyter
    #     ms-python.flake8
    #     # ms-python.vscode-pylance
    #     # ms-python.black-formatter
    #     # njpwerner.autodocstring
    #     # almenon.arepl

    #     pkief.material-icon-theme
    #     bbenoist.nix
    #   ];
    # })

    # Python environment
    (pkgs.python3.withPackages (python-pkgs: with python-pkgs; [
      pandas
      numpy
      matplotlib
      seaborn
      jupyter
      pip
      pytest
      flake8
      debugpy
    ]))
  ];
}