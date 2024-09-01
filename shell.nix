let
  pkgs = import <nixpkgs> {};
in pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages (python-pkgs: [
      python-pkgs.pandas
      python-pkgs.numpy
      python-pkgs.matplotlib
      python-pkgs.scipy
      python-pkgs.keyboard
      python-pkgs.pygame
    ]))
  ];
}
