{pkgs ? import<nixpkgs> {config.allowUnfree = true;} }:

pkgs.mkShell {
  name = "python-env";
  buildInputs = [
    pkgs.fish
    pkgs.git
    # VS Code with extensions
    (pkgs.vscode-with-extensions.override {
      vscodeExtensions = with pkgs.vscode-extensions; [
        ms-python.python
        ms-python.debugpy
        ms-toolsai.jupyter
        ms-python.vscode-pylance
        ms-python.black-formatter
        ms-python.flake8
        njpwerner.autodocstring
        almenon.arepl

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
      pip
      pytest
      flake8
      debugpy
    ]))
  ];
  shellHook =''
    exec fish
  '';
}