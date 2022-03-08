import wavedrom
svg = wavedrom.render("""
{ "signal" : 
	[
		["LINK 1",
			{ "name": "CLK", "wave": "p...........", "period":2 },
			{ "name": "CTRL", "wave": "01...=.0.=.0.=.0.....1..", "data": ["CTRLN [2]", "CTRLN [1]", "CTRLN [0]"] }, 
			["DATA",
				["Col 0",
					{ "name": " ", "wave": "x3.3.3.3.3.3.3.3.x...3.3", "data": ["Sci N [15]", "Sci N [14]", "Sci N [13]", "Sci N [12]", "Sci N [11]", "Sci N [10]", "Sci N [9]", "Sci N [8]", "Sci N+1 [15]"] },
					{ "name": " ", "wave": "x3.3.3.3.3.3.3.3.x...3.3", "data": ["Sci N [7]", "Sci N [6]", "Sci N [5]", "Sci N [4]", "Sci N [3]", "Sci N [2]", "Sci N [1]", "Sci N [0]", "Sci N+1 [7]"] }
				],
				["Col 1",
					{ "name": " ", "wave": "x5.5.5.5.5.5.5.5.x...5.5", "data": ["Sci N [15]", "Sci N [14]", "Sci N [13]", "Sci N [12]", "Sci N [11]", "Sci N [10]", "Sci N [9]", "Sci N [8]", "Sci N+1 [15]"] },
					{ "name": " ", "wave": "x5.5.5.5.5.5.5.5.x...5.5", "data": ["Sci N [7]", "Sci N [6]", "Sci N [5]", "Sci N [4]", "Sci N [3]", "Sci N [2]", "Sci N [1]", "Sci N [0]", "Sci N+1 [7]"] }
				]
			]
		],

		["LINK 2",
			{ "name": "CLK", "wave": "p...........", "period":2 },
			{ "name": "CTRL", "wave": "01...=.0.=.0.=.0.....1..", "data": ["CTRLN [2]", "CTRLN [1]", "CTRLN [0]"] }, 
			["DATA",
				["Col 2",
					{ "name": " ", "wave": "x4.4.4.4.4.4.4.4.x...4.4", "data": ["Sci N [15]", "Sci N [14]", "Sci N [13]", "Sci N [12]", "Sci N [11]", "Sci N [10]", "Sci N [9]", "Sci N [8]", "Sci N+1 [15]"] },
					{ "name": " ", "wave": "x4.4.4.4.4.4.4.4.x...4.4", "data": ["Sci N [7]", "Sci N [6]", "Sci N [5]", "Sci N [4]", "Sci N [3]", "Sci N [2]", "Sci N [1]", "Sci N [0]", "Sci N+1 [7]"] }
				],
				["Col 3",
					{ "name": " ", "wave": "x2.2.2.2.2.2.2.2.x...2.2", "data": ["Sci N [15]", "Sci N [14]", "Sci N [13]", "Sci N [12]", "Sci N [11]", "Sci N [10]", "Sci N [9]", "Sci N [8]", "Sci N+1 [15]"] },
					{ "name": " ", "wave": "x2.2.2.2.2.2.2.2.x...2.2", "data": ["Sci N [7]", "Sci N [6]", "Sci N [5]", "Sci N [4]", "Sci N [3]", "Sci N [2]", "Sci N [1]", "Sci N [0]", "Sci N+1 [7]"] }
				]
			]
		]
	],
	"config" : { "hscale" : 2 }
} 
""")
svg.saveas("interface-demux-ep-sci.svg")