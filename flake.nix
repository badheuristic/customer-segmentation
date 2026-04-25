{
  description = "customer segmentation analysis env";
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  };
  outputs = { self, nixpkgs }:
  let
    system = "x86_64-linux";
    pkgs = nixpkgs.legacyPackages.${system};
  in
  {
    devShells.${system}.default = pkgs.mkShell {
      buildInputs = [
        (pkgs.python3.withPackages (ps: with ps; [
          numpy
          matplotlib
          seaborn
          pandas
          scikit-learn
        ]))
      ];
      shellHook = ''
        echo "environment loaded."
        python --version
      '';
    };
  };
}
