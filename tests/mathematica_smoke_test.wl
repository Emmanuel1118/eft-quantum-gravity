(* Run in a fresh local kernel. No research calculation or notebook frontend. *)
Print["Kernel: ", $Version];
If[2 + 2 =!= 4, Print["FAIL: basic evaluation"]; Exit[1]];
Print["PASS: basic evaluation"];

If[CheckAbort[
    Get[FileNameJoin[{DirectoryName[$InputFileName], "..", "calculations",
      "mathematica", "setup.wl"}]], $Failed] =!= True,
  Print["FAIL: setup.wl"]; Exit[1]
];
Print["PASS: setup.wl"];

If[!MemberQ[$Packages, "FeynCalc`"] ||
    FeynCalc`DiracTrace[1, FeynCalc`DiracTraceEvaluate -> True] =!= 4,
  Print["FAIL: FeynCalc"]; Exit[1]
];
Print["PASS: FeynCalc ", FeynCalc`$FeynCalcVersion];

If[!MemberQ[$Packages, "FeynGrav`"] ||
    Length[DownValues[FeynGrav`GravitonScalarVertex]] == 0 ||
    FeynGrav`ScalarPropagator[smokeMomentum, smokeMass] =!=
      I FeynCalc`FAD[{smokeMomentum, smokeMass}],
  Print["FAIL: FeynGrav"]; Exit[1]
];
Print["PASS: FeynGrav definitions and scalar propagator"];
Print["PASS: MATHEMATICA_SMOKE_TEST"];
Exit[0];
