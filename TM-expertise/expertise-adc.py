import wavedrom
svg = wavedrom.render("""
{ 	"signal" : 
	[
     	{"node": ".A.................B"},
     	{"node": ".C...........D"},
     	{"node": ".E.....F"},

		{ "name": "CTRL",          "wave": "x===|=====|====|==x", "data": ["DTV (CA)", "DTW (C0)", " ", "DTW (C0)", "LDW (EA)", "ERR (E2)", "DTW (C0)", " ", "DTW (C0)", "LDW (EA)", "DTV (CA)", " ", "DTW (C0)", "LDW (EA)"] }, 
		{},
		["DATA",
				{ "name": "Col 0", "wave": "x===|=====|====|==x", "data": ["pixel 0", "pixel 1", " ", "pixel 32", "pixel 33", "pixel 0", "pixel 1", " ", "pixel 32", "pixel 33", "pixel 0", " ", "pixel 32", "pixel 33"] },
				{ "name": "Col 1", "wave": "x===|=====|====|==x", "data": ["pixel 0", "pixel 1", " ", "pixel 32", "pixel 33", "pixel 0", "pixel 1", " ", "pixel 32", "pixel 33", "pixel 0", " ", "pixel 32", "pixel 33"] },
				{ "name": "Col 2", "wave": "x===|=====|====|==x", "data": ["pixel 0", "pixel 1", " ", "pixel 32", "pixel 33", "pixel 0", "pixel 1", " ", "pixel 32", "pixel 33", "pixel 0", " ", "pixel 32", "pixel 33"] },
				{ "name": "Col 3", "wave": "x===|=====|====|==x", "data": ["pixel 0", "pixel 1", " ", "pixel 32", "pixel 33", "pixel 0", "pixel 1", " ", "pixel 32", "pixel 33", "pixel 0", " ", "pixel 32", "pixel 33"] }
		]
	],
  
	"edge" : [ "A<->B SCAN", "C<->D STEP", "E<->F FRAME" ],

	"config" : { "hscale" : 2 }
} 
""")
svg.saveas("expertise-adc.svg")