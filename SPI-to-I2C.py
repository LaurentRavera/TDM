import wavedrom
svg = wavedrom.render("""
{ 	"signal" : 
	[
		{},

		["SPI",
		
			{ "name": "SCLK", "phase": 0.5, "wave": "0.P...............................0"},

	   		["MOSI",

				{ "name": " ", "wave":  "x========44444443========55555555x", "data": ["AD14", "AD13", "AD12", "AD11", "AD10", "AD9", "AD8", "AD7", "AD6", "AD5", "AD4", "AD3", "AD2", "AD1", "AD0", "<o>R</o>/W", "DT15", "DT14", "DT13", "DT12", "DT11", "DT10", "DT9", "DT8", "DT7", "DT6", "DT5", "DT4", "DT3", "DT2", "DT1", "DT0"] },
				{ "name": " ", "wave":  "x========44444443========55555555x", "data": ["HD15", "HD14", "HD13", "HD12", "HD11", "HD10", "HD9", "HD8", "HD7", "HD6", "HD5", "HD4", "HD3", "HD2", "HD1", "HD0", "DT15", "DT14", "DT13", "DT12", "DT11", "DT10", "DT9", "DT8", "DT7", "DT6", "DT5", "DT4", "DT3", "DT2", "DT1", "DT0"] },
				{ "name": " "},	
				{ "name": "I2C content", "wave":  "x10......444444430.......55555555x", "data": ["AD6", "AD5", "AD4", "AD3", "AD2", "AD1", "AD0", "R/<o>W</o>", "DT7", "DT6", "DT5", "DT4", "DT3", "DT2", "DT1", "DT0"] }
			]
		]		
	],

	"config" : { "hscale" : 1 }
} 
""")
svg.saveas("SPI-to-I2C.svg")