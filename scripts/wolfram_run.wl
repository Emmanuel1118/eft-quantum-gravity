(* Environment variables transport paths without generating/evaluating code. *)
SetOptions[$Output, FormatType -> OutputForm];
If[!StringQ[Environment["EFT_WOLFRAM_SOURCE"]] ||
    !FileExistsQ[Environment["EFT_WOLFRAM_SOURCE"]] ||
    !StringQ[Environment["EFT_WOLFRAM_COMPLETION"]], Exit[1]];
If[!TrueQ[SyntaxQ[Import[Environment["EFT_WOLFRAM_SOURCE"], "Text"]]],
  Print["FAIL: invalid Wolfram Language syntax in source file."]; Exit[1]
];

(* Exit[0] in the source also runs $Epilog. The parent checks the native exit
   code as well, so Exit[1] still fails even when this marker is written. *)
$Epilog := Export[Environment["EFT_WOLFRAM_COMPLETION"], "COMPLETED", "Text"];
If[CheckAbort[Get[Environment["EFT_WOLFRAM_SOURCE"]], $Failed] === $Failed,
  Exit[1]
];
Exit[0];
