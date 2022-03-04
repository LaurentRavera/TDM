import wavedrom
svg = wavedrom.render("""
{ "signal" : 
	[
		["LINK 1",
			{ "name": "CLK", "wave": "p..........", "period":2 },
			{ "name": "CTRL", "wave": "01...=.0.=.0.=.0...1..", "data": ["CTRLN [2]", "CTRLN [1]", "CTRLN [0]"] }, 
			["DATA",
				["Col 0",
					{ "name": " ", "wave": "x3.3.3.3.3.3.3.3.x.3.3", "data": ["Val N [15]", "Val N [14]", "Val N [13]", "Val N [12]", "Val N [11]", "Val N [10]", "Val N [9]", "Val N [8]", "Val N+1 [15]"] },
					{ "name": " ", "wave": "x3.3.3.3.3.3.3.3.x.3.3", "data": ["Val N [7]", "Val N [6]", "Val N [5]", "Val N [4]", "Val N [3]", "Val N [2]", "Val N [1]", "Val N [0]", "Val N+1 [7]"] }
				],
				["Col 1",
					{ "name": " ", "wave": "x5.5.5.5.5.5.5.5.x.5.5", "data": ["Val N [15]", "Val N [14]", "Val N [13]", "Val N [12]", "Val N [11]", "Val N [10]", "Val N [9]", "Val N [8]", "Val N+1 [15]"] },
					{ "name": " ", "wave": "x5.5.5.5.5.5.5.5.x.5.5", "data": ["Val N [7]", "Val N [6]", "Val N [5]", "Val N [4]", "Val N [3]", "Val N [2]", "Val N [1]", "Val N [0]", "Val N+1 [7]"] }
				]
			]
		],

		["LINK 2",
			{ "name": "CLK", "wave": "p..........", "period":2 },
			{ "name": "CTRL", "wave": "01...=.0.=.0.=.0...1..", "data": ["CTRLN [2]", "CTRLN [1]", "CTRLN [0]"] }, 
			["DATA",
				["Col 2",
					{ "name": " ", "wave": "x4.4.4.4.4.4.4.4.x.4.4", "data": ["Val N [15]", "Val N [14]", "Val N [13]", "Val N [12]", "Val N [11]", "Val N [10]", "Val N [9]", "Val N [8]", "Val N+1 [15]"] },
					{ "name": " ", "wave": "x4.4.4.4.4.4.4.4.x.4.4", "data": ["Val N [7]", "Val N [6]", "Val N [5]", "Val N [4]", "Val N [3]", "Val N [2]", "Val N [1]", "Val N [0]", "Val N+1 [7]"] }
				],
				["Col 3",
					{ "name": " ", "wave": "x2.2.2.2.2.2.2.2.x.2.2", "data": ["Val N [15]", "Val N [14]", "Val N [13]", "Val N [12]", "Val N [11]", "Val N [10]", "Val N [9]", "Val N [8]", "Val N+1 [15]"] },
					{ "name": " ", "wave": "x2.2.2.2.2.2.2.2.x.2.2", "data": ["Val N [7]", "Val N [6]", "Val N [5]", "Val N [4]", "Val N [3]", "Val N [2]", "Val N [1]", "Val N [0]", "Val N+1 [7]"] }
				]
			]
		]
	],
	"config" : { "hscale" : 1 }
} 
""")
svg.saveas("interface-demux-ep.svg")