{pkgs ? import<nixpkgs> {config.allowUnfree = true;} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.fish
    pkgs.git
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
    (pkgs.python3.withPackages (python-pkgs: with python-pkgs; [
      pandas
      numpy
      matplotlib
      seaborn
      jupyter
      pip
      pytest
    ]))
  ];
  shellHook =''
    exec fish
  '';
}