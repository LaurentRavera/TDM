import wavedrom
svg = wavedrom.render("""
{ "signal" : 
	[
		["EP",
			{ "name": "SCLK", 		"wave": "0...P...............................l..", "period":1 },
			{ "name": "MOSI", 		"wave": "x...44444444444444444444444444444444x..", "data": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32"], "phase": 0.5 },
			{ "name": "<o>CS</o> DEMUX 0", "wave": "1..0................................1.." },
			{ "name": "CS DEMUX 1", "wave": "h......................................" },
			{ "name": "CS RAS", 	"wave": "h......................................" },
			{ "name": "MISO", 		"wave": "3...555555555555555555555555555555553..", "data": ["Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "Z"], "phase": 0.5 }
		],
		
  		{ "name": "", "wave": "" },

		["DEMUX 0",
			{ "name": "", "wave": "" },
			{ "name": "MISO", "wave": "3...555555555555555555555555555555553..", "data": ["Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "Z"], "phase": 0.5 },
			{ "name": "", "wave": "" }
		],

		["DEMUX 1",
			{ "name": "", "wave": "" },
			{ "name": "MISO", "wave": "3......................................", "data": ["Z"], "phase": 0.5 },
			{ "name": "", "wave": "" }
	],
  
  		["RAS",
			{ "name": "", "wave": "" },
			{ "name": "MISO", "wave": "3......................................", "data": ["Z"], "phase": 0.5 },
			{ "name": "", "wave": "" }
	]

	],
	"config" : { "hscale" : 1 }
} 
""")
svg.saveas("dre-internal-spi.svg")