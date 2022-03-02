import wavedrom
svg = wavedrom.render("""
{
"signal" : 
 [
  { "name": "Row address @ DRE output", "wave": "=.......=...................=...........", "period": 1, "node": "........a" },
  { "name": "Error signal @ DEMUX input", "wave": "4x5x", "data": ["data settled", "data settled"], "period": 10, "node": ".b" },
  {}, 
  { "name": "DEMUX ADC clk", "wave": "p.......................................", "period": 1 },
  { "name": "SYNC @ DEMUX input", "wave": "0........1.0............................", "node": ".........c", "period": 1 },
  { "name": "Pixel sequence in DEMUX", "wave": "=..........=...................=........", "node": "...........d", "period": 1 },
  { "name": "Boxcar", "wave": "0...1....0..............1....0..........", "node": "........................e", "period": 1 }
 ],
"edge":
 [
 "a~>b", "a~>c", "d~>e"
 ],
"config" : { "hscale" : 0.5, "skin": "narrow" }
} 
""")
svg.saveas("synchro-RA-ADC.svg")