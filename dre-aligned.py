import wavedrom
svg = wavedrom.render("""
{ "signal" : [
  ["DRE 1",
  { "name": "ck frame (~150 kHz)", "wave": "0.1......|..0....|....1." },
  { "name": "ck row (~5 MHz)", "wave": "n...|...|...", "period": 2},
  { "name": "signal", "wave": "=.=.=.=.=|=.=.=.=|=.=.=.", "data": ["Pix33", "Pix0", "Pix1", "Pix2", " ", "Pix16", "Pix17", "Pix18", "", "Pix32", "Pix33", "Pix0" ] },
   {}],
  
  ["DRE 2",
  { "name": "ck frame (~150 kHz)", "wave": "0.1......|..0....|....1." },
  { "name": "ck row (~5 MHz)", "wave": "n...|...|...", "period": 2},
  { "name": "signal", "wave": "=.=.=.=.=|=.=.=.=|=.=.=.", "data": ["Pix33", "Pix0", "Pix1", "Pix2", " ", "Pix16", "Pix17", "Pix18", "", "Pix32", "Pix33", "Pix0" ] },
   {}],
  
  ["DRE 3",
  { "name": "ck frame (~150 kHz)", "wave": "0.1......|..0....|....1." },
  { "name": "ck row (~5 MHz)", "wave": "n...|...|...", "period": 2},
  { "name": "signal", "wave": "=.=.=.=.=|=.=.=.=|=.=.=.", "data": ["Pix33", "Pix0", "Pix1", "Pix2", " ", "Pix16", "Pix17", "Pix18", "", "Pix32", "Pix33", "Pix0" ] },
   {}],
  
  ["DRE 4",
  { "name": "ck frame (~150 kHz)", "wave": "0.1......|..0....|....1." },
  { "name": "ck row (~5 MHz)", "wave": "n...|...|...", "period": 2},
  { "name": "signal", "wave": "=.=.=.=.=|=.=.=.=|=.=.=.", "data": ["Pix33", "Pix0", "Pix1", "Pix2", " ", "Pix16", "Pix17", "Pix18", "", "Pix32", "Pix33", "Pix0" ] },
   {}],
  
  ["DRE 5",
  { "name": "ck frame (~150 kHz)", "wave": "0.1......|..0....|....1." },
  { "name": "ck row (~5 MHz)", "wave": "n...|...|...", "period": 2},
  { "name": "signal", "wave": "=.=.=.=.=|=.=.=.=|=.=.=.", "data": ["Pix33", "Pix0", "Pix1", "Pix2", " ", "Pix16", "Pix17", "Pix18", "", "Pix32", "Pix33", "Pix0" ] },
   {}],
  
  ["DRE 6",
  { "name": "ck frame (~150 kHz)", "wave": "0.1......|..0....|....1." },
  { "name": "ck row (~5 MHz)", "wave": "n...|...|...", "period": 2},
  { "name": "signal", "wave": "=.=.=.=.=|=.=.=.=|=.=.=.", "data": ["Pix33", "Pix0", "Pix1", "Pix2", " ", "Pix16", "Pix17", "Pix18", "", "Pix32", "Pix33", "Pix0" ] },
   {}]
],
  "config" : { "hscale" : 1 }
}
  
""")
svg.saveas("dre-aligned.svg")