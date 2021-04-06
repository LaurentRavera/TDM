import wavedrom
svg = wavedrom.render("""
{ "signal" : 
 [
  { "name": "CTRL", "wave": "01...=.0.=.0.=.0...1..", "data": ["CTRLN [2]", "CTRLN [1]", "CTRLN [0]"] }, 
   ["DATA",
   	["Col 0",
	 { "name": " ", "wave": "x3.3.3.3.3.3.3.3.x.3.3", "data": ["PixN [15]", "PixN [14]", "PixN [13]", "PixN [12]", "PixN [11]", "PixN [10]", "PixN [9]", "PixN [8]", "PixN+1 [15]"] },
	 { "name": " ", "wave": "x3.3.3.3.3.3.3.3.x.3.3", "data": ["PixN [7]", "PixN [6]", "PixN [5]", "PixN [4]", "PixN [3]", "PixN [2]", "PixN [1]", "PixN [0]", "PixN+1 [7]"] }
    ],
   	["Col 1",
	 { "name": " ", "wave": "x5.5.5.5.5.5.5.5.x.5.5", "data": ["PixN [15]", "PixN [14]", "PixN [13]", "PixN [12]", "PixN [11]", "PixN [10]", "PixN [9]", "PixN [8]", "PixN+1 [15]"] },
	 { "name": " ", "wave": "x5.5.5.5.5.5.5.5.x.5.5", "data": ["PixN [7]", "PixN [6]", "PixN [5]", "PixN [4]", "PixN [3]", "PixN [2]", "PixN [1]", "PixN [0]", "PixN+1 [7]"] }
    ],
   	["Col 2",
	 { "name": " ", "wave": "x4.4.4.4.4.4.4.4.x.4.4", "data": ["PixN [15]", "PixN [14]", "PixN [13]", "PixN [12]", "PixN [11]", "PixN [10]", "PixN [9]", "PixN [8]", "PixN+1 [15]"] },
	 { "name": " ", "wave": "x4.4.4.4.4.4.4.4.x.4.4", "data": ["PixN [7]", "PixN [6]", "PixN [5]", "PixN [4]", "PixN [3]", "PixN [2]", "PixN [1]", "PixN [0]", "PixN+1 [7]"] }
    ],
   	["Col 3",
	 { "name": " ", "wave": "x2.2.2.2.2.2.2.2.x.2.2", "data": ["PixN [15]", "PixN [14]", "PixN [13]", "PixN [12]", "PixN [11]", "PixN [10]", "PixN [9]", "PixN [8]", "PixN+1 [15]"] },
	 { "name": " ", "wave": "x2.2.2.2.2.2.2.2.x.2.2", "data": ["PixN [7]", "PixN [6]", "PixN [5]", "PixN [4]", "PixN [3]", "PixN [2]", "PixN [1]", "PixN [0]", "PixN+1 [7]"] }
    ]
  ],
  { "name": "CLK", "wave": "p..........", "period":2 }
 ],
 "config" : { "hscale" : 1 }
} 
""")
svg.saveas("interface-demux-ep.svg")