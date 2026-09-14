(* Shared package setup; keep process/kinematic assumptions in calculations.
   Optional local_config.wl may extend $Path for an existing installation. *)
Module[{localConfig = FileNameJoin[{DirectoryName[$InputFileName], "local_config.wl"}]},
  If[FileExistsQ[localConfig],
    If[Check[Get[localConfig]; True, False] =!= True, Return[$Failed]]
  ];
  If[!And @@ (StringQ[Quiet[FindFile[#]]] & /@ {"FeynCalc`", "FeynGrav`"}),
    Print["FAIL: FeynCalc or FeynGrav is not on $Path. See the Mathematica README."];
    Return[$Failed]
  ];
  If[Check[Needs["FeynCalc`"]; Needs["FeynGrav`"]; True, False] =!= True,
    Return[$Failed]
  ];
  And @@ (MemberQ[$Packages, #] & /@ {"FeynCalc`", "FeynGrav`"})
]
