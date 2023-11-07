import wavedrom
svg = wavedrom.render("""
{ 	"signal" : 
	[
		{ "name": "CTRL",          "wave": "0====|===0", "data": ["FWD (C2)", "DTW (C0)", "DTW (C0)", " ", "DTW (C0)", "DTW (C0)", "LDW (EA)"] }, 
		{},
		["DATA",
				{ "name": "Col 0", "wave": "0====|===0", "data": ["sample 0", "sample 1", "sample 2", " ", "sample 1355", "sample 1356", "sample 1357"] },
				{ "name": "Col 1", "wave": "0====|===0", "data": ["sample 0", "sample 1", "sample 2", " ", "sample 1355", "sample 1356", "sample 1357"] },
				{ "name": "Col 2", "wave": "0====|===0", "data": ["sample 0", "sample 1", "sample 2", " ", "sample 1355", "sample 1356", "sample 1357"] },
				{ "name": "Col 3", "wave": "0====|===0", "data": ["sample 0", "sample 1", "sample 2", " ", "sample 1355", "sample 1356", "sample 1357"] }
		]

	],

	"config" : { "hscale" : 3 }
} 
""")
svg.saveas("expertise-dump.svg")