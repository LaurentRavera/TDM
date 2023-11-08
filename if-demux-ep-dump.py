import wavedrom
svg = wavedrom.render("""
{ "signal" : 
	[
		{},
		{"node": ".A.......B..", "period": 2, "phase": 2},
		["LINK 0",
			{ "name": "CLK", "wave": "p...........", "period":2 },
		{ "name": "CTRL", "wave": "01...=.0.=.0.=.0.1...=.0", "data": ["CTRLN [2]", "CTRLN [1]", "CTRLN [0]", "CTRLN [2]"] }, 
			["DATA",
				["Col 0",
					{ "name": " ", "wave": "x3.3.3.3.3.3.3.3.3.3.3.3", "data": ["ADC N [15]", "ADC N [14]", "ADC N [13]", "ADC N [12]", "ADC N [11]", "ADC N [10]", "ADC N [9]", "ADC N [8]", "ADC N+1 [15]", "ADC N+1 [14]", "ADC N+1 [13]"] },
					{ "name": " ", "wave": "x3.3.3.3.3.3.3.3.3.3.3.3", "data": ["ADC N [7]", "ADC N [6]", "ADC N [5]", "ADC N [4]", "ADC N [3]", "ADC N [2]", "ADC N [1]", "ADC N [0]", "ADC N+1 [7]", "ADC N+1 [6]", "ADC N+1 [5]"] }
				],
				["Col 1",
					{ "name": " ", "wave": "x5.5.5.5.5.5.5.5.5.5.5.5", "data": ["ADC N [15]", "ADC N [14]", "ADC N [13]", "ADC N [12]", "ADC N [11]", "ADC N [10]", "ADC N [9]", "ADC N [8]", "ADC N+1 [15]", "ADC N+1 [14]", "ADC N+1 [13]"] },
					{ "name": " ", "wave": "x5.5.5.5.5.5.5.5.5.5.5.5", "data": ["ADC N [7]", "ADC N [6]", "ADC N [5]", "ADC N [4]", "ADC N [3]", "ADC N [2]", "ADC N [1]", "ADC N [0]", "ADC N+1 [7]", "ADC N+1 [6]", "ADC N+1 [5]"] }
				]
			]
		],
  
		{},

		["LINK 1",
			{ "name": "CLK", "wave": "p...........", "period":2 },
			{ "name": "CTRL", "wave": "01...=.0.=.0.=.0.1...=.0", "data": ["CTRLN [2]", "CTRLN [1]", "CTRLN [0]", "CTRLN [2]"] }, 
			["DATA",
				["Col 2",
					{ "name": " ", "wave": "x4.4.4.4.4.4.4.4.4.4.4.4", "data": ["ADC N [15]", "ADC N [14]", "ADC N [13]", "ADC N [12]", "ADC N [11]", "ADC N [10]", "ADC N [9]", "ADC N [8]", "ADC N+1 [15]", "ADC N+1 [14]", "ADC N+1 [13]"] },
					{ "name": " ", "wave": "x4.4.4.4.4.4.4.4.4.4.4.4", "data": ["ADC N [7]", "ADC N [6]", "ADC N [5]", "ADC N [4]", "ADC N [3]", "ADC N [2]", "ADC N [1]", "ADC N [0]", "ADC N+1 [7]", "ADC N+1 [6]", "ADC N+1 [5]"] }
				],
				["Col 3",
					{ "name": " ", "wave": "x2.2.2.2.2.2.2.2.2.2.2.2", "data": ["ADC N [15]", "ADC N [14]", "ADC N [13]", "ADC N [12]", "ADC N [11]", "ADC N [10]", "ADC N [9]", "ADC N [8]", "ADC N+1 [15]", "ADC N+1 [14]", "ADC N+1 [13]"] },
					{ "name": " ", "wave": "x2.2.2.2.2.2.2.2.2.2.2.2", "data": ["ADC N [7]", "ADC N [6]", "ADC N [5]", "ADC N [4]", "ADC N [3]", "ADC N [2]", "ADC N [1]", "ADC N [0]", "ADC N+1 [7]", "ADC N+1 [6]", "ADC N+1 [5]"] }
				]
			]
		]
	],

	"edge" : [ "A+B 128ns"		
	],

	"config" : { "hscale" : 2 }
} 
""")
svg.saveas("interface-demux-ep-adc.svg")